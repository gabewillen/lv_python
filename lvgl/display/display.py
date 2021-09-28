import ctypes
from lvgl import lib


class Display(object):

    c_init = None

    def __init__(self, width, height, driver):
        self.driver = driver(width * height)
        self.driver.hor_res = width
        self.driver.ver_res = height
        self.c_ptr = lib.lv_disp_drv_register(self.driver.lv_disp_drv_ptr)



