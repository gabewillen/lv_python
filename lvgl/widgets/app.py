from lvgl.widgets.window import Window
from lvgl.obj import Obj, ObjMetaclass, with_metaclass, LV_OBJS
from lvgl.display.driver import get_driver
from threading import Thread
from lvgl import lib
import time



class App(object):
    display_driver = None
    width = 0
    height = 0
    title = 'App'

    def __init__(self,  **kwargs):
        self.display_driver = get_driver(self.display_driver)(kwargs.get('width', self.width), kwargs.get('height', self.height), **kwargs)
        self.window = None
        # self._lv_tick_thread = Thread(target=self._lv_tick, daemon=True)

    def _lv_tick(self):
        while self.running:
            lib.lv_tick_inc(5)
            # lib.lv_task_handler()
            time.sleep(.005)

    def build(self):
        return None

    def stop(self, *args):
        self.running = False
        self.window.close()

    def run(self):

        self.window = Window(title=self.title)
        self.window.add_btn_right(lib.LV_SYMBOL_CLOSE, on_clicked=self.stop)
        with self.window:
            self.build()
        self.running = True
        # self._lv_tick_thread.start()
        while self.running:
            lib.lv_tick_inc(1)
            lib.lv_task_handler()
            time.sleep(.001)
