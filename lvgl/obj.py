from lvgl import lib, lv_enum_to_dict
import ctypes
from weakref import ref
from threading import Timer
from six import with_metaclass
from lvgl.properties import AliasProperty, Property, VariableListProperty, OptionProperty

LV_OBJS = {}
LV_EVENTS = lv_enum_to_dict('LV_EVENT_')
LV_ALIGN = lv_enum_to_dict('LV_ALIGN_')


class ObjMetaclass(type):

    def __new__(mcs, name, bases, dct):
        cls = super(ObjMetaclass, mcs).__new__(mcs, name, bases, dct)
        cls.lv_parts = lv_enum_to_dict('LV_{}_PART_'.format(cls.lv_name.upper()))
        cls.__properties__ = set()
        for base in cls.__mro__:
            for key, item in base.__dict__.items():
                if isinstance(item, Property):
                    cls.__properties__.add(key)
                    item.__set_name__(base, key)
                elif key.startswith('on_') and key[3:] not in cls.__properties__:
                    cls.events.setdefault(key, set()).add(item)
        return cls
    #
    def __call__(mcs, *args, **kwargs):
        """
        You may be wondering why I chose to use a metaclass and more specifically intercept the call to __init__ adding more overhead.
        I felt it necessary considering python doesn't enforce super class initialization. It is essential that the lv_obj_ptr be created once for every lvgl object.
        If this were inside the  Obj.__init__ and the child class failed to call the super method it would result in a segmentation fault. These are extremely
        hard to debug in python. If you disagree I am open to criticism.
        :param args:
        :param kwargs:
        :return:
        """
        if 'lv_obj_ptr' not in kwargs:
            # no lv_obj_ptr no problem lets find out if this object has a parent or we will use the display and create one
            # parent = kwargs.setdefault('parent', Obj(lv_obj_ptr=lib.lv_disp_get_scr_act(lib.lv_disp_get_default())))
            parent = kwargs.get('parent', None)
            if parent is None:
                if not Obj.stack:
                    parent = kwargs['parent'] = Obj(lv_obj_ptr=lib.lv_disp_get_scr_act(lib.lv_disp_get_default()))
                    Obj.stack.append(parent) # this is the display and will always remain in the stack
                else:
                    parent = Obj.stack[-1]
            lv_obj_ptr = kwargs['lv_obj_ptr'] = mcs.lv_create(parent.lv_obj_ptr, None)
        else:
            lv_obj_ptr = kwargs['lv_obj_ptr']
        address = ctypes.addressof(lv_obj_ptr.contents)
        if address in LV_OBJS: # we already have an obj with this lv_obj_ptr no need to create another one
            return LV_OBJS[address]
        else:
            # attach an event observer for this object
            obj = super(ObjMetaclass, mcs).__call__(*args, **kwargs)
            lib.lv_obj_set_event_cb(lv_obj_ptr, lib.lv_event_cb_t(event_cb))
            return obj


def event_cb(ptr, event, *args):
    obj = LV_OBJS.get(ctypes.addressof(ptr.contents), None)
    if obj is not None:
        obj.on_event(event, *args)


def lv_getter(name, attr):
    def getter(self, c_call=getattr(lib, 'lv_{}_get_{}'.format(name, attr))):
        return c_call(self.lv_obj_ptr)

    return getter


def lv_setter(name, attr):
    def setter(self, value, c_call=getattr(lib, 'lv_{}_set_{}'.format(name, attr))):
        c_call(self.lv_obj_ptr, value)

    return setter

#
class LV_Obj_Property(AliasProperty):


    def link(self, instance, name=None):
        super(LV_Obj_Property, self).link(instance, name)
        self.setter = lv_setter(self.owner_class.lv_name, self.name)
        self.getter = lv_getter(self.owner_class.lv_name, self.name)


class Obj(object, with_metaclass(ObjMetaclass)):
    lv_create = lib.lv_obj_create
    lv_name = 'obj'
    lv_parts = None
    lv_states = lv_enum_to_dict('LV_STATE_')
    lv_protections = lv_enum_to_dict('LV_PROTECT_')
    lv_ext_click_areas = lv_enum_to_dict('LV_EXT_CLICK_AREA_')

    stack = []
    events = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Obj, cls).__new__(cls)
        lv_obj_ptr = kwargs.pop('lv_obj_ptr')
        LV_OBJS[ctypes.addressof(lv_obj_ptr.contents)] = obj #ref(obj)
        obj.lv_obj_ptr = lv_obj_ptr
        return obj

    def on_event(self, c_event, *args):
        callbacks = self.events.get('on_{}'.format(LV_EVENTS[c_event]), set())
        for callback in callbacks:
            callback(self, *args)

    def bind(self, **kwargs):
        for key, item in kwargs.items():
            property = getattr(self.__class__, key[3:], None)
            if property is not None:
                property.add_observer(self, item)
            else:
                self.events.setdefault(key, set()).add(item)

    def link_properties(self):
        for property in self.__properties__:
            getattr(self.__class__, property).link(self)

    def __init__(self,  **kwargs):
        self.events = self.__class__.events.copy()
        self.link_properties()
        for key, item in kwargs.items():
            if key.startswith('on_'):
                self.bind(**{key: item})
            else:
                setattr(self, key, item)
        self._parent = lib.lv_obj_get_parent(self.lv_obj_ptr)


    width = LV_Obj_Property()
    height = LV_Obj_Property()
    x = LV_Obj_Property()
    y = LV_Obj_Property()

    lv_obj_ptr = None


    def get_pos(self):
        return self.x, self.y

    def set_pos(self, pos):
        if isinstance(pos, (list, tuple)):
            x, y = pos
        elif isinstance(pos, dict):
            x = pos.get('x', self.x)
            y = pos.get('y', self.y)
        else:
            x = y = pos
        lib.lv_obj_set_pos(self.lv_obj_ptr, x, y)
        self.x = x
        self.y = y

    pos = AliasProperty(get_pos, set_pos, bind=('x', 'y'))

    align_x = Property(0)
    align_y = Property(0)
    align_to = Property(None)
    align_type = OptionProperty(LV_ALIGN, default_value=LV_ALIGN['center'])

    def set_align(self, align):

        obj = align[0]
        if obj is not None:
            obj = obj.lv_obj_ptr
        align_x, align_y = align[2:]
        align = align[1]
        lib.lv_obj_align(self.lv_obj_ptr, obj, align, align_x, align_y)

    align = VariableListProperty([align_to, align_type, align_x, align_y], setter=set_align)


    _parent = None

    def get_parent(self):
        parent_ptr = lib.lv_obj_get_parent(self.lv_obj_ptr)
        if parent_ptr:
            return Obj(lv_obj_ptr=parent_ptr)

    def set_parent(self, parent):
        if parent != self.parent:
            lib.lv_obj_set_parent(self.lv_obj_ptr, parent.lv_obj_ptr)

    parent = AliasProperty(get_parent, set_parent)

    def move_foreground(self):
        lib.lv_obj_move_foreground(self.lv_obj_ptr)

    def move_background(self):
        lib.lv_obj_move_background(self.lv_obj_ptr)

    def get_hidden(self):
        return lib.lv_obj_get_hidden(self.lv_obj_ptr)


    def set_hidden(self, value):
        lib.lv_obj_set_hidden(self.lv_obj_ptr, value)


    hidden = AliasProperty(get_hidden, set_hidden)

    def get_visible(self):
        return lib.lv_obj_is_visible(self.lv_obj_ptr)

    visible = AliasProperty(get_visible)


    click = LV_Obj_Property()
    top = LV_Obj_Property()
    drag = LV_Obj_Property()
    drag_dir = LV_Obj_Property()
    drag_throw = LV_Obj_Property()
    drag_parent = LV_Obj_Property()
    focus_parent = LV_Obj_Property()
    gesture_parent = LV_Obj_Property()
    parent_event = LV_Obj_Property()
    base_dir = LV_Obj_Property()

    width_margin = LV_Obj_Property()
    height_margin = LV_Obj_Property()
    width_fit = LV_Obj_Property()
    height_fit = LV_Obj_Property()
    auto_realign = LV_Obj_Property()

    def get_radius(self, part='main'):
        return lib._lv_obj_get_style_int(self.lv_obj_ptr, self.lv_parts[part], lib.LV_STYLE_RADIUS)

    def set_radius(self, value, part='main', state='default'):
        lib._lv_obj_set_style_local_int(self.lv_obj_ptr, self.lv_parts[part],
                                        lib.LV_STYLE_RADIUS | (self.lv_states[state] << lib.LV_STYLE_STATE_POS), value)

    radius = AliasProperty(get_radius, set_radius)

    _children = []

    def get_children(self):
        return self._children

    def set_children(self, children):
        for child in children:
            child.parent = self
        self._children = children

    children = AliasProperty(get_children, set_children)

    def on_delete(self, *args):
        del LV_OBJS[ctypes.addressof(self.lv_obj_ptr.contents)]


    def clean(self):
        lib.lv_obj_clean(self.lv_obj_ptr)

    def area_is_visible(self, area):
        lv_area = lib.lv_area_t()
        lv_area.x1 = area[0]
        lv_area.y1 = area[1]
        lv_area.x2 = area[2]
        lv_area.y2 = area[3]
        return lib.lv_obj_area_is_visible(self.lv_obj_ptr, area)

    def invalidate_area(self, area):
        lv_area = lib.lv_area_t()
        lv_area.x1 = area[0]
        lv_area.y1 = area[1]
        lv_area.x2 = area[2]
        lv_area.y2 = area[3]
        return lib.lv_obj_invalidate_area(self.lv_obj_ptr, area)

    def invalidate(self):
        return lib.lv_obj_invalidate(self.lv_obj_ptr)


    def __enter__(self):
        self.stack.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stack.pop(-1)
