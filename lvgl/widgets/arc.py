from lvgl.obj import Obj, lib#, LV_Obj_Property
from lvgl.widgets import MinMaxMixin, TypeMixin
from lvgl.properties import AliasProperty

class Arc(MinMaxMixin, TypeMixin, Obj):

    lv_create = lib.lv_arc_create
    lv_name = 'arc'

    # start_angle = LV_Obj_Property()
    # end_angle = LV_Obj_Property()

    def get_angle(self):
        return self.start_angle, self.end_angle

    def set_angle(self, value):
        lib.lv_arc_set_angles(self.lv_obj_ptr, value[0], value[1])

    angle = AliasProperty(get_angle, set_angle)

    def get_bg_end_angle(self):
        return lib.lv_arc_get_bg_angle_end(self.lv_obj_ptr)

    def set_bg_end_angle(self, value):
        lib.lv_arc_set_bg_end_angle(self.lv_obj_ptr, value)

    @property
    def bg_start_angle(self):
        return lib.lv_arc_get_bg_angle_start(self.lv_obj_ptr)

    @bg_start_angle.setter
    def bg_start_angle(self, value):
        lib.lv_arc_set_bg_start_angle(self.lv_obj_ptr, value)

    @property
    def bg_angle(self):
        return self.bg_start_angle, self.bg_end_angle

    @bg_angle.setter
    def bg_angle(self, bg_angle):
        lib.lv_arc_set_bg_angles(self.lv_obj_ptr, bg_angle[0], bg_angle[1])

    @property
    def arc_type(self):
        return lib.lv_arc_get_type(self.lv_obj_ptr)

    @arc_type.setter
    def arc_type(self, arc_type='normal'):
        lib.lv_arc_set_type(self.lv_obj_ptr, getattr(lib, 'LV_ARC_TYPE_{}'.format(arc_type.upper())))

    @property
    def dragged(self):
        return lib.lv_arc_is_dragged(self.lv_obj_ptr)

    @property
    def adjustable(self):
        return lib.lv_arc_get_adjustable(self.lv_obj_ptr)

