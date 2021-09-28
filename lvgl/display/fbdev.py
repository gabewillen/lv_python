from lvgl.display.driver import DisplayDriver, register
from lvgl.display.display import Display
from lvgl import lib, lv_symbols


@register
class FBDev(DisplayDriver):
    lv_init = lib.fbdev_init
    lv_flush_cb = lib.fbdev_flush

    def __init__(self, width, height, input_device_path=None, input_device_symbol=None):
        width = lib.c_int(width)
        height = lib.c_int(height)
        lib.fbdev_init(width, height)
        lib.fbdev_get_sizes(lib.cast(lib.pointer(width), lib.POINTER(lib.c_uint32)), lib.cast(lib.pointer(height), lib.POINTER(lib.c_uint32)))
        print(width, height)
        lib.evdev_init()
        super(FBDev, self).__init__(width.value, height.value)
        self.lv_input = lib.lv_indev_drv_t()
        self.lv_input_ptr = lib.pointer(self.lv_input)
        self.lv_input.type = lib.LV_INDEV_TYPE_POINTER
        if input_device_path is not None:
            lib.evdev_set_file(input_device_path)
        self.lv_input.read_cb = type(self.lv_input.read_cb)(lib.evdev_read)
        self.lv_input_dev_ptr = lib.lv_indev_drv_register(self.lv_input_ptr)
        if input_device_symbol is not None:
            self.lv_input_cursor_ptr = lib.lv_img_create(lib.lv_disp_get_scr_act(self.lv_disp_ptr), None)
            lib.lv_img_set_src(self.lv_input_cursor_ptr, lv_symbols[input_device_symbol])
            lib.lv_indev_set_cursor(self.lv_input_dev_ptr, self.lv_input_cursor_ptr)

