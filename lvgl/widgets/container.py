from lvgl import lib, lv_enum_to_dict
from lvgl.obj import Obj
from lvgl.properties import AliasProperty, OptionProperty, VariableListProperty

LV_LAYOUT = lv_enum_to_dict('LV_LAYOUT_')
LV_FIT = lv_enum_to_dict('LV_FIT_')


class Container(Obj):
    lv_create = lib.lv_cont_create

    def get_layout(self):
        c_layout = lib.lv_cont_get_layout(self.lv_obj_ptr)
        return LV_LAYOUT[c_layout]

    def set_layout(self, layout):
        lib.lv_cont_set_layout(self.lv_obj_ptr, layout)

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
    }, setter=set_layout)

    # def get_fit_left(self):
    #     return LV_FIT[lib.lv_cont_get_fit_left(self.lv_obj_ptr)]
    #
    # def set_fit_left(self, fit):
    #     lv_obj_ptr = self.lv_obj_ptr
    #     lib.lv_cont_set_fit4(lv_obj_ptr, LV_FIT[fit], lib.lv_cont_get_fit_right(lv_obj_ptr),
    #                          lib.lv_cont_get_fit_top(lv_obj_ptr),
    #                          lib.lv_cont_get_fit_bottom(lv_obj_ptr))
    #
    # fit_left = AliasProperty(get_fit_left, set_fit_left)
    #
    # def get_fit_right(self):
    #     return LV_FIT[lib.lv_cont_get_fit_right(self.lv_obj_ptr)]
    #
    # def set_fit_right(self, fit):
    #     lv_obj_ptr = self.lv_obj_ptr
    #     lib.lv_cont_set_fit4(lv_obj_ptr,
    #                          lib.lv_cont_get_fit_left(lv_obj_ptr), LV_FIT[fit],
    #                          lib.lv_cont_get_fit_top(lv_obj_ptr), lib.lv_cont_get_fit_bottom(lv_obj_ptr))
    #
    # fit_right = AliasProperty(get_fit_right, set_fit_right)
    #
    # def get_fit_top(self):
    #     return LV_FIT[lib.lv_cont_get_fit_top(self.lv_obj_ptr)]
    #
    # def set_fit_top(self, fit):
    #     lv_obj_ptr = self.lv_obj_ptr
    #     lib.lv_cont_set_fit4(lv_obj_ptr,
    #                          lib.lv_cont_get_fit_left(lv_obj_ptr),
    #                          lib.lv_cont_get_fit_right(lv_obj_ptr), LV_FIT[fit],
    #                          lib.lv_cont_get_fit_bottom(lv_obj_ptr))
    #
    # fit_top = AliasProperty(get_fit_top, set_fit_top)
    #
    # def get_fit_bottom(self):
    #     return LV_FIT[lib.lv_cont_get_fit_bottom(self.lv_obj_ptr)]
    #
    # def set_fit_bottom(self, fit):
    #     lv_obj_ptr = self.lv_obj_ptr
    #     lib.lv_cont_set_fit4(lv_obj_ptr,
    #                          lib.lv_cont_get_fit_left(lv_obj_ptr),
    #                          lib.lv_cont_get_fit_right(lv_obj_ptr),
    #                          lib.lv_cont_get_fit_top(lv_obj_ptr),
    #                          LV_FIT[fit])


    fit_options = {
        None: lib.LV_FIT_NONE,
        'tight': lib.LV_FIT_TIGHT,
        'parent': lib.LV_FIT_PARENT,
        'max': lib.LV_FIT_MAX,
        'none': lib.LV_FIT_NONE
    }

    fit_left = OptionProperty(fit_options, getter=lambda self: lib.lv_cont_get_fit_left(self.lv_obj_ptr))
    fit_right = OptionProperty(fit_options, getter=lambda self: lib.lv_cont_get_fit_right(self.lv_obj_ptr))
    fit_top = OptionProperty(fit_options, getter=lambda self: lib.lv_cont_get_fit_top(self.lv_obj_ptr))
    fit_bottom = OptionProperty(fit_options,  getter=lambda self: lib.lv_cont_get_fit_bottom(self.lv_obj_ptr))

    def get_fit(self):
        return self.fit_left, self.fit_right, self.fit_top, self.fit_bottom

    def set_fit(self, value):
        fit = list(self.fit)
        if isinstance(value, (tuple, list)):
            for val, i in enumerate(value):
                fit[i] = self.fit_options[val]
        else:
            fit = [self.fit_options[value]] * len(fit)
        print('set_fit', fit)
        lib.lv_cont_set_fit4(self.lv_obj_ptr, *fit)

    fit = AliasProperty(setter=set_fit, getter=get_fit)
