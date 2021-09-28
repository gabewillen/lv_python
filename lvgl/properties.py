# from weakref import finalize
from functools import partial
from threading import Lock


class Property(object):

    def __init__(self, default_value=None):
        self.default_value = default_value
        self.owner_class = None
        self.name = None
        self.callbacks = {}
        self.dispatching = False

    def link(self, instance, name=None):
        if name is None:
            if self.name is None:
                for base in instance.__class__.__mro__:
                    for key, item in base.__dict__.items():
                        if item is self:
                            self.name = name = key
                            break
                    if name is not None:
                        break
            else:
                name = self.name
        else:
            self.name = name
        self.__dict__.setdefault(instance, self.default_value)
        # finalize(instance, self.__dict__.pop, instance)
        method = getattr(instance, 'on_{}'.format(name), None)
        if method is not None:
            self.add_observer(instance, method)

    def add_observer(self, instance, method, *args, **kwargs):
        callback = partial(method, *args, **kwargs)
        self.callbacks.setdefault(instance, list()).append(callback)
        # finalize(method, self.callbacks[instance].remove, callback)

    def callback(self, instance, value):
        if not self.dispatching:
            self.dispatching = True
            callbacks = self.callbacks.setdefault(instance, list())
            for index in range(len(callbacks)):
                method = callbacks.pop(0)
                method(value)
                callbacks.append(method)
            self.dispatching = False

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.get(instance)

    def __set__(self, instance, value):
        if not instance in self.__dict__:
            self.link(instance)
        self.set(instance, value)

    def set(self, instance, value, **kwargs):
        current = kwargs.get('current_value', self.__get__(instance))
        if current != value:
            self.__dict__[instance] = value
            self.callback(instance, value)

    def get(self, instance):
        return self.__dict__.setdefault(instance, self.default_value)

    def __set_name__(self, owner, name):
        self.owner_class = owner
        self.name = name




class AliasProperty(Property):

    def __init__(self, getter=None, setter=None, bind=None, **kwargs):
        super(AliasProperty, self).__init__(**kwargs)
        self.getter = getter if getter is not None else super(AliasProperty, self).get
        self.setter = setter if setter is not None else super(AliasProperty, self).set
        self.locked = False
        self.bound_properties = bind if bind is not None else []

    def get(self, instance):
        value = self.__dict__[instance] = self.getter(instance)
        return value

    def set(self, instance, value, **kwargs):
        current = kwargs.get('current', self.__get__)
        if current == value:
            return
        elif self.setter is None:
            raise AttributeError("can't set attribute")
        if not self.locked:
            self.locked = True
            if self.setter(instance, value) is None:
                super(AliasProperty, self).set(instance, value, current_value=current)
            self.locked = False

    def update(self, instance, *args):
        if not self.locked:
            old = super(AliasProperty, self).get(instance)
            new = self.get(instance)
            if new != old:
                self.callback(instance, new)

    def link(self, instance, name=None):
        super(AliasProperty, self).link(instance, name)
        for property in self.bound_properties:
            getattr(instance.__class__, property).add_observer(instance, self.update, instance)


class OptionProperty(AliasProperty):

    def __init__(self, options, getter=None, setter=None, default_value=None, **kwargs):
        if getter is None:
            getter = super(AliasProperty, self).get
        if setter is None:
            setter = super(AliasProperty, self).set
        if not isinstance(options, dict):
            if default_value is None:
                default_value = options[0]
            options = dict((item, item) for item in options)
        elif default_value is None:
            default_value = list(options.values())[0]
        self.options = options
        super(OptionProperty, self).__init__(getter, setter, default_value=default_value, **kwargs)

    def set(self, instance, value, **kwargs):
        if value not in self.options:
            raise KeyError('{} is not a valid option. valid options are {}'.format(value, tuple(self.options.keys())))
        super(OptionProperty, self).set(instance, self.options[value])


class VariableListProperty(AliasProperty):

    def __init__(self, default_value=None, length=None, getter=None, setter=None):
        self.length = length if length is not None else len(default_value)
        super(VariableListProperty, self).__init__(getter, setter, default_value=default_value)

    def get(self, instance):
        current_value = list(super(VariableListProperty, self).get(instance))
        default_value = self.default_value
        for index in range(self.length):
            if isinstance(default_value[index], Property):
                current_value[index] = default_value[index].__get__(instance)
        return current_value

    def set(self, instance, value, **kwargs):
        if not isinstance(value, (list, tuple)):
            value = [value]
        current_value = self.get(instance)
        default_value = self.default_value
        new_value = list(current_value)
        value_length = len(value)
        for index in range(self.length):
            if isinstance(default_value[index], Property):
                default_value[index].__set__(instance, value[index % value_length])
                new_value[index] = default_value[index].__get__(instance)
            else:
                new_value[index] = value[index % value_length]
        super(VariableListProperty, self).set(instance, new_value, current_value=current_value)

    def update(self, instance, index, value):
        current_value = super(VariableListProperty, self).get(instance)
        if current_value[index] != value:
            value = self.get(instance)
            super(VariableListProperty, self).set(instance, value, current_value=current_value)

    def link(self, instance, name=None):
        super(VariableListProperty, self).link(instance, None)
        for index, item in enumerate(self.default_value):
            if isinstance(item, Property):
                item.add_observer(instance, self.update, instance, index)


if __name__ == '__main__':
    class Test(object):
        a = Property(0)
        b = Property(0)

        def get_c(self):
            return self.a, self.b

        def set_c(self, value):
            self.a = value[0]
            self.b = value[1]

        c = AliasProperty(get_c, set_c, ('a', 'b'))

        def on_a(self, value):
            print("on_a", value)

        def on_b(self, value):
            print('on_b', value)

        def on_c(self, value):
            print('on_c', value)

        def d_setter(self, value):
            print('d_setter', value)

        d = VariableListProperty([None, a, b], setter=d_setter)

        def on_d(self, value):
            print('on_d', value)

    t = Test()
    Test.a.link(t, 'a')
    Test.b.link(t, 'b')
    Test.c.link(t, 'c')
    Test.d.link(t, 'd')
    t.a = 2
    t.b = 1
    t.c = 3, 4
    t.d = 0
    print(Test.a.callbacks)
