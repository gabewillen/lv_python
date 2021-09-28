
from lvgl.widgets.container import Container, lib
from lvgl.widgets.label import Label
from lvgl.properties import AliasProperty

class Button(Container):
    lv_create = lib.lv_btn_create
    lv_name = 'btn'

    _label = None

    def get_checkable(self):
        return lib.lv_btn_get_checkable(self.lv_obj_ptr)

    def set_checkable(self, value):
        lib.lv_btn_set_checkable(self.lv_obj_ptr, value)

    checkable = AliasProperty(get_checkable, set_checkable)

    def get_state(self):
        return lib.lv_btn_get_state(self.lv_obj_ptr)

    def set_state(self, state):
        lib.lv_btn_set_state(self.lv_obj_ptr, getattr(lib, 'LV_BTN_STATE_{}'.format(state.upper())))

    state = AliasProperty(get_state, set_state)

    def get_label(self):
        return self._label

    def set_label(self, text):
        self._label = Label(parent=self, text=text)

    label = AliasProperty(get_label, set_label)