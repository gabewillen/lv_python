from lvgl.obj import lib
from lvgl.properties import AliasProperty, Property

class Mixin:
    __lv_method_name = None

    def lvgl_call(self, method, *args):
        return getattr(lib, 'lv_{}_{}'.format(self.__class__.__name__.lower(), method))(self.lv_obj_ptr, *args)


class ValueMixin(Mixin):

    def get_value(self):
        return self.lvgl_call('get_value')

    def set_value(self, value):
        self.lvgl_call('set_value', value)

    value = AliasProperty(get_value, set_value)

class TypeMixin(Mixin):

    def get_type(self):
        return self.lvgl_call('get_type')

    def set_type(self, type):
        self.lvgl_call('set_type', getattr(lib, 'LV_{}_TYPE_'.format(self.__class__.__name__.lower(), type.upper())))

    type = AliasProperty(get_type, set_type)

class MinMaxMixin(ValueMixin):

    def get_min_value(self):
        return self.lvgl_call('get_min_value')

    def set_min_value(self, min_value):
        self.range = min_value, self.max_value

    min_value = AliasProperty(get_min_value, set_min_value)

    def get_max_value(self):
        return self.lvgl_call('get_max_value')

    def set_max_value(self, max_value):
        self.range = self.min_value, self.max_value

    max_value = AliasProperty(get_max_value, set_max_value)

    def get_range(self):
        return self.min_value, self.max_value

    def set_range(self, range):
        self.lvgl_call('set_range', *range)

    range = AliasProperty(get_range, set_range, bind=('min_value', 'max_value'))