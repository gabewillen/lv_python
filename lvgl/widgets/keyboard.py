from lvgl.widgets import lib
from lvgl.obj import Obj, LV_EVENTS

LV_KEYBOARD_MODE = {
    lib.LV_KEYBOARD_MODE_TEXT_LOWER: 'text_lower',
    lib.LV_KEYBOARD_MODE_TEXT_UPPER: 'text_upper',
    lib.LV_KEYBOARD_MODE_SPECIAL: 'special',
    lib.LV_KEYBOARD_MODE_NUM: 'num'
}

LV_KEYBOARD_MODE.update(dict((item, key) for key, item in LV_KEYBOARD_MODE.items()))


class Keyboard(Obj):

    lv_create = lib.lv_keyboard_create


    def on_event(self, c_event, *args):
        lib.lv_keyboard_def_event_cb(self.lv_obj_ptr, c_event)
        super(Keyboard, self).on_event(c_event, *args)

    @property
    def textarea(self):
        return lib.lv_keyboard_get_textarea(self.lv_obj_ptr)

    @textarea.setter
    def textarea(self, widget):
        lib.lv_keyboard_set_textarea(self.lv_obj_ptr, widget.lv_obj_ptr)

    @property
    def mode(self):
        return lib.lv_keyboard_get_mode(self.lv_obj_ptr)

    @mode.setter
    def mode(self, mode):
        lib.lv_keyboard_set_mode(self.lv_obj_ptr, LV_KEYBOARD_MODE[mode])


    def show(self):
        self.hidden = False

    def hide(self):
        self.hidden = True

    # TODO implement the rest of API