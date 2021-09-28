import ctypes

from lvgl import lib, lv_enum_to_dict

DRIVERS = {}

class DisplayBuffer(object):

    def __init__(self, size):
        self.c_buf = (lib.lv_color_t * size)()
        self.c_val = lib.lv_disp_buf_t()
        self.c_ptr = lib.pointer(self.c_val)
        lib.lv_disp_buf_init(self.c_ptr, lib.cast(self.c_buf, lib.c_void_p), None, size)


class DisplayDriver(object):

    lv_flush_cb = None
    lv_init = None

    def __init__(self, hor_res, ver_res):
        self.buffer = DisplayBuffer(hor_res * ver_res)
        self.lv_disp_drv = lib.lv_disp_drv_t()
        self.lv_disp_drv_ptr = ctypes.pointer(self.lv_disp_drv)
        lib.lv_disp_drv_init(self.lv_disp_drv_ptr)
        self.lv_disp_drv.hor_res = hor_res
        self.lv_disp_drv.ver_res = ver_res
        self.lv_disp_drv.buffer = self.buffer.c_ptr
        self.lv_disp_drv.flush_cb = type(self.lv_disp_drv.flush_cb)(self.lv_flush_cb)
        self.lv_disp_ptr = lib.lv_disp_drv_register(self.lv_disp_drv_ptr)

    @property
    def hor_res(self):
        return self.lv_disp_drv.hor_res

    @hor_res.setter
    def hor_res(self, value):
        self.lv_disp_drv.hor_res = value

    @property
    def ver_res(self):
        return self.lv_disp_drv.ver_res

    @ver_res.setter
    def ver_res(self, value):
        self.lv_disp_drv.ver_res = value

def register(cls):
    DRIVERS[cls.__name__.lower()] = cls
    return cls

def get_driver(name):
    return DRIVERS[name]