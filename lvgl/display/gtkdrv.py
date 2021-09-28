from lvgl.display.driver import DisplayDriver, register
from lvgl.input.driver import InputDriver
import ctypes
from lvgl import lib


class GtkMouseDriver(object):

    def __init__(self):
        self.driver = InputDriver(lib.LV_INDEV_TYPE_POINTER, lib.gtkdrv_mouse_read_cb)
        self.c_ptr = lib.lv_indev_drv_register(self.driver.c_ptr)

@register
class GtkDrv(DisplayDriver):

    lv_flush_cb = lib.gtkdrv_flush_cb

    def __init__(self, width, height, **kwargs):
        lib.gtkdrv_init(width, height)
        super(GtkDrv, self).__init__(width, height)
        self.mouse_driver = GtkMouseDriver()