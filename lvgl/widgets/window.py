from lvgl import lib, lv_enum_to_dict, lv_symbols
from lvgl.obj import Obj, LV_Obj_Property, LV_EVENTS
from lvgl.properties import AliasProperty, OptionProperty
from lvgl.widgets.button import Button




class Window(Obj):

    lv_create = lib.lv_win_create
    lv_layouts = lv_enum_to_dict('LV_LAYOUT_')
    lv_name = 'win'

    def close(self):
        lib.lv_obj_del(self.lv_obj_ptr)

    title = LV_Obj_Property()
    # header_height = LV_Obj_Property()
    # btn_width = LV_Obj_Property()

    def _set_layout(self, layout):
        lib.lv_win_set_layout(self.lv_obj_ptr, layout)

    def _get_layout(self):
        return lib.lv_win_get_layout(self.lv_obj_ptr)

    layout = OptionProperty({
        'off': lib.LV_LAYOUT_OFF,
        'center': lib.LV_LAYOUT_CENTER,
        'column_left': lib.LV_LAYOUT_COLUMN_LEFT,
        'column_mid': lib.LV_LAYOUT_COLUMN_MID,
        'column_right': lib.LV_LAYOUT_COLUMN_RIGHT,
        'row_top': lib.LV_LAYOUT_ROW_TOP,
        'pretty_top': lib.LV_LAYOUT_PRETTY_TOP,
        'pretty_mid': lib.LV_LAYOUT_PRETTY_MID,
        'pretty_bottom': lib.LV_LAYOUT_PRETTY_BOTTOM,
        'grid': lib.LV_LAYOUT_GRID
    }, setter=_set_layout)

    def clean(self):
        lib.lv_win_clean(self.lv_obj_ptr)

    def add_btn_right(self, img, **kwargs):
        return Button(lv_obj_ptr=lib.lv_win_add_btn_right(self.lv_obj_ptr, img), **kwargs)


    def add_btn_left(self, img):
        return lib.lv_win_add_btn_left(self.lv_obj_ptr, img)

