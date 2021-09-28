from lvgl.obj import Obj, lib
from lvgl.widgets.page import Page
from lvgl.properties import AliasProperty

class TabView(Obj):

    lv_create = lib.lv_tabview_create
    lv_name = 'tabview'
    _tabs = {}

    def __init__(self, **kwargs):
        self._tabs = {}
        super(TabView, self).__init__(**kwargs)

    def tab_index(self, name):
        return list(self._tabs.keys()).index(name)

    def add_tab(self, name):
        self._tabs[name] = Page(lv_obj_ptr=lib.lv_tabview_add_tab(self.lv_obj_ptr, name))

    def clean_tab(self):
        lib.lv_tabview_clean_tab(self.lv_obj_ptr)

    def set_tabs(self, tabs):
        for tab in tabs:
            self.add_tab(tab)

    def get_tabs(self):
        return self._tabs

    tabs = AliasProperty(get_tabs, set_tabs)

    def set_active_tab(self, name, animate=lib.LV_ANIM_ON):
        lib.lv_tabview_set_tab_act(self.lv_obj_ptr, self.tab_index(name), animate)

    def get_active_tab(self):
        return self._tabs[list(self._tabs.keys())[lib.lv_tabview_get_tab_act(self.lv_obj_ptr)]]

    active_tab = AliasProperty(get_active_tab, set_active_tab)