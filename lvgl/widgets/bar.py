from lvgl.obj import Obj, lib
from lvgl.widgets import MinMaxMixin, TypeMixin

class Bar(MinMaxMixin, TypeMixin, Obj):

    lv_create = lib.lv_bar_create

    def start_value(self, value=None, animation='on'):
        if value is not None:
            lib.lv_bar_set_start_value(self.lv_obj_ptr, value, getattr(lib, f'LV_ANIM_{animation.upper()}'))
        return lib.lv_bar_get_start_value(self.lv_obj_ptr)

    @property
    def anim_time(self):
        return lib.lv_bar_get_anim_time(self.lv_obj_ptr)

    @anim_time.setter
    def anim_time(self, time):
        lib.lv_bar_set_anim_time(self.lv_obj_ptr, time)

