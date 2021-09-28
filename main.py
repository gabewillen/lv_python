from lvgl.widgets.app import App
from lvgl.widgets.button import Button
from lvgl.widgets.keyboard import Keyboard
from lvgl.widgets.text_area import TextArea
from lvgl.widgets.tabview import TabView


class Main(App):

    display_driver = 'gtkdrv'
    width = 1024
    height = 768
    title = 'Shaper'

    def build_auto_tab(self, tab):
        tab.layout = 'grid'
        with tab:
            TextArea(cursor_hidden=True)
            Button(label='start', align_type='in_bottom_left')

    def build_edit_tab(self, tab):
        tab.scrollbar_mode = 'off'
        with tab:
            editor = TextArea(align_type='in_top_left', width=int(tab.width * .8), height=tab.height // 2)
            load_button = Button(label='Load', align_to=editor, align_type='out_right_top', align_x=50)
            Button(label='Save', align_to=load_button, align_type='out_bottom_left')
            keyboard = Keyboard(textarea=editor)

    def build_jog_tab(self, tab):
        tab.layout = 'grid'
        with tab:
            Button(label='-', height=tab.height, width=tab.width // 3)
            Button(label='+', align_type='in_top_right', height=tab.height, width=tab.width // 3)

    def build(self):
        self.window.layout = 'grid'
        main = TabView(tabs=['Auto','Edit', 'Jog', 'Offset'])
        self.build_auto_tab(main.tabs['Auto'])
        self.build_edit_tab(main.tabs['Edit'])
        self.build_jog_tab(main.tabs['Jog'])

Main(input_device_path='/dev/input/event21', input_device_symbol='bullet').run()

