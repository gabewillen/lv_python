import lvgl.liblvgl as lib
from lvgl.properties import AliasProperty



class Style(object):

    def __init__(self, obj=None, **kwargs):
        for key, item in kwargs.items():
            setattr(self, key, item)
        self.obj_ptr = obj.c_ptr if obj is not None else obj

    def get_radius(self):
        pass
