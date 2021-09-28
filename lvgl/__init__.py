import lvgl.liblvgl as lib
import atexit
from weakref import ref

# from lvgl.properties import OptionProperty

lib.lv_init()
print('lib.lv_init()')


# atexit.register(lib.lv_deinit)


def lv_enum_to_dict(lv_prefix='LV_', mirror=True, dct=None):
    if dct is None:
        dct = dict((key[len(lv_prefix):].lower(), item) for key, item in lib.__dict__.items() if key.startswith(lv_prefix))
    if mirror:
        dct.update(dict((item, key) for key, item in dct.items()))
    return dct


lv_symbols = lv_enum_to_dict('LV_SYMBOL_', False)


def lv_enum(seq=None, **kwargs):
    dct = dict(seq, **kwargs)
    dct.update(dict((item, key) for key, item in dct.items()))
    return dct
