from lvgl.obj import Obj, lib, LV_Obj_Property
from lvgl.properties import AliasProperty

class Image(Obj):
    lv_create = lib.lv_img_create
    lv_name = 'img'

    src = LV_Obj_Property()
    offset_x = LV_Obj_Property()
    offset_y = LV_Obj_Property()
    pivot = LV_Obj_Property()
    angle = LV_Obj_Property()