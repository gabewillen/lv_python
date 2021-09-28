from lvgl.widgets import lib
from lvgl.obj import Obj
from itertools import takewhile

class ButtonMatrix(Obj):

    lv_create = lib.lv_btnmatrix_create
    lv_name = 'btnmatrix'

    @property
    def map(self):
        array = lib.cast(lib.lv_btnmatrix_get_map_array(self.lv_obj_ptr), lib.POINTER(lib.c_char_p))
        return [string for string in takewhile(bool, array)]

    @map.setter
    def map(self, mapping):
        c_array = (lib.c_char_p * len(mapping))(*mapping)
        lib.lv_btnmatrix_set_map(self.lv_obj_ptr, lib.cast(c_array, lib.POINTER(lib.POINTER(lib.c_char))))