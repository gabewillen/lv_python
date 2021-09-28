import sys
import os
import shutil
import glob
import pkgconfig
from ctypesgen.main import main

if len(sys.argv) <= 1:
    sys.argv = ['setup.py', 'build']

from setuptools import setup, Extension

#  https://stackoverflow.com/questions/4529555/building-a-ctypes-based-c-library-with-distutils
from distutils.command.build_ext import build_ext as build_ext_orig


class CTypesExtension(Extension): pass


class build_ext(build_ext_orig):

    def build_extension(self, ext):
        self._ctypes = isinstance(ext, CTypesExtension)
        return super().build_extension(ext)

    def get_export_symbols(self, ext):
        if self._ctypes:
            return ext.export_symbols
        return super().get_export_symbols(ext)

    def get_ext_filename(self, ext_name):
        if self._ctypes:
            return ext_name + '.so'
        return super().get_ext_filename(ext_name)


sources = []
for path in 'lv_core', 'lv_draw', 'lv_font', 'lv_gpu', 'lv_hal', 'lv_misc', 'lv_themes', 'lv_widgets':
    sources.extend(glob.glob('lib/lvgl/src/' + path + '/*.c'))
sources.extend(glob.glob('lib/lv_drivers/*.c'))
lv_driver_dirs = ['indev', 'display']
compile_args = ['-Wall', '-Wshadow', '-Wundef', '-fPIC', '-O3', '-g3', '-I./lib']
link_args = ['-lpthread', '-shared']
try:
    compile_args.extend(pkgconfig.cflags('gtk+-3.0').split(' '))
    link_args.extend(pkgconfig.libs('gtk+-3.0').split(' '))
    lv_driver_dirs.append('gtkdrv')
except pkgconfig.PackageNotFoundError:
    pass
for path in lv_driver_dirs:
    sources.extend(glob.glob('lib/lv_drivers/' + path + '/*.c'))


module1 = CTypesExtension('_lvgl',
                          sources=sources,
                          extra_compile_args=compile_args,
                          extra_link_args=link_args
                          )

dist = setup(name='lvgl',
             version='0.1',
             description='lvgl bindings',
             ext_modules=[module1],
             cmdclass={'build_ext': build_ext}
             )

for output in dist.get_command_obj('build_ext').get_outputs():
    shutil.copy(output, '.')
