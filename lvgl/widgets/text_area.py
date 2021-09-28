from lvgl.obj import Obj, lib
from lvgl.properties import AliasProperty


class TextArea(Obj):
    lv_create = lib.lv_textarea_create

    def add_char(self, char):
        lib.lv_textarea_add_char(self.lv_obj_ptr, lib.c_char(char))

    def add_text(self, text):
        lib.lv_textarea_add_text(self.lv_obj_ptr, lib.create_string_buffer(text))

    def del_char(self, direction=-1):
        if direction > 0:
            lib.lv_textarea_del_char_forward(self.lv_obj_ptr)
        else:
            lib.lv_textarea_del_char(self.lv_obj_ptr)

    def get_text(self):
        return lib.lv_textarea_get_text(self.lv_obj_ptr)

    def set_text(self, text):
        lib.lv_textarea_set_text(self.lv_obj_ptr, lib.create_string_buffer(text))

    text = AliasProperty(get_text, set_text)

    def get_placeholder_text(self):
        return lib.lv_textarea_get_placeholder_text(self.lv_obj_ptr)

    def set_placeholder_text(self, text):
        lib.lv_textarea_set_placeholder_text(self.lv_obj_ptr, lib.create_string_buffer(text))

    placeholder_text = AliasProperty(get_placeholder_text, set_placeholder_text)

    def get_cursor_position(self):
        return lib.lv_textarea_get_cursor_pos(self.lv_obj_ptr)

    def set_cursor_position(self, pos):
        return lib.lv_textarea_set_cursor_pos(self.lv_obj_ptr, pos)

    cursor_position = AliasProperty(get_cursor_position, set_cursor_position)

    def set_cursor_hidden(self, value):
        lib.lv_textarea_set_cursor_hidden(self.lv_obj_ptr, value)

    def get_cursor_hidden(self):
        return lib.lv_textarea_get_cursor_hidden(self.lv_obj_ptr)

    cursor_hidden = AliasProperty(get_cursor_hidden, set_cursor_hidden)