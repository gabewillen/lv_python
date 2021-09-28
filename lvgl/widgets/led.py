from lvgl.obj import Obj, LV_Obj_Property, lib

class Led(Obj):

    lv_create = lib.lv_led_create
    lv_name = 'led'

    def on(self):
        lib.lv_led_on(self.lv_obj_ptr)

    def off(self):
        lib.lv_led_off(self.lv_obj_ptr)

    def toggle(self):
        lib.lv_led_toggle(self.lv_obj_ptr)

    bright = LV_Obj_Property()