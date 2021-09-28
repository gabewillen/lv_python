from lvgl import lib
from lvgl.obj import Obj
from lvgl.properties import AliasProperty

class Label(Obj):

    lv_create = lib.lv_label_create


    def get_text(self):
        return lib.lv_label_get_text(self.lv_obj_ptr)


    def set_text(self, text):
        lib.lv_label_set_text(self.lv_obj_ptr, text)

    text = AliasProperty(get_text, set_text)