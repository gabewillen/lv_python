from lvgl.obj import Obj, lib, lv_enum_to_dict
from lvgl.properties import AliasProperty, OptionProperty
from lvgl.widgets.container import Container

lv_scrollbar_modes = lv_enum_to_dict('LV_SCRLBAR_MODE_')

LV_SCROLLBAR_MODES = lv_enum_to_dict(dct={
        'off': lib.LV_SCROLLBAR_MODE_OFF,
        'on': lib.LV_SCROLLBAR_MODE_ON,
        'drag': lib.LV_SCROLLBAR_MODE_DRAG,
        'auto': lib.LV_SCROLLBAR_MODE_AUTO,
        'hide': lib.LV_SCROLLBAR_MODE_HIDE,
        'unhide': lib.LV_SCROLLBAR_MODE_UNHIDE
    })

class Page(Container):

    lv_create = lib.lv_page_create


    def lv_page_clean(self):
        lib.lv_page_clean(self.lv_obj_ptr)

    def set_scrollbar_mode(self, mode):
        lib.lv_page_set_scrollbar_mode(self.lv_obj_ptr, mode)

    def get_scrollbar_mode(self):
        return LV_SCROLLBAR_MODES[lib.lv_page_get_scrollbar_mode(self.lv_obj_ptr)]

    scrollbar_mode = OptionProperty(LV_SCROLLBAR_MODES, getter=get_scrollbar_mode, setter=set_scrollbar_mode)

