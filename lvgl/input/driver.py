from lvgl import lib
import ctypes

class InputDriver:

    def __init__(self, driver_type, read_cb):
        indev_drv = self.c_val = lib.lv_indev_drv_t()
        self.c_ptr = ctypes.pointer(self.c_val)
        lib.lv_indev_drv_init(self.c_ptr)
        indev_drv.type = driver_type
        indev_drv.read_cb = type(indev_drv.read_cb)(read_cb)
