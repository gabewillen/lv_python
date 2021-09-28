from lvgl.input.driver import InputDriver
from lvgl import lib

class MouseDriver(InputDriver):

    def __init__(self, read_cb):
        super(MouseDriver, self).__init__(lib.LV_INDEV_TYPE_POINTER, read_cb)