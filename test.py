r"""Wrapper for _lvgl.h

Generated with:
venv/bin/ctypesgen lib/_lvgl.h -a -o test.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# No libraries

# No modules

__u_char = c_ubyte# /usr/include/bits/types.h: 31

__u_short = c_uint# /usr/include/bits/types.h: 32

__u_int = c_uint# /usr/include/bits/types.h: 33

__u_long = c_ulong# /usr/include/bits/types.h: 34

__int8_t = c_char# /usr/include/bits/types.h: 37

__uint8_t = c_ubyte# /usr/include/bits/types.h: 38

__int16_t = c_int# /usr/include/bits/types.h: 39

__uint16_t = c_uint# /usr/include/bits/types.h: 40

__int32_t = c_int# /usr/include/bits/types.h: 41

__uint32_t = c_uint# /usr/include/bits/types.h: 42

__int64_t = c_long# /usr/include/bits/types.h: 44

__uint64_t = c_ulong# /usr/include/bits/types.h: 45

__int_least8_t = __int8_t# /usr/include/bits/types.h: 52

__uint_least8_t = __uint8_t# /usr/include/bits/types.h: 53

__int_least16_t = __int16_t# /usr/include/bits/types.h: 54

__uint_least16_t = __uint16_t# /usr/include/bits/types.h: 55

__int_least32_t = __int32_t# /usr/include/bits/types.h: 56

__uint_least32_t = __uint32_t# /usr/include/bits/types.h: 57

__int_least64_t = __int64_t# /usr/include/bits/types.h: 58

__uint_least64_t = __uint64_t# /usr/include/bits/types.h: 59

__quad_t = c_long# /usr/include/bits/types.h: 63

__u_quad_t = c_ulong# /usr/include/bits/types.h: 64

__intmax_t = c_long# /usr/include/bits/types.h: 72

__uintmax_t = c_ulong# /usr/include/bits/types.h: 73

__dev_t = c_ulong# /usr/include/bits/types.h: 145

__uid_t = c_uint# /usr/include/bits/types.h: 146

__gid_t = c_uint# /usr/include/bits/types.h: 147

__ino_t = c_ulong# /usr/include/bits/types.h: 148

__ino64_t = c_ulong# /usr/include/bits/types.h: 149

__mode_t = c_uint# /usr/include/bits/types.h: 150

__nlink_t = c_ulong# /usr/include/bits/types.h: 151

__off_t = c_long# /usr/include/bits/types.h: 152

__off64_t = c_long# /usr/include/bits/types.h: 153

__pid_t = c_int# /usr/include/bits/types.h: 154

# /usr/include/bits/types.h: 155
class struct_anon_1(Structure):
    pass

struct_anon_1.__slots__ = [
    '__val',
]
struct_anon_1._fields_ = [
    ('__val', c_int * int(2)),
]

__fsid_t = struct_anon_1# /usr/include/bits/types.h: 155

__clock_t = c_long# /usr/include/bits/types.h: 156

__rlim_t = c_ulong# /usr/include/bits/types.h: 157

__rlim64_t = c_ulong# /usr/include/bits/types.h: 158

__id_t = c_uint# /usr/include/bits/types.h: 159

__time_t = c_long# /usr/include/bits/types.h: 160

__useconds_t = c_uint# /usr/include/bits/types.h: 161

__suseconds_t = c_long# /usr/include/bits/types.h: 162

__suseconds64_t = c_long# /usr/include/bits/types.h: 163

__daddr_t = c_int# /usr/include/bits/types.h: 165

__key_t = c_int# /usr/include/bits/types.h: 166

__clockid_t = c_int# /usr/include/bits/types.h: 169

__timer_t = POINTER(None)# /usr/include/bits/types.h: 172

__blksize_t = c_long# /usr/include/bits/types.h: 175

__blkcnt_t = c_long# /usr/include/bits/types.h: 180

__blkcnt64_t = c_long# /usr/include/bits/types.h: 181

__fsblkcnt_t = c_ulong# /usr/include/bits/types.h: 184

__fsblkcnt64_t = c_ulong# /usr/include/bits/types.h: 185

__fsfilcnt_t = c_ulong# /usr/include/bits/types.h: 188

__fsfilcnt64_t = c_ulong# /usr/include/bits/types.h: 189

__fsword_t = c_long# /usr/include/bits/types.h: 192

__ssize_t = c_long# /usr/include/bits/types.h: 194

__syscall_slong_t = c_long# /usr/include/bits/types.h: 197

__syscall_ulong_t = c_ulong# /usr/include/bits/types.h: 199

__loff_t = __off64_t# /usr/include/bits/types.h: 203

__caddr_t = String# /usr/include/bits/types.h: 204

__intptr_t = c_long# /usr/include/bits/types.h: 207

__socklen_t = c_uint# /usr/include/bits/types.h: 210

__sig_atomic_t = c_int# /usr/include/bits/types.h: 215

int8_t = __int8_t# /usr/include/bits/stdint-intn.h: 24

int16_t = __int16_t# /usr/include/bits/stdint-intn.h: 25

int32_t = __int32_t# /usr/include/bits/stdint-intn.h: 26

int64_t = __int64_t# /usr/include/bits/stdint-intn.h: 27

uint8_t = __uint8_t# /usr/include/bits/stdint-uintn.h: 24

uint16_t = __uint16_t# /usr/include/bits/stdint-uintn.h: 25

uint32_t = __uint32_t# /usr/include/bits/stdint-uintn.h: 26

uint64_t = __uint64_t# /usr/include/bits/stdint-uintn.h: 27

int_least8_t = __int_least8_t# /usr/include/stdint.h: 43

int_least16_t = __int_least16_t# /usr/include/stdint.h: 44

int_least32_t = __int_least32_t# /usr/include/stdint.h: 45

int_least64_t = __int_least64_t# /usr/include/stdint.h: 46

uint_least8_t = __uint_least8_t# /usr/include/stdint.h: 49

uint_least16_t = __uint_least16_t# /usr/include/stdint.h: 50

uint_least32_t = __uint_least32_t# /usr/include/stdint.h: 51

uint_least64_t = __uint_least64_t# /usr/include/stdint.h: 52

int_fast8_t = c_char# /usr/include/stdint.h: 58

int_fast16_t = c_long# /usr/include/stdint.h: 60

int_fast32_t = c_long# /usr/include/stdint.h: 61

int_fast64_t = c_long# /usr/include/stdint.h: 62

uint_fast8_t = c_ubyte# /usr/include/stdint.h: 71

uint_fast16_t = c_ulong# /usr/include/stdint.h: 73

uint_fast32_t = c_ulong# /usr/include/stdint.h: 74

uint_fast64_t = c_ulong# /usr/include/stdint.h: 75

intptr_t = c_long# /usr/include/stdint.h: 87

uintptr_t = c_ulong# /usr/include/stdint.h: 90

intmax_t = __intmax_t# /usr/include/stdint.h: 101

uintmax_t = __uintmax_t# /usr/include/stdint.h: 102

lv_coord_t = c_int16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 70

lv_anim_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 153

lv_group_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 188

lv_fs_drv_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 215

lv_img_decoder_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 247

lv_disp_drv_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 307

lv_indev_drv_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 308

lv_font_user_data_t = POINTER(None)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 444

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 33
class struct__silence_gcc_warning(Structure):
    pass

lv_log_level_t = c_int8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 40

ptrdiff_t = c_long# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stddef.h: 143

size_t = c_ulong# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stddef.h: 209

wchar_t = c_int# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stddef.h: 321

# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stddef.h: 426
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    '__max_align_ll',
    '__max_align_ld',
]
struct_anon_2._fields_ = [
    ('__max_align_ll', c_longlong),
    ('__max_align_ld', c_longdouble),
]

max_align_t = struct_anon_2# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stddef.h: 426

enum_anon_3 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 45

LV_RES_INV = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 45

LV_RES_OK = (LV_RES_INV + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 45

lv_res_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 50

lv_uintptr_t = uintptr_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 54

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 51
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'total_size',
    'free_cnt',
    'free_size',
    'free_biggest_size',
    'used_cnt',
    'max_used',
    'used_pct',
    'frag_pct',
]
struct_anon_4._fields_ = [
    ('total_size', c_uint32),
    ('free_cnt', c_uint32),
    ('free_size', c_uint32),
    ('free_biggest_size', c_uint32),
    ('used_cnt', c_uint32),
    ('max_used', c_uint32),
    ('used_pct', c_uint8),
    ('frag_pct', c_uint8),
]

lv_mem_monitor_t = struct_anon_4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 51

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 57
class struct_anon_5(Structure):
    pass

struct_anon_5.__slots__ = [
    'p',
    'size',
    'used',
]
struct_anon_5._fields_ = [
    ('p', POINTER(None)),
    ('size', c_uint16),
    ('used', c_uint8, 1),
]

lv_mem_buf_t = struct_anon_5# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 57

lv_mem_buf_arr_t = lv_mem_buf_t * int(16)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 59

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 60
for _lib in _libs.values():
    try:
        _lv_mem_buf = (lv_mem_buf_arr_t).in_dll(_lib, "_lv_mem_buf")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 69
for _lib in _libs.values():
    if not _lib.has("_lv_mem_init", "cdecl"):
        continue
    _lv_mem_init = _lib.get("_lv_mem_init", "cdecl")
    _lv_mem_init.argtypes = []
    _lv_mem_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 75
for _lib in _libs.values():
    if not _lib.has("_lv_mem_deinit", "cdecl"):
        continue
    _lv_mem_deinit = _lib.get("_lv_mem_deinit", "cdecl")
    _lv_mem_deinit.argtypes = []
    _lv_mem_deinit.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_mem_alloc", "cdecl"):
        continue
    lv_mem_alloc = _lib.get("lv_mem_alloc", "cdecl")
    lv_mem_alloc.argtypes = [c_size_t]
    lv_mem_alloc.restype = POINTER(c_ubyte)
    lv_mem_alloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_mem_free", "cdecl"):
        continue
    lv_mem_free = _lib.get("lv_mem_free", "cdecl")
    lv_mem_free.argtypes = [POINTER(None)]
    lv_mem_free.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 97
for _lib in _libs.values():
    if not _lib.has("lv_mem_realloc", "cdecl"):
        continue
    lv_mem_realloc = _lib.get("lv_mem_realloc", "cdecl")
    lv_mem_realloc.argtypes = [POINTER(None), c_size_t]
    lv_mem_realloc.restype = POINTER(c_ubyte)
    lv_mem_realloc.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_mem_defrag", "cdecl"):
        continue
    lv_mem_defrag = _lib.get("lv_mem_defrag", "cdecl")
    lv_mem_defrag.argtypes = []
    lv_mem_defrag.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 108
for _lib in _libs.values():
    if not _lib.has("lv_mem_test", "cdecl"):
        continue
    lv_mem_test = _lib.get("lv_mem_test", "cdecl")
    lv_mem_test.argtypes = []
    lv_mem_test.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 115
for _lib in _libs.values():
    if not _lib.has("lv_mem_monitor", "cdecl"):
        continue
    lv_mem_monitor = _lib.get("lv_mem_monitor", "cdecl")
    lv_mem_monitor.argtypes = [POINTER(lv_mem_monitor_t)]
    lv_mem_monitor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 122
for _lib in _libs.values():
    if not _lib.has("_lv_mem_get_size", "cdecl"):
        continue
    _lv_mem_get_size = _lib.get("_lv_mem_get_size", "cdecl")
    _lv_mem_get_size.argtypes = [POINTER(None)]
    _lv_mem_get_size.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 128
for _lib in _libs.values():
    if not _lib.has("_lv_mem_buf_get", "cdecl"):
        continue
    _lv_mem_buf_get = _lib.get("_lv_mem_buf_get", "cdecl")
    _lv_mem_buf_get.argtypes = [c_uint32]
    _lv_mem_buf_get.restype = POINTER(c_ubyte)
    _lv_mem_buf_get.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 134
for _lib in _libs.values():
    if not _lib.has("_lv_mem_buf_release", "cdecl"):
        continue
    _lv_mem_buf_release = _lib.get("_lv_mem_buf_release", "cdecl")
    _lv_mem_buf_release.argtypes = [POINTER(None)]
    _lv_mem_buf_release.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 139
for _lib in _libs.values():
    if not _lib.has("_lv_mem_buf_free_all", "cdecl"):
        continue
    _lv_mem_buf_free_all = _lib.get("_lv_mem_buf_free_all", "cdecl")
    _lv_mem_buf_free_all.argtypes = []
    _lv_mem_buf_free_all.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 205
for _lib in _libs.values():
    if not _lib.has("_lv_memcpy", "cdecl"):
        continue
    _lv_memcpy = _lib.get("_lv_memcpy", "cdecl")
    _lv_memcpy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    _lv_memcpy.restype = POINTER(c_ubyte)
    _lv_memcpy.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 215
for _lib in _libs.values():
    try:
        d8 = (POINTER(c_uint8)).in_dll(_lib, "d8")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 216
for _lib in _libs.values():
    try:
        s8 = (POINTER(c_uint8)).in_dll(_lib, "s8")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 234
for _lib in _libs.values():
    if not _lib.has("_lv_memset", "cdecl"):
        continue
    _lv_memset = _lib.get("_lv_memset", "cdecl")
    _lv_memset.argtypes = [POINTER(None), c_uint8, c_size_t]
    _lv_memset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 241
for _lib in _libs.values():
    if not _lib.has("_lv_memset_00", "cdecl"):
        continue
    _lv_memset_00 = _lib.get("_lv_memset_00", "cdecl")
    _lv_memset_00.argtypes = [POINTER(None), c_size_t]
    _lv_memset_00.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 248
for _lib in _libs.values():
    if not _lib.has("_lv_memset_ff", "cdecl"):
        continue
    _lv_memset_ff = _lib.get("_lv_memset_ff", "cdecl")
    _lv_memset_ff.argtypes = [POINTER(None), c_size_t]
    _lv_memset_ff.restype = None
    break

lv_ll_node_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 30

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 37
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'n_size',
    'head',
    'tail',
]
struct_anon_6._fields_ = [
    ('n_size', c_uint32),
    ('head', POINTER(lv_ll_node_t)),
    ('tail', POINTER(lv_ll_node_t)),
]

lv_ll_t = struct_anon_6# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 37

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 48
for _lib in _libs.values():
    if not _lib.has("_lv_ll_init", "cdecl"):
        continue
    _lv_ll_init = _lib.get("_lv_ll_init", "cdecl")
    _lv_ll_init.argtypes = [POINTER(lv_ll_t), c_uint32]
    _lv_ll_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 55
for _lib in _libs.values():
    if not _lib.has("_lv_ll_ins_head", "cdecl"):
        continue
    _lv_ll_ins_head = _lib.get("_lv_ll_ins_head", "cdecl")
    _lv_ll_ins_head.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_ins_head.restype = POINTER(c_ubyte)
    _lv_ll_ins_head.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 63
for _lib in _libs.values():
    if not _lib.has("_lv_ll_ins_prev", "cdecl"):
        continue
    _lv_ll_ins_prev = _lib.get("_lv_ll_ins_prev", "cdecl")
    _lv_ll_ins_prev.argtypes = [POINTER(lv_ll_t), POINTER(None)]
    _lv_ll_ins_prev.restype = POINTER(c_ubyte)
    _lv_ll_ins_prev.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 70
for _lib in _libs.values():
    if not _lib.has("_lv_ll_ins_tail", "cdecl"):
        continue
    _lv_ll_ins_tail = _lib.get("_lv_ll_ins_tail", "cdecl")
    _lv_ll_ins_tail.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_ins_tail.restype = POINTER(c_ubyte)
    _lv_ll_ins_tail.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 78
for _lib in _libs.values():
    if not _lib.has("_lv_ll_remove", "cdecl"):
        continue
    _lv_ll_remove = _lib.get("_lv_ll_remove", "cdecl")
    _lv_ll_remove.argtypes = [POINTER(lv_ll_t), POINTER(None)]
    _lv_ll_remove.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 84
for _lib in _libs.values():
    if not _lib.has("_lv_ll_clear", "cdecl"):
        continue
    _lv_ll_clear = _lib.get("_lv_ll_clear", "cdecl")
    _lv_ll_clear.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_clear.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 94
for _lib in _libs.values():
    if not _lib.has("_lv_ll_chg_list", "cdecl"):
        continue
    _lv_ll_chg_list = _lib.get("_lv_ll_chg_list", "cdecl")
    _lv_ll_chg_list.argtypes = [POINTER(lv_ll_t), POINTER(lv_ll_t), POINTER(None), c_bool]
    _lv_ll_chg_list.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 101
for _lib in _libs.values():
    if not _lib.has("_lv_ll_get_head", "cdecl"):
        continue
    _lv_ll_get_head = _lib.get("_lv_ll_get_head", "cdecl")
    _lv_ll_get_head.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_get_head.restype = POINTER(c_ubyte)
    _lv_ll_get_head.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 108
for _lib in _libs.values():
    if not _lib.has("_lv_ll_get_tail", "cdecl"):
        continue
    _lv_ll_get_tail = _lib.get("_lv_ll_get_tail", "cdecl")
    _lv_ll_get_tail.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_get_tail.restype = POINTER(c_ubyte)
    _lv_ll_get_tail.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 116
for _lib in _libs.values():
    if not _lib.has("_lv_ll_get_next", "cdecl"):
        continue
    _lv_ll_get_next = _lib.get("_lv_ll_get_next", "cdecl")
    _lv_ll_get_next.argtypes = [POINTER(lv_ll_t), POINTER(None)]
    _lv_ll_get_next.restype = POINTER(c_ubyte)
    _lv_ll_get_next.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 124
for _lib in _libs.values():
    if not _lib.has("_lv_ll_get_prev", "cdecl"):
        continue
    _lv_ll_get_prev = _lib.get("_lv_ll_get_prev", "cdecl")
    _lv_ll_get_prev.argtypes = [POINTER(lv_ll_t), POINTER(None)]
    _lv_ll_get_prev.restype = POINTER(c_ubyte)
    _lv_ll_get_prev.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 131
for _lib in _libs.values():
    if not _lib.has("_lv_ll_get_len", "cdecl"):
        continue
    _lv_ll_get_len = _lib.get("_lv_ll_get_len", "cdecl")
    _lv_ll_get_len.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_get_len.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 147
for _lib in _libs.values():
    if not _lib.has("_lv_ll_move_before", "cdecl"):
        continue
    _lv_ll_move_before = _lib.get("_lv_ll_move_before", "cdecl")
    _lv_ll_move_before.argtypes = [POINTER(lv_ll_t), POINTER(None), POINTER(None)]
    _lv_ll_move_before.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_ll.h: 154
for _lib in _libs.values():
    if not _lib.has("_lv_ll_is_empty", "cdecl"):
        continue
    _lv_ll_is_empty = _lib.get("_lv_ll_is_empty", "cdecl")
    _lv_ll_is_empty.argtypes = [POINTER(lv_ll_t)]
    _lv_ll_is_empty.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 60
class struct__lv_task_t(Structure):
    pass

lv_task_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_task_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 41

enum_anon_7 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_OFF = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_LOWEST = (LV_TASK_PRIO_OFF + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_LOW = (LV_TASK_PRIO_LOWEST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_MID = (LV_TASK_PRIO_LOW + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_HIGH = (LV_TASK_PRIO_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

LV_TASK_PRIO_HIGHEST = (LV_TASK_PRIO_HIGH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

_LV_TASK_PRIO_NUM = (LV_TASK_PRIO_HIGHEST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 46

lv_task_prio_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 55

struct__lv_task_t.__slots__ = [
    'period',
    'last_run',
    'task_cb',
    'user_data',
    'repeat_count',
    'prio',
]
struct__lv_task_t._fields_ = [
    ('period', c_uint32),
    ('last_run', c_uint32),
    ('task_cb', lv_task_cb_t),
    ('user_data', POINTER(None)),
    ('repeat_count', c_int32),
    ('prio', c_uint8, 3),
]

lv_task_t = struct__lv_task_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 69

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 78
for _lib in _libs.values():
    if not _lib.has("_lv_task_core_init", "cdecl"):
        continue
    _lv_task_core_init = _lib.get("_lv_task_core_init", "cdecl")
    _lv_task_core_init.argtypes = []
    _lv_task_core_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 86
for _lib in _libs.values():
    if not _lib.has("lv_task_handler", "cdecl"):
        continue
    lv_task_handler = _lib.get("lv_task_handler", "cdecl")
    lv_task_handler.argtypes = []
    lv_task_handler.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_task_create_basic", "cdecl"):
        continue
    lv_task_create_basic = _lib.get("lv_task_create_basic", "cdecl")
    lv_task_create_basic.argtypes = []
    lv_task_create_basic.restype = POINTER(lv_task_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 107
for _lib in _libs.values():
    if not _lib.has("lv_task_create", "cdecl"):
        continue
    lv_task_create = _lib.get("lv_task_create", "cdecl")
    lv_task_create.argtypes = [lv_task_cb_t, c_uint32, lv_task_prio_t, POINTER(None)]
    lv_task_create.restype = POINTER(lv_task_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_task_del", "cdecl"):
        continue
    lv_task_del = _lib.get("lv_task_del", "cdecl")
    lv_task_del.argtypes = [POINTER(lv_task_t)]
    lv_task_del.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_task_set_cb", "cdecl"):
        continue
    lv_task_set_cb = _lib.get("lv_task_set_cb", "cdecl")
    lv_task_set_cb.argtypes = [POINTER(lv_task_t), lv_task_cb_t]
    lv_task_set_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_task_set_prio", "cdecl"):
        continue
    lv_task_set_prio = _lib.get("lv_task_set_prio", "cdecl")
    lv_task_set_prio.argtypes = [POINTER(lv_task_t), lv_task_prio_t]
    lv_task_set_prio.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_task_set_period", "cdecl"):
        continue
    lv_task_set_period = _lib.get("lv_task_set_period", "cdecl")
    lv_task_set_period.argtypes = [POINTER(lv_task_t), c_uint32]
    lv_task_set_period.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 140
for _lib in _libs.values():
    if not _lib.has("lv_task_ready", "cdecl"):
        continue
    lv_task_ready = _lib.get("lv_task_ready", "cdecl")
    lv_task_ready.argtypes = [POINTER(lv_task_t)]
    lv_task_ready.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 147
for _lib in _libs.values():
    if not _lib.has("lv_task_set_repeat_count", "cdecl"):
        continue
    lv_task_set_repeat_count = _lib.get("lv_task_set_repeat_count", "cdecl")
    lv_task_set_repeat_count.argtypes = [POINTER(lv_task_t), c_int32]
    lv_task_set_repeat_count.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 154
for _lib in _libs.values():
    if not _lib.has("lv_task_reset", "cdecl"):
        continue
    lv_task_reset = _lib.get("lv_task_reset", "cdecl")
    lv_task_reset.argtypes = [POINTER(lv_task_t)]
    lv_task_reset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 160
for _lib in _libs.values():
    if not _lib.has("lv_task_enable", "cdecl"):
        continue
    lv_task_enable = _lib.get("lv_task_enable", "cdecl")
    lv_task_enable.argtypes = [c_bool]
    lv_task_enable.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 166
for _lib in _libs.values():
    if not _lib.has("lv_task_get_idle", "cdecl"):
        continue
    lv_task_get_idle = _lib.get("lv_task_get_idle", "cdecl")
    lv_task_get_idle.argtypes = []
    lv_task_get_idle.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 173
for _lib in _libs.values():
    if not _lib.has("lv_task_get_next", "cdecl"):
        continue
    lv_task_get_next = _lib.get("lv_task_get_next", "cdecl")
    lv_task_get_next.argtypes = [POINTER(lv_task_t)]
    lv_task_get_next.restype = POINTER(lv_task_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 52
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'i',
    'f',
]
struct_anon_8._fields_ = [
    ('i', c_uint16),
    ('f', c_uint16),
]

lv_sqrt_res_t = struct_anon_8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 52

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 64
for _lib in _libs.values():
    if not _lib.has("_lv_trigo_sin", "cdecl"):
        continue
    _lv_trigo_sin = _lib.get("_lv_trigo_sin", "cdecl")
    _lv_trigo_sin.argtypes = [c_int16]
    _lv_trigo_sin.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 77
for _lib in _libs.values():
    if not _lib.has("_lv_bezier3", "cdecl"):
        continue
    _lv_bezier3 = _lib.get("_lv_bezier3", "cdecl")
    _lv_bezier3.argtypes = [c_uint32, c_uint32, c_uint32, c_uint32, c_uint32]
    _lv_bezier3.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 85
for _lib in _libs.values():
    if not _lib.has("_lv_atan2", "cdecl"):
        continue
    _lv_atan2 = _lib.get("_lv_atan2", "cdecl")
    _lv_atan2.argtypes = [c_int, c_int]
    _lv_atan2.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 99
for _lib in _libs.values():
    if not _lib.has("_lv_sqrt", "cdecl"):
        continue
    _lv_sqrt = _lib.get("_lv_sqrt", "cdecl")
    _lv_sqrt.argtypes = [c_uint32, POINTER(lv_sqrt_res_t), c_uint32]
    _lv_sqrt.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 109
for _lib in _libs.values():
    if not _lib.has("_lv_pow", "cdecl"):
        continue
    _lv_pow = _lib.get("_lv_pow", "cdecl")
    _lv_pow.argtypes = [c_int64, c_int8]
    _lv_pow.restype = c_int64
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 120
for _lib in _libs.values():
    if not _lib.has("_lv_map", "cdecl"):
        continue
    _lv_map = _lib.get("_lv_map", "cdecl")
    _lv_map.argtypes = [c_int32, c_int32, c_int32, c_int32, c_int32]
    _lv_map.restype = c_int32
    break

lv_async_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(None))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_async.h: 31

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_async.h: 45
for _lib in _libs.values():
    if not _lib.has("lv_async_call", "cdecl"):
        continue
    lv_async_call = _lib.get("lv_async_call", "cdecl")
    lv_async_call.argtypes = [lv_async_cb_t, POINTER(None)]
    lv_async_call.restype = lv_res_t
    break

enum_anon_9 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_TRANSP = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_0 = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_10 = 25# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_20 = 51# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_30 = 76# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_40 = 102# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_50 = 127# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_60 = 153# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_70 = 178# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_80 = 204# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_90 = 229# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_100 = 255# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

LV_OPA_COVER = 255# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 59

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 213
class union_anon_10(Union):
    pass

union_anon_10.__slots__ = [
    'blue',
    'green',
    'red',
]
union_anon_10._fields_ = [
    ('blue', c_uint8, 1),
    ('green', c_uint8, 1),
    ('red', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 218
class union_anon_11(Union):
    pass

union_anon_11.__slots__ = [
    'full',
    'ch',
]
union_anon_11._fields_ = [
    ('full', c_uint8),
    ('ch', union_anon_10),
]

lv_color1_t = union_anon_11# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 218

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 221
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'blue',
    'green',
    'red',
]
struct_anon_12._fields_ = [
    ('blue', c_uint8, 2),
    ('green', c_uint8, 3),
    ('red', c_uint8, 3),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 227
class union_anon_13(Union):
    pass

union_anon_13.__slots__ = [
    'ch',
    'full',
]
union_anon_13._fields_ = [
    ('ch', struct_anon_12),
    ('full', c_uint8),
]

lv_color8_t = union_anon_13# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 227

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 230
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'blue',
    'green',
    'red',
]
struct_anon_14._fields_ = [
    ('blue', c_uint16, 5),
    ('green', c_uint16, 6),
    ('red', c_uint16, 5),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 243
class union_anon_15(Union):
    pass

union_anon_15.__slots__ = [
    'ch',
    'full',
]
union_anon_15._fields_ = [
    ('ch', struct_anon_14),
    ('full', c_uint16),
]

lv_color16_t = union_anon_15# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 243

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 246
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'blue',
    'green',
    'red',
    'alpha',
]
struct_anon_16._fields_ = [
    ('blue', c_uint8),
    ('green', c_uint8),
    ('red', c_uint8),
    ('alpha', c_uint8),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 253
class union_anon_17(Union):
    pass

union_anon_17.__slots__ = [
    'ch',
    'full',
]
union_anon_17._fields_ = [
    ('ch', struct_anon_16),
    ('full', c_uint32),
]

lv_color32_t = union_anon_17# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 253

lv_color_int_t = c_uint32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 272

lv_color_t = lv_color32_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 273

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 283
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'h',
    's',
    'v',
]
struct_anon_18._fields_ = [
    ('h', c_uint16),
    ('s', c_uint8),
    ('v', c_uint8),
]

lv_color_hsv_t = struct_anon_18# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 283

lv_opa_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 287

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 351
for _lib in _libs.values():
    try:
        ret = (lv_color8_t).in_dll(_lib, "ret")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 375
for _lib in _libs.values():
    try:
        ret = (lv_color16_t).in_dll(_lib, "ret")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 449
for _lib in _libs.values():
    try:
        ret = (lv_color_t).in_dll(_lib, "ret")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 494
for _lib in _libs.values():
    try:
        ret = (lv_color_t).in_dll(_lib, "ret")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 584
for _lib in _libs.values():
    try:
        c32 = (lv_color32_t).in_dll(_lib, "c32")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 651
for _lib in _libs.values():
    if not _lib.has("lv_color_fill", "cdecl"):
        continue
    lv_color_fill = _lib.get("lv_color_fill", "cdecl")
    lv_color_fill.argtypes = [POINTER(lv_color_t), lv_color_t, c_uint32]
    lv_color_fill.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 654
for _lib in _libs.values():
    if not _lib.has("lv_color_lighten", "cdecl"):
        continue
    lv_color_lighten = _lib.get("lv_color_lighten", "cdecl")
    lv_color_lighten.argtypes = [lv_color_t, lv_opa_t]
    lv_color_lighten.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 656
for _lib in _libs.values():
    if not _lib.has("lv_color_darken", "cdecl"):
        continue
    lv_color_darken = _lib.get("lv_color_darken", "cdecl")
    lv_color_darken.argtypes = [lv_color_t, lv_opa_t]
    lv_color_darken.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 665
for _lib in _libs.values():
    if not _lib.has("lv_color_hsv_to_rgb", "cdecl"):
        continue
    lv_color_hsv_to_rgb = _lib.get("lv_color_hsv_to_rgb", "cdecl")
    lv_color_hsv_to_rgb.argtypes = [c_uint16, c_uint8, c_uint8]
    lv_color_hsv_to_rgb.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 674
for _lib in _libs.values():
    if not _lib.has("lv_color_rgb_to_hsv", "cdecl"):
        continue
    lv_color_rgb_to_hsv = _lib.get("lv_color_rgb_to_hsv", "cdecl")
    lv_color_rgb_to_hsv.argtypes = [c_uint8, c_uint8, c_uint8]
    lv_color_rgb_to_hsv.restype = lv_color_hsv_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 681
for _lib in _libs.values():
    if not _lib.has("lv_color_to_hsv", "cdecl"):
        continue
    lv_color_to_hsv = _lib.get("lv_color_to_hsv", "cdecl")
    lv_color_to_hsv.argtypes = [lv_color_t]
    lv_color_to_hsv.restype = lv_color_hsv_t
    break

# /usr/include/string.h: 47
for _lib in _libs.values():
    if not _lib.has("memmove", "cdecl"):
        continue
    memmove = _lib.get("memmove", "cdecl")
    memmove.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memmove.restype = POINTER(c_ubyte)
    memmove.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/string.h: 61
for _lib in _libs.values():
    if not _lib.has("memset", "cdecl"):
        continue
    memset = _lib.get("memset", "cdecl")
    memset.argtypes = [POINTER(None), c_int, c_size_t]
    memset.restype = POINTER(c_ubyte)
    memset.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/string.h: 64
for _lib in _libs.values():
    if not _lib.has("memcmp", "cdecl"):
        continue
    memcmp = _lib.get("memcmp", "cdecl")
    memcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    memcmp.restype = c_int
    break

# /usr/include/string.h: 91
for _lib in _libs.values():
    if not _lib.has("memchr", "cdecl"):
        continue
    memchr = _lib.get("memchr", "cdecl")
    memchr.argtypes = [POINTER(None), c_int, c_size_t]
    memchr.restype = POINTER(c_ubyte)
    memchr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /usr/include/string.h: 140
for _lib in _libs.values():
    if not _lib.has("strcmp", "cdecl"):
        continue
    strcmp = _lib.get("strcmp", "cdecl")
    strcmp.argtypes = [String, String]
    strcmp.restype = c_int
    break

# /usr/include/string.h: 143
for _lib in _libs.values():
    if not _lib.has("strncmp", "cdecl"):
        continue
    strncmp = _lib.get("strncmp", "cdecl")
    strncmp.argtypes = [String, String, c_size_t]
    strncmp.restype = c_int
    break

# /usr/include/string.h: 147
for _lib in _libs.values():
    if not _lib.has("strcoll", "cdecl"):
        continue
    strcoll = _lib.get("strcoll", "cdecl")
    strcoll.argtypes = [String, String]
    strcoll.restype = c_int
    break

# /usr/include/bits/types/__locale_t.h: 31
class struct___locale_data(Structure):
    pass

# /usr/include/bits/types/__locale_t.h: 28
class struct___locale_struct(Structure):
    pass

struct___locale_struct.__slots__ = [
    '__locales',
    '__ctype_b',
    '__ctype_tolower',
    '__ctype_toupper',
    '__names',
]
struct___locale_struct._fields_ = [
    ('__locales', POINTER(struct___locale_data) * int(13)),
    ('__ctype_b', POINTER(c_uint)),
    ('__ctype_tolower', POINTER(c_int)),
    ('__ctype_toupper', POINTER(c_int)),
    ('__names', POINTER(c_char) * int(13)),
]

__locale_t = POINTER(struct___locale_struct)# /usr/include/bits/types/__locale_t.h: 42

locale_t = __locale_t# /usr/include/bits/types/locale_t.h: 24

# /usr/include/string.h: 159
for _lib in _libs.values():
    if not _lib.has("strcoll_l", "cdecl"):
        continue
    strcoll_l = _lib.get("strcoll_l", "cdecl")
    strcoll_l.argtypes = [String, String, locale_t]
    strcoll_l.restype = c_int
    break

# /usr/include/string.h: 163
for _lib in _libs.values():
    if not _lib.has("strxfrm_l", "cdecl"):
        continue
    strxfrm_l = _lib.get("strxfrm_l", "cdecl")
    strxfrm_l.argtypes = [String, String, c_size_t, locale_t]
    strxfrm_l.restype = c_size_t
    break

# /usr/include/string.h: 171
for _lib in _libs.values():
    if not _lib.has("strdup", "cdecl"):
        continue
    strdup = _lib.get("strdup", "cdecl")
    strdup.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        strdup.restype = ReturnString
    else:
        strdup.restype = String
        strdup.errcheck = ReturnString
    break

# /usr/include/string.h: 179
for _lib in _libs.values():
    if not _lib.has("strndup", "cdecl"):
        continue
    strndup = _lib.get("strndup", "cdecl")
    strndup.argtypes = [String, c_size_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strndup.restype = ReturnString
    else:
        strndup.restype = String
        strndup.errcheck = ReturnString
    break

# /usr/include/string.h: 230
for _lib in _libs.values():
    if not _lib.has("strchr", "cdecl"):
        continue
    strchr = _lib.get("strchr", "cdecl")
    strchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strchr.restype = ReturnString
    else:
        strchr.restype = String
        strchr.errcheck = ReturnString
    break

# /usr/include/string.h: 257
for _lib in _libs.values():
    if not _lib.has("strrchr", "cdecl"):
        continue
    strrchr = _lib.get("strrchr", "cdecl")
    strrchr.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strrchr.restype = ReturnString
    else:
        strrchr.restype = String
        strrchr.errcheck = ReturnString
    break

# /usr/include/string.h: 277
for _lib in _libs.values():
    if not _lib.has("strcspn", "cdecl"):
        continue
    strcspn = _lib.get("strcspn", "cdecl")
    strcspn.argtypes = [String, String]
    strcspn.restype = c_size_t
    break

# /usr/include/string.h: 281
for _lib in _libs.values():
    if not _lib.has("strspn", "cdecl"):
        continue
    strspn = _lib.get("strspn", "cdecl")
    strspn.argtypes = [String, String]
    strspn.restype = c_size_t
    break

# /usr/include/string.h: 307
for _lib in _libs.values():
    if not _lib.has("strpbrk", "cdecl"):
        continue
    strpbrk = _lib.get("strpbrk", "cdecl")
    strpbrk.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strpbrk.restype = ReturnString
    else:
        strpbrk.restype = String
        strpbrk.errcheck = ReturnString
    break

# /usr/include/string.h: 334
for _lib in _libs.values():
    if not _lib.has("strstr", "cdecl"):
        continue
    strstr = _lib.get("strstr", "cdecl")
    strstr.argtypes = [String, String]
    if sizeof(c_int) == sizeof(c_void_p):
        strstr.restype = ReturnString
    else:
        strstr.restype = String
        strstr.errcheck = ReturnString
    break

# /usr/include/string.h: 391
for _lib in _libs.values():
    if not _lib.has("strlen", "cdecl"):
        continue
    strlen = _lib.get("strlen", "cdecl")
    strlen.argtypes = [String]
    strlen.restype = c_size_t
    break

# /usr/include/string.h: 397
for _lib in _libs.values():
    if not _lib.has("strnlen", "cdecl"):
        continue
    strnlen = _lib.get("strnlen", "cdecl")
    strnlen.argtypes = [String, c_size_t]
    strnlen.restype = c_size_t
    break

# /usr/include/string.h: 403
for _lib in _libs.values():
    if not _lib.has("strerror", "cdecl"):
        continue
    strerror = _lib.get("strerror", "cdecl")
    strerror.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strerror.restype = ReturnString
    else:
        strerror.restype = String
        strerror.errcheck = ReturnString
    break

# /usr/include/string.h: 421
for _lib in _libs.values():
    if not _lib.has("__xpg_strerror_r", "cdecl"):
        continue
    __xpg_strerror_r = _lib.get("__xpg_strerror_r", "cdecl")
    __xpg_strerror_r.argtypes = [c_int, String, c_size_t]
    __xpg_strerror_r.restype = c_int
    break

# /usr/include/string.h: 442
for _lib in _libs.values():
    if not _lib.has("strerror_l", "cdecl"):
        continue
    strerror_l = _lib.get("strerror_l", "cdecl")
    strerror_l.argtypes = [c_int, locale_t]
    if sizeof(c_int) == sizeof(c_void_p):
        strerror_l.restype = ReturnString
    else:
        strerror_l.restype = String
        strerror_l.errcheck = ReturnString
    break

# /usr/include/strings.h: 34
for _lib in _libs.values():
    if not _lib.has("bcmp", "cdecl"):
        continue
    bcmp = _lib.get("bcmp", "cdecl")
    bcmp.argtypes = [POINTER(None), POINTER(None), c_size_t]
    bcmp.restype = c_int
    break

# /usr/include/strings.h: 38
for _lib in _libs.values():
    if not _lib.has("bcopy", "cdecl"):
        continue
    bcopy = _lib.get("bcopy", "cdecl")
    bcopy.argtypes = [POINTER(None), POINTER(None), c_size_t]
    bcopy.restype = None
    break

# /usr/include/strings.h: 42
for _lib in _libs.values():
    if not _lib.has("bzero", "cdecl"):
        continue
    bzero = _lib.get("bzero", "cdecl")
    bzero.argtypes = [POINTER(None), c_size_t]
    bzero.restype = None
    break

# /usr/include/strings.h: 68
for _lib in _libs.values():
    if not _lib.has("index", "cdecl"):
        continue
    index = _lib.get("index", "cdecl")
    index.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        index.restype = ReturnString
    else:
        index.restype = String
        index.errcheck = ReturnString
    break

# /usr/include/strings.h: 96
for _lib in _libs.values():
    if not _lib.has("rindex", "cdecl"):
        continue
    rindex = _lib.get("rindex", "cdecl")
    rindex.argtypes = [String, c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        rindex.restype = ReturnString
    else:
        rindex.restype = String
        rindex.errcheck = ReturnString
    break

# /usr/include/strings.h: 104
for _lib in _libs.values():
    if not _lib.has("ffs", "cdecl"):
        continue
    ffs = _lib.get("ffs", "cdecl")
    ffs.argtypes = [c_int]
    ffs.restype = c_int
    break

# /usr/include/strings.h: 110
for _lib in _libs.values():
    if not _lib.has("ffsl", "cdecl"):
        continue
    ffsl = _lib.get("ffsl", "cdecl")
    ffsl.argtypes = [c_long]
    ffsl.restype = c_int
    break

# /usr/include/strings.h: 111
for _lib in _libs.values():
    if not _lib.has("ffsll", "cdecl"):
        continue
    ffsll = _lib.get("ffsll", "cdecl")
    ffsll.argtypes = [c_longlong]
    ffsll.restype = c_int
    break

# /usr/include/strings.h: 116
for _lib in _libs.values():
    if not _lib.has("strcasecmp", "cdecl"):
        continue
    strcasecmp = _lib.get("strcasecmp", "cdecl")
    strcasecmp.argtypes = [String, String]
    strcasecmp.restype = c_int
    break

# /usr/include/strings.h: 120
for _lib in _libs.values():
    if not _lib.has("strncasecmp", "cdecl"):
        continue
    strncasecmp = _lib.get("strncasecmp", "cdecl")
    strncasecmp.argtypes = [String, String, c_size_t]
    strncasecmp.restype = c_int
    break

# /usr/include/strings.h: 128
for _lib in _libs.values():
    if not _lib.has("strcasecmp_l", "cdecl"):
        continue
    strcasecmp_l = _lib.get("strcasecmp_l", "cdecl")
    strcasecmp_l.argtypes = [String, String, locale_t]
    strcasecmp_l.restype = c_int
    break

# /usr/include/strings.h: 133
for _lib in _libs.values():
    if not _lib.has("strncasecmp_l", "cdecl"):
        continue
    strncasecmp_l = _lib.get("strncasecmp_l", "cdecl")
    strncasecmp_l.argtypes = [String, String, c_size_t, locale_t]
    strncasecmp_l.restype = c_int
    break

# /usr/include/string.h: 450
for _lib in _libs.values():
    if not _lib.has("explicit_bzero", "cdecl"):
        continue
    explicit_bzero = _lib.get("explicit_bzero", "cdecl")
    explicit_bzero.argtypes = [POINTER(None), c_size_t]
    explicit_bzero.restype = None
    break

# /usr/include/string.h: 462
for _lib in _libs.values():
    if not _lib.has("strsignal", "cdecl"):
        continue
    strsignal = _lib.get("strsignal", "cdecl")
    strsignal.argtypes = [c_int]
    if sizeof(c_int) == sizeof(c_void_p):
        strsignal.restype = ReturnString
    else:
        strsignal.restype = String
        strsignal.errcheck = ReturnString
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 42
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'x',
    'y',
]
struct_anon_19._fields_ = [
    ('x', lv_coord_t),
    ('y', lv_coord_t),
]

lv_point_t = struct_anon_19# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 42

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 50
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'x1',
    'y1',
    'x2',
    'y2',
]
struct_anon_20._fields_ = [
    ('x1', lv_coord_t),
    ('y1', lv_coord_t),
    ('x2', lv_coord_t),
    ('y2', lv_coord_t),
]

lv_area_t = struct_anon_20# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 50

enum_anon_21 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_CENTER = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_TOP_LEFT = (LV_ALIGN_CENTER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_TOP_MID = (LV_ALIGN_IN_TOP_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_TOP_RIGHT = (LV_ALIGN_IN_TOP_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_BOTTOM_LEFT = (LV_ALIGN_IN_TOP_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_BOTTOM_MID = (LV_ALIGN_IN_BOTTOM_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_BOTTOM_RIGHT = (LV_ALIGN_IN_BOTTOM_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_LEFT_MID = (LV_ALIGN_IN_BOTTOM_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_IN_RIGHT_MID = (LV_ALIGN_IN_LEFT_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_TOP_LEFT = (LV_ALIGN_IN_RIGHT_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_TOP_MID = (LV_ALIGN_OUT_TOP_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_TOP_RIGHT = (LV_ALIGN_OUT_TOP_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_BOTTOM_LEFT = (LV_ALIGN_OUT_TOP_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_BOTTOM_MID = (LV_ALIGN_OUT_BOTTOM_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_BOTTOM_RIGHT = (LV_ALIGN_OUT_BOTTOM_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_LEFT_TOP = (LV_ALIGN_OUT_BOTTOM_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_LEFT_MID = (LV_ALIGN_OUT_LEFT_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_LEFT_BOTTOM = (LV_ALIGN_OUT_LEFT_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_RIGHT_TOP = (LV_ALIGN_OUT_LEFT_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_RIGHT_MID = (LV_ALIGN_OUT_RIGHT_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

LV_ALIGN_OUT_RIGHT_BOTTOM = (LV_ALIGN_OUT_RIGHT_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 53

lv_align_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 76

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 90
for _lib in _libs.values():
    if not _lib.has("lv_area_set", "cdecl"):
        continue
    lv_area_set = _lib.get("lv_area_set", "cdecl")
    lv_area_set.argtypes = [POINTER(lv_area_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t]
    lv_area_set.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_area_set_width", "cdecl"):
        continue
    lv_area_set_width = _lib.get("lv_area_set_width", "cdecl")
    lv_area_set_width.argtypes = [POINTER(lv_area_t), lv_coord_t]
    lv_area_set_width.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_area_set_height", "cdecl"):
        continue
    lv_area_set_height = _lib.get("lv_area_set_height", "cdecl")
    lv_area_set_height.argtypes = [POINTER(lv_area_t), lv_coord_t]
    lv_area_set_height.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 142
for _lib in _libs.values():
    if not _lib.has("_lv_area_set_pos", "cdecl"):
        continue
    _lv_area_set_pos = _lib.get("_lv_area_set_pos", "cdecl")
    _lv_area_set_pos.argtypes = [POINTER(lv_area_t), lv_coord_t, lv_coord_t]
    _lv_area_set_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 149
for _lib in _libs.values():
    if not _lib.has("lv_area_get_size", "cdecl"):
        continue
    lv_area_get_size = _lib.get("lv_area_get_size", "cdecl")
    lv_area_get_size.argtypes = [POINTER(lv_area_t)]
    lv_area_get_size.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 158
for _lib in _libs.values():
    if not _lib.has("_lv_area_intersect", "cdecl"):
        continue
    _lv_area_intersect = _lib.get("_lv_area_intersect", "cdecl")
    _lv_area_intersect.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(lv_area_t)]
    _lv_area_intersect.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 166
for _lib in _libs.values():
    if not _lib.has("_lv_area_join", "cdecl"):
        continue
    _lv_area_join = _lib.get("_lv_area_join", "cdecl")
    _lv_area_join.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(lv_area_t)]
    _lv_area_join.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 175
for _lib in _libs.values():
    if not _lib.has("_lv_area_is_point_on", "cdecl"):
        continue
    _lv_area_is_point_on = _lib.get("_lv_area_is_point_on", "cdecl")
    _lv_area_is_point_on.argtypes = [POINTER(lv_area_t), POINTER(lv_point_t), lv_coord_t]
    _lv_area_is_point_on.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 183
for _lib in _libs.values():
    if not _lib.has("_lv_area_is_on", "cdecl"):
        continue
    _lv_area_is_on = _lib.get("_lv_area_is_on", "cdecl")
    _lv_area_is_on.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t)]
    _lv_area_is_on.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 192
for _lib in _libs.values():
    if not _lib.has("_lv_area_is_in", "cdecl"):
        continue
    _lv_area_is_in = _lib.get("_lv_area_is_in", "cdecl")
    _lv_area_is_in.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), lv_coord_t]
    _lv_area_is_in.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 201
for _lib in _libs.values():
    if not _lib.has("_lv_area_align", "cdecl"):
        continue
    _lv_area_align = _lib.get("_lv_area_align", "cdecl")
    _lv_area_align.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), lv_align_t, POINTER(lv_point_t)]
    _lv_area_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 147
class struct__disp_t(Structure):
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 66
class struct__disp_drv_t(Structure):
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 61
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'buf1',
    'buf2',
    'buf_act',
    'size',
    'area',
    'flushing',
    'flushing_last',
    'last_area',
    'last_part',
]
struct_anon_22._fields_ = [
    ('buf1', POINTER(None)),
    ('buf2', POINTER(None)),
    ('buf_act', POINTER(None)),
    ('size', c_uint32),
    ('area', lv_area_t),
    ('flushing', c_int),
    ('flushing_last', c_int),
    ('last_area', c_uint32, 1),
    ('last_part', c_uint32, 1),
]

lv_disp_buf_t = struct_anon_22# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 61

struct__disp_drv_t.__slots__ = [
    'hor_res',
    'ver_res',
    'buffer',
    'antialiasing',
    'rotated',
    'dpi',
    'flush_cb',
    'rounder_cb',
    'set_px_cb',
    'monitor_cb',
    'wait_cb',
    'clean_dcache_cb',
    'gpu_wait_cb',
    'gpu_blend_cb',
    'gpu_fill_cb',
    'color_chroma_key',
]
struct__disp_drv_t._fields_ = [
    ('hor_res', lv_coord_t),
    ('ver_res', lv_coord_t),
    ('buffer', POINTER(lv_disp_buf_t)),
    ('antialiasing', c_uint32, 1),
    ('rotated', c_uint32, 1),
    ('dpi', c_uint32, 10),
    ('flush_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), POINTER(lv_area_t), POINTER(lv_color_t))),
    ('rounder_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), POINTER(lv_area_t))),
    ('set_px_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), POINTER(c_uint8), lv_coord_t, lv_coord_t, lv_coord_t, lv_color_t, lv_opa_t)),
    ('monitor_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), c_uint32, c_uint32)),
    ('wait_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t))),
    ('clean_dcache_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t))),
    ('gpu_wait_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t))),
    ('gpu_blend_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), POINTER(lv_color_t), POINTER(lv_color_t), c_uint32, lv_opa_t)),
    ('gpu_fill_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__disp_drv_t), POINTER(lv_color_t), lv_coord_t, POINTER(lv_area_t), lv_color_t)),
    ('color_chroma_key', lv_color_t),
]

lv_disp_drv_t = struct__disp_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 139

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 195
class struct__lv_obj_t(Structure):
    pass

struct__disp_t.__slots__ = [
    'driver',
    'refr_task',
    'scr_ll',
    'act_scr',
    'prev_scr',
    'scr_to_load',
    'top_layer',
    'sys_layer',
    'del_prev',
    'bg_color',
    'bg_img',
    'bg_opa',
    'inv_areas',
    'inv_area_joined',
    'inv_p',
    'last_activity_time',
]
struct__disp_t._fields_ = [
    ('driver', lv_disp_drv_t),
    ('refr_task', POINTER(lv_task_t)),
    ('scr_ll', lv_ll_t),
    ('act_scr', POINTER(struct__lv_obj_t)),
    ('prev_scr', POINTER(struct__lv_obj_t)),
    ('scr_to_load', POINTER(struct__lv_obj_t)),
    ('top_layer', POINTER(struct__lv_obj_t)),
    ('sys_layer', POINTER(struct__lv_obj_t)),
    ('del_prev', c_uint8, 1),
    ('bg_color', lv_color_t),
    ('bg_img', POINTER(None)),
    ('bg_opa', lv_opa_t),
    ('inv_areas', lv_area_t * int(32)),
    ('inv_area_joined', c_uint8 * int(32)),
    ('inv_p', c_uint32, 10),
    ('last_activity_time', c_uint32),
]

lv_disp_t = struct__disp_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 178

enum_anon_23 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

LV_DISP_SIZE_SMALL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

LV_DISP_SIZE_MEDIUM = (LV_DISP_SIZE_SMALL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

LV_DISP_SIZE_LARGE = (LV_DISP_SIZE_MEDIUM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

LV_DISP_SIZE_EXTRA_LARGE = (LV_DISP_SIZE_LARGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

lv_disp_size_t = enum_anon_23# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 185

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 197
for _lib in _libs.values():
    if not _lib.has("lv_disp_drv_init", "cdecl"):
        continue
    lv_disp_drv_init = _lib.get("lv_disp_drv_init", "cdecl")
    lv_disp_drv_init.argtypes = [POINTER(lv_disp_drv_t)]
    lv_disp_drv_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 214
for _lib in _libs.values():
    if not _lib.has("lv_disp_buf_init", "cdecl"):
        continue
    lv_disp_buf_init = _lib.get("lv_disp_buf_init", "cdecl")
    lv_disp_buf_init.argtypes = [POINTER(lv_disp_buf_t), POINTER(None), POINTER(None), c_uint32]
    lv_disp_buf_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 222
for _lib in _libs.values():
    if not _lib.has("lv_disp_drv_register", "cdecl"):
        continue
    lv_disp_drv_register = _lib.get("lv_disp_drv_register", "cdecl")
    lv_disp_drv_register.argtypes = [POINTER(lv_disp_drv_t)]
    lv_disp_drv_register.restype = POINTER(lv_disp_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_disp_drv_update", "cdecl"):
        continue
    lv_disp_drv_update = _lib.get("lv_disp_drv_update", "cdecl")
    lv_disp_drv_update.argtypes = [POINTER(lv_disp_t), POINTER(lv_disp_drv_t)]
    lv_disp_drv_update.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 235
for _lib in _libs.values():
    if not _lib.has("lv_disp_remove", "cdecl"):
        continue
    lv_disp_remove = _lib.get("lv_disp_remove", "cdecl")
    lv_disp_remove.argtypes = [POINTER(lv_disp_t)]
    lv_disp_remove.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 241
for _lib in _libs.values():
    if not _lib.has("lv_disp_set_default", "cdecl"):
        continue
    lv_disp_set_default = _lib.get("lv_disp_set_default", "cdecl")
    lv_disp_set_default.argtypes = [POINTER(lv_disp_t)]
    lv_disp_set_default.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 247
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_default", "cdecl"):
        continue
    lv_disp_get_default = _lib.get("lv_disp_get_default", "cdecl")
    lv_disp_get_default.argtypes = []
    lv_disp_get_default.restype = POINTER(lv_disp_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 254
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_hor_res", "cdecl"):
        continue
    lv_disp_get_hor_res = _lib.get("lv_disp_get_hor_res", "cdecl")
    lv_disp_get_hor_res.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_hor_res.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 261
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_ver_res", "cdecl"):
        continue
    lv_disp_get_ver_res = _lib.get("lv_disp_get_ver_res", "cdecl")
    lv_disp_get_ver_res.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_ver_res.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 268
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_antialiasing", "cdecl"):
        continue
    lv_disp_get_antialiasing = _lib.get("lv_disp_get_antialiasing", "cdecl")
    lv_disp_get_antialiasing.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_antialiasing.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 275
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_dpi", "cdecl"):
        continue
    lv_disp_get_dpi = _lib.get("lv_disp_get_dpi", "cdecl")
    lv_disp_get_dpi.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_dpi.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 282
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_size_category", "cdecl"):
        continue
    lv_disp_get_size_category = _lib.get("lv_disp_get_size_category", "cdecl")
    lv_disp_get_size_category.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_size_category.restype = lv_disp_size_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 290
for _lib in _libs.values():
    if not _lib.has("lv_disp_flush_ready", "cdecl"):
        continue
    lv_disp_flush_ready = _lib.get("lv_disp_flush_ready", "cdecl")
    lv_disp_flush_ready.argtypes = [POINTER(lv_disp_drv_t)]
    lv_disp_flush_ready.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 298
for _lib in _libs.values():
    if not _lib.has("lv_disp_flush_is_last", "cdecl"):
        continue
    lv_disp_flush_is_last = _lib.get("lv_disp_flush_is_last", "cdecl")
    lv_disp_flush_is_last.argtypes = [POINTER(lv_disp_drv_t)]
    lv_disp_flush_is_last.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 307
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_next", "cdecl"):
        continue
    lv_disp_get_next = _lib.get("lv_disp_get_next", "cdecl")
    lv_disp_get_next.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_next.restype = POINTER(lv_disp_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 314
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_buf", "cdecl"):
        continue
    lv_disp_get_buf = _lib.get("lv_disp_get_buf", "cdecl")
    lv_disp_get_buf.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_buf.restype = POINTER(lv_disp_buf_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 320
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_inv_buf_size", "cdecl"):
        continue
    lv_disp_get_inv_buf_size = _lib.get("lv_disp_get_inv_buf_size", "cdecl")
    lv_disp_get_inv_buf_size.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_inv_buf_size.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 326
for _lib in _libs.values():
    if not _lib.has("_lv_disp_pop_from_inv_buf", "cdecl"):
        continue
    _lv_disp_pop_from_inv_buf = _lib.get("_lv_disp_pop_from_inv_buf", "cdecl")
    _lv_disp_pop_from_inv_buf.argtypes = [POINTER(lv_disp_t), c_uint16]
    _lv_disp_pop_from_inv_buf.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 333
for _lib in _libs.values():
    if not _lib.has("lv_disp_is_double_buf", "cdecl"):
        continue
    lv_disp_is_double_buf = _lib.get("lv_disp_is_double_buf", "cdecl")
    lv_disp_is_double_buf.argtypes = [POINTER(lv_disp_t)]
    lv_disp_is_double_buf.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 341
for _lib in _libs.values():
    if not _lib.has("lv_disp_is_true_double_buf", "cdecl"):
        continue
    lv_disp_is_true_double_buf = _lib.get("lv_disp_is_true_double_buf", "cdecl")
    lv_disp_is_true_double_buf.argtypes = [POINTER(lv_disp_t)]
    lv_disp_is_true_double_buf.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 172
class struct__lv_indev_t(Structure):
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 81
class struct__lv_indev_drv_t(Structure):
    pass

enum_anon_24 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

LV_INDEV_TYPE_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

LV_INDEV_TYPE_POINTER = (LV_INDEV_TYPE_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

LV_INDEV_TYPE_KEYPAD = (LV_INDEV_TYPE_POINTER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

LV_INDEV_TYPE_BUTTON = (LV_INDEV_TYPE_KEYPAD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

LV_INDEV_TYPE_ENCODER = (LV_INDEV_TYPE_BUTTON + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 39

lv_indev_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 47

enum_anon_25 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 50

LV_INDEV_STATE_REL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 50

LV_INDEV_STATE_PR = (LV_INDEV_STATE_REL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 50

lv_indev_state_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 51

enum_anon_26 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 53

LV_DRAG_DIR_HOR = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 53

LV_DRAG_DIR_VER = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 53

LV_DRAG_DIR_BOTH = 3# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 53

LV_DRAG_DIR_ONE = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 53

lv_drag_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 60

enum_anon_27 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 62

LV_GESTURE_DIR_TOP = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 62

LV_GESTURE_DIR_BOTTOM = (LV_GESTURE_DIR_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 62

LV_GESTURE_DIR_LEFT = (LV_GESTURE_DIR_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 62

LV_GESTURE_DIR_RIGHT = (LV_GESTURE_DIR_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 62

lv_gesture_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 68

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 78
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'point',
    'key',
    'btn_id',
    'enc_diff',
    'state',
]
struct_anon_28._fields_ = [
    ('point', lv_point_t),
    ('key', c_uint32),
    ('btn_id', c_uint32),
    ('enc_diff', c_int16),
    ('state', lv_indev_state_t),
]

lv_indev_data_t = struct_anon_28# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 78

struct__lv_indev_drv_t.__slots__ = [
    'type',
    'read_cb',
    'feedback_cb',
    'disp',
    'read_task',
    'drag_limit',
    'drag_throw',
    'gesture_min_velocity',
    'gesture_limit',
    'long_press_time',
    'long_press_rep_time',
]
struct__lv_indev_drv_t._fields_ = [
    ('type', lv_indev_type_t),
    ('read_cb', CFUNCTYPE(UNCHECKED(c_bool), POINTER(struct__lv_indev_drv_t), POINTER(lv_indev_data_t))),
    ('feedback_cb', CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_indev_drv_t), c_uint8)),
    ('disp', POINTER(struct__disp_t)),
    ('read_task', POINTER(lv_task_t)),
    ('drag_limit', c_uint8),
    ('drag_throw', c_uint8),
    ('gesture_min_velocity', c_uint8),
    ('gesture_limit', c_uint8),
    ('long_press_time', c_uint16),
    ('long_press_rep_time', c_uint16),
]

lv_indev_drv_t = struct__lv_indev_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 122

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 130
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'act_point',
    'last_point',
    'vect',
    'drag_sum',
    'drag_throw_vect',
    'act_obj',
    'last_obj',
    'last_pressed',
    'gesture_dir',
    'gesture_sum',
    'drag_limit_out',
    'drag_in_prog',
    'drag_dir',
    'gesture_sent',
]
struct_anon_29._fields_ = [
    ('act_point', lv_point_t),
    ('last_point', lv_point_t),
    ('vect', lv_point_t),
    ('drag_sum', lv_point_t),
    ('drag_throw_vect', lv_point_t),
    ('act_obj', POINTER(struct__lv_obj_t)),
    ('last_obj', POINTER(struct__lv_obj_t)),
    ('last_pressed', POINTER(struct__lv_obj_t)),
    ('gesture_dir', lv_gesture_dir_t),
    ('gesture_sum', lv_point_t),
    ('drag_limit_out', c_uint8, 1),
    ('drag_in_prog', c_uint8, 1),
    ('drag_dir', lv_drag_dir_t, 3),
    ('gesture_sent', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 150
class struct_anon_30(Structure):
    pass

struct_anon_30.__slots__ = [
    'last_state',
    'last_key',
]
struct_anon_30._fields_ = [
    ('last_state', lv_indev_state_t),
    ('last_key', c_uint32),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 129
class union_anon_31(Union):
    pass

union_anon_31.__slots__ = [
    'pointer',
    'keypad',
]
union_anon_31._fields_ = [
    ('pointer', struct_anon_29),
    ('keypad', struct_anon_30),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 165
class struct__lv_indev_proc_t(Structure):
    pass

struct__lv_indev_proc_t.__slots__ = [
    'state',
    'types',
    'pr_timestamp',
    'longpr_rep_timestamp',
    'long_pr_sent',
    'reset_query',
    'disabled',
    'wait_until_release',
]
struct__lv_indev_proc_t._fields_ = [
    ('state', lv_indev_state_t),
    ('types', union_anon_31),
    ('pr_timestamp', c_uint32),
    ('longpr_rep_timestamp', c_uint32),
    ('long_pr_sent', c_uint8, 1),
    ('reset_query', c_uint8, 1),
    ('disabled', c_uint8, 1),
    ('wait_until_release', c_uint8, 1),
]

lv_indev_proc_t = struct__lv_indev_proc_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 165

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 54
class struct__lv_group_t(Structure):
    pass

struct__lv_indev_t.__slots__ = [
    'driver',
    'proc',
    'cursor',
    'group',
    'btn_points',
]
struct__lv_indev_t._fields_ = [
    ('driver', lv_indev_drv_t),
    ('proc', lv_indev_proc_t),
    ('cursor', POINTER(struct__lv_obj_t)),
    ('group', POINTER(struct__lv_group_t)),
    ('btn_points', POINTER(lv_point_t)),
]

lv_indev_t = struct__lv_indev_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 179

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 191
for _lib in _libs.values():
    if not _lib.has("lv_indev_drv_init", "cdecl"):
        continue
    lv_indev_drv_init = _lib.get("lv_indev_drv_init", "cdecl")
    lv_indev_drv_init.argtypes = [POINTER(lv_indev_drv_t)]
    lv_indev_drv_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 198
for _lib in _libs.values():
    if not _lib.has("lv_indev_drv_register", "cdecl"):
        continue
    lv_indev_drv_register = _lib.get("lv_indev_drv_register", "cdecl")
    lv_indev_drv_register.argtypes = [POINTER(lv_indev_drv_t)]
    lv_indev_drv_register.restype = POINTER(lv_indev_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 205
for _lib in _libs.values():
    if not _lib.has("lv_indev_drv_update", "cdecl"):
        continue
    lv_indev_drv_update = _lib.get("lv_indev_drv_update", "cdecl")
    lv_indev_drv_update.argtypes = [POINTER(lv_indev_t), POINTER(lv_indev_drv_t)]
    lv_indev_drv_update.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 213
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_next", "cdecl"):
        continue
    lv_indev_get_next = _lib.get("lv_indev_get_next", "cdecl")
    lv_indev_get_next.argtypes = [POINTER(lv_indev_t)]
    lv_indev_get_next.restype = POINTER(lv_indev_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 221
for _lib in _libs.values():
    if not _lib.has("_lv_indev_read", "cdecl"):
        continue
    _lv_indev_read = _lib.get("_lv_indev_read", "cdecl")
    _lv_indev_read.argtypes = [POINTER(lv_indev_t), POINTER(lv_indev_data_t)]
    _lv_indev_read.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_tick.h: 42
for _lib in _libs.values():
    if not _lib.has("lv_tick_inc", "cdecl"):
        continue
    lv_tick_inc = _lib.get("lv_tick_inc", "cdecl")
    lv_tick_inc.argtypes = [c_uint32]
    lv_tick_inc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_tick.h: 50
for _lib in _libs.values():
    if not _lib.has("lv_tick_get", "cdecl"):
        continue
    lv_tick_get = _lib.get("lv_tick_get", "cdecl")
    lv_tick_get.argtypes = []
    lv_tick_get.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_tick.h: 57
for _lib in _libs.values():
    if not _lib.has("lv_tick_elaps", "cdecl"):
        continue
    lv_tick_elaps = _lib.get("lv_tick_elaps", "cdecl")
    lv_tick_elaps.argtypes = [c_uint32]
    lv_tick_elaps.restype = c_uint32
    break

enum_anon_32 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_AUDIO = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_VIDEO = (_LV_STR_SYMBOL_AUDIO + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_LIST = (_LV_STR_SYMBOL_VIDEO + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_OK = (_LV_STR_SYMBOL_LIST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_CLOSE = (_LV_STR_SYMBOL_OK + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_POWER = (_LV_STR_SYMBOL_CLOSE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_SETTINGS = (_LV_STR_SYMBOL_POWER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_HOME = (_LV_STR_SYMBOL_SETTINGS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_DOWNLOAD = (_LV_STR_SYMBOL_HOME + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_DRIVE = (_LV_STR_SYMBOL_DOWNLOAD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_REFRESH = (_LV_STR_SYMBOL_DRIVE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_MUTE = (_LV_STR_SYMBOL_REFRESH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_VOLUME_MID = (_LV_STR_SYMBOL_MUTE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_VOLUME_MAX = (_LV_STR_SYMBOL_VOLUME_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_IMAGE = (_LV_STR_SYMBOL_VOLUME_MAX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_EDIT = (_LV_STR_SYMBOL_IMAGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_PREV = (_LV_STR_SYMBOL_EDIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_PLAY = (_LV_STR_SYMBOL_PREV + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_PAUSE = (_LV_STR_SYMBOL_PLAY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_STOP = (_LV_STR_SYMBOL_PAUSE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_NEXT = (_LV_STR_SYMBOL_STOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_EJECT = (_LV_STR_SYMBOL_NEXT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_LEFT = (_LV_STR_SYMBOL_EJECT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_RIGHT = (_LV_STR_SYMBOL_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_PLUS = (_LV_STR_SYMBOL_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_MINUS = (_LV_STR_SYMBOL_PLUS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_EYE_OPEN = (_LV_STR_SYMBOL_MINUS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_EYE_CLOSE = (_LV_STR_SYMBOL_EYE_OPEN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_WARNING = (_LV_STR_SYMBOL_EYE_CLOSE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_SHUFFLE = (_LV_STR_SYMBOL_WARNING + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_UP = (_LV_STR_SYMBOL_SHUFFLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_DOWN = (_LV_STR_SYMBOL_UP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_LOOP = (_LV_STR_SYMBOL_DOWN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_DIRECTORY = (_LV_STR_SYMBOL_LOOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_UPLOAD = (_LV_STR_SYMBOL_DIRECTORY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_CALL = (_LV_STR_SYMBOL_UPLOAD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_CUT = (_LV_STR_SYMBOL_CALL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_COPY = (_LV_STR_SYMBOL_CUT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_SAVE = (_LV_STR_SYMBOL_COPY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_CHARGE = (_LV_STR_SYMBOL_SAVE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_PASTE = (_LV_STR_SYMBOL_CHARGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BELL = (_LV_STR_SYMBOL_PASTE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_KEYBOARD = (_LV_STR_SYMBOL_BELL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_GPS = (_LV_STR_SYMBOL_KEYBOARD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_FILE = (_LV_STR_SYMBOL_GPS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_WIFI = (_LV_STR_SYMBOL_FILE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BATTERY_FULL = (_LV_STR_SYMBOL_WIFI + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BATTERY_3 = (_LV_STR_SYMBOL_BATTERY_FULL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BATTERY_2 = (_LV_STR_SYMBOL_BATTERY_3 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BATTERY_1 = (_LV_STR_SYMBOL_BATTERY_2 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BATTERY_EMPTY = (_LV_STR_SYMBOL_BATTERY_1 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_USB = (_LV_STR_SYMBOL_BATTERY_EMPTY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BLUETOOTH = (_LV_STR_SYMBOL_USB + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_TRASH = (_LV_STR_SYMBOL_BLUETOOTH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_BACKSPACE = (_LV_STR_SYMBOL_TRASH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_SD_CARD = (_LV_STR_SYMBOL_BACKSPACE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_NEW_LINE = (_LV_STR_SYMBOL_SD_CARD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

_LV_STR_SYMBOL_DUMMY = (_LV_STR_SYMBOL_NEW_LINE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 94

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 44
class struct_anon_33(Structure):
    pass

struct_anon_33.__slots__ = [
    'adv_w',
    'box_w',
    'box_h',
    'ofs_x',
    'ofs_y',
    'bpp',
]
struct_anon_33._fields_ = [
    ('adv_w', c_uint16),
    ('box_w', c_uint16),
    ('box_h', c_uint16),
    ('ofs_x', c_int16),
    ('ofs_y', c_int16),
    ('bpp', c_uint8),
]

lv_font_glyph_dsc_t = struct_anon_33# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 44

enum_anon_34 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 47

LV_FONT_SUBPX_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 47

LV_FONT_SUBPX_HOR = (LV_FONT_SUBPX_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 47

LV_FONT_SUBPX_VER = (LV_FONT_SUBPX_HOR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 47

LV_FONT_SUBPX_BOTH = (LV_FONT_SUBPX_VER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 47

lv_font_subpx_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 54

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 57
class struct__lv_font_struct(Structure):
    pass

struct__lv_font_struct.__slots__ = [
    'get_glyph_dsc',
    'get_glyph_bitmap',
    'line_height',
    'base_line',
    'subpx',
    'underline_position',
    'underline_thickness',
    'dsc',
]
struct__lv_font_struct._fields_ = [
    ('get_glyph_dsc', CFUNCTYPE(UNCHECKED(c_bool), POINTER(struct__lv_font_struct), POINTER(lv_font_glyph_dsc_t), c_uint32, c_uint32)),
    ('get_glyph_bitmap', CFUNCTYPE(UNCHECKED(POINTER(c_uint8)), POINTER(struct__lv_font_struct), c_uint32)),
    ('line_height', lv_coord_t),
    ('base_line', lv_coord_t),
    ('subpx', c_uint8, 2),
    ('underline_position', c_int8),
    ('underline_thickness', c_int8),
    ('dsc', POINTER(None)),
]

lv_font_t = struct__lv_font_struct# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 77

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_font_get_glyph_bitmap", "cdecl"):
        continue
    lv_font_get_glyph_bitmap = _lib.get("lv_font_get_glyph_bitmap", "cdecl")
    lv_font_get_glyph_bitmap.argtypes = [POINTER(lv_font_t), c_uint32]
    lv_font_get_glyph_bitmap.restype = POINTER(c_uint8)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 99
for _lib in _libs.values():
    if not _lib.has("lv_font_get_glyph_dsc", "cdecl"):
        continue
    lv_font_get_glyph_dsc = _lib.get("lv_font_get_glyph_dsc", "cdecl")
    lv_font_get_glyph_dsc.argtypes = [POINTER(lv_font_t), POINTER(lv_font_glyph_dsc_t), c_uint32, c_uint32]
    lv_font_get_glyph_dsc.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_font_get_glyph_width", "cdecl"):
        continue
    lv_font_get_glyph_width = _lib.get("lv_font_get_glyph_width", "cdecl")
    lv_font_get_glyph_width.argtypes = [POINTER(lv_font_t), c_uint32, c_uint32]
    lv_font_get_glyph_width.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 140
for _lib in _libs.values():
    try:
        lv_font_montserrat_14 = (lv_font_t).in_dll(_lib, "lv_font_montserrat_14")
        break
    except:
        pass

enum_anon_35 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 32

LV_ANIM_OFF = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 32

LV_ANIM_ON = (LV_ANIM_OFF + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 32

lv_anim_enable_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 37

lv_anim_value_t = lv_coord_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 40

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 75
class struct__lv_anim_t(Structure):
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 51
class struct__lv_anim_path_t(Structure):
    pass

lv_anim_path_cb_t = CFUNCTYPE(UNCHECKED(lv_anim_value_t), POINTER(struct__lv_anim_path_t), POINTER(struct__lv_anim_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 49

struct__lv_anim_path_t.__slots__ = [
    'cb',
    'user_data',
]
struct__lv_anim_path_t._fields_ = [
    ('cb', lv_anim_path_cb_t),
    ('user_data', POINTER(None)),
]

lv_anim_path_t = struct__lv_anim_path_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 54

lv_anim_exec_xcb_t = CFUNCTYPE(UNCHECKED(None), POINTER(None), lv_anim_value_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 62

lv_anim_custom_exec_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_anim_t), lv_anim_value_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 66

lv_anim_ready_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_anim_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 69

lv_anim_start_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_anim_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 72

struct__lv_anim_t.__slots__ = [
    'var',
    'exec_cb',
    'start_cb',
    'ready_cb',
    'path',
    'start',
    'current',
    'end',
    'time',
    'act_time',
    'playback_delay',
    'playback_time',
    'repeat_delay',
    'repeat_cnt',
    'early_apply',
    'time_orig',
    'playback_now',
    'has_run',
]
struct__lv_anim_t._fields_ = [
    ('var', POINTER(None)),
    ('exec_cb', lv_anim_exec_xcb_t),
    ('start_cb', lv_anim_start_cb_t),
    ('ready_cb', lv_anim_ready_cb_t),
    ('path', lv_anim_path_t),
    ('start', c_int32),
    ('current', c_int32),
    ('end', c_int32),
    ('time', c_int32),
    ('act_time', c_int32),
    ('playback_delay', c_uint32),
    ('playback_time', c_uint32),
    ('repeat_delay', c_uint32),
    ('repeat_cnt', c_uint16),
    ('early_apply', c_uint8, 1),
    ('time_orig', c_uint32),
    ('playback_now', c_uint8, 1),
    ('has_run', c_uint32, 1),
]

lv_anim_t = struct__lv_anim_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 99

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 108
for _lib in _libs.values():
    if not _lib.has("_lv_anim_core_init", "cdecl"):
        continue
    _lv_anim_core_init = _lib.get("_lv_anim_core_init", "cdecl")
    _lv_anim_core_init.argtypes = []
    _lv_anim_core_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 118
for _lib in _libs.values():
    if not _lib.has("lv_anim_init", "cdecl"):
        continue
    lv_anim_init = _lib.get("lv_anim_init", "cdecl")
    lv_anim_init.argtypes = [POINTER(lv_anim_t)]
    lv_anim_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 265
for _lib in _libs.values():
    if not _lib.has("lv_anim_start", "cdecl"):
        continue
    lv_anim_start = _lib.get("lv_anim_start", "cdecl")
    lv_anim_start.argtypes = [POINTER(lv_anim_t)]
    lv_anim_start.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 313
for _lib in _libs.values():
    if not _lib.has("lv_anim_del", "cdecl"):
        continue
    lv_anim_del = _lib.get("lv_anim_del", "cdecl")
    lv_anim_del.argtypes = [POINTER(None), lv_anim_exec_xcb_t]
    lv_anim_del.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 322
for _lib in _libs.values():
    if not _lib.has("lv_anim_get", "cdecl"):
        continue
    lv_anim_get = _lib.get("lv_anim_get", "cdecl")
    lv_anim_get.argtypes = [POINTER(None), lv_anim_exec_xcb_t]
    lv_anim_get.restype = POINTER(lv_anim_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 344
for _lib in _libs.values():
    if not _lib.has("lv_anim_count_running", "cdecl"):
        continue
    lv_anim_count_running = _lib.get("lv_anim_count_running", "cdecl")
    lv_anim_count_running.argtypes = []
    lv_anim_count_running.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 353
for _lib in _libs.values():
    if not _lib.has("lv_anim_speed_to_time", "cdecl"):
        continue
    lv_anim_speed_to_time = _lib.get("lv_anim_speed_to_time", "cdecl")
    lv_anim_speed_to_time.argtypes = [c_uint16, lv_anim_value_t, lv_anim_value_t]
    lv_anim_speed_to_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 361
for _lib in _libs.values():
    if not _lib.has("lv_anim_refr_now", "cdecl"):
        continue
    lv_anim_refr_now = _lib.get("lv_anim_refr_now", "cdecl")
    lv_anim_refr_now.argtypes = []
    lv_anim_refr_now.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 368
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_linear", "cdecl"):
        continue
    lv_anim_path_linear = _lib.get("lv_anim_path_linear", "cdecl")
    lv_anim_path_linear.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_linear.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 375
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_ease_in", "cdecl"):
        continue
    lv_anim_path_ease_in = _lib.get("lv_anim_path_ease_in", "cdecl")
    lv_anim_path_ease_in.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_ease_in.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 382
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_ease_out", "cdecl"):
        continue
    lv_anim_path_ease_out = _lib.get("lv_anim_path_ease_out", "cdecl")
    lv_anim_path_ease_out.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_ease_out.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 389
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_ease_in_out", "cdecl"):
        continue
    lv_anim_path_ease_in_out = _lib.get("lv_anim_path_ease_in_out", "cdecl")
    lv_anim_path_ease_in_out.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_ease_in_out.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 396
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_overshoot", "cdecl"):
        continue
    lv_anim_path_overshoot = _lib.get("lv_anim_path_overshoot", "cdecl")
    lv_anim_path_overshoot.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_overshoot.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 403
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_bounce", "cdecl"):
        continue
    lv_anim_path_bounce = _lib.get("lv_anim_path_bounce", "cdecl")
    lv_anim_path_bounce.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_bounce.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 411
for _lib in _libs.values():
    if not _lib.has("lv_anim_path_step", "cdecl"):
        continue
    lv_anim_path_step = _lib.get("lv_anim_path_step", "cdecl")
    lv_anim_path_step.argtypes = [POINTER(lv_anim_path_t), POINTER(lv_anim_t)]
    lv_anim_path_step.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 416
for _lib in _libs.values():
    try:
        lv_anim_path_def = (lv_anim_path_t).in_dll(_lib, "lv_anim_path_def")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 32
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_null", "cdecl"):
        continue
    lv_debug_check_null = _lib.get("lv_debug_check_null", "cdecl")
    lv_debug_check_null.argtypes = [POINTER(None)]
    lv_debug_check_null.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 34
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_mem_integrity", "cdecl"):
        continue
    lv_debug_check_mem_integrity = _lib.get("lv_debug_check_mem_integrity", "cdecl")
    lv_debug_check_mem_integrity.argtypes = []
    lv_debug_check_mem_integrity.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 36
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_str", "cdecl"):
        continue
    lv_debug_check_str = _lib.get("lv_debug_check_str", "cdecl")
    lv_debug_check_str.argtypes = [POINTER(None)]
    lv_debug_check_str.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 38
for _lib in _libs.values():
    if not _lib.has("lv_debug_log_error", "cdecl"):
        continue
    lv_debug_log_error = _lib.get("lv_debug_log_error", "cdecl")
    lv_debug_log_error.argtypes = [String, c_uint64]
    lv_debug_log_error.restype = None
    break

enum_anon_36 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 30

LV_DRAW_MASK_RES_TRANSP = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 30

LV_DRAW_MASK_RES_FULL_COVER = (LV_DRAW_MASK_RES_TRANSP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 30

LV_DRAW_MASK_RES_CHANGED = (LV_DRAW_MASK_RES_FULL_COVER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 30

LV_DRAW_MASK_RES_UNKNOWN = (LV_DRAW_MASK_RES_CHANGED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 30

lv_draw_mask_res_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 37

enum_anon_37 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

LV_DRAW_MASK_TYPE_LINE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

LV_DRAW_MASK_TYPE_ANGLE = (LV_DRAW_MASK_TYPE_LINE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

LV_DRAW_MASK_TYPE_RADIUS = (LV_DRAW_MASK_TYPE_ANGLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

LV_DRAW_MASK_TYPE_FADE = (LV_DRAW_MASK_TYPE_RADIUS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

LV_DRAW_MASK_TYPE_MAP = (LV_DRAW_MASK_TYPE_FADE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 39

lv_draw_mask_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 47

enum_anon_38 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 49

LV_DRAW_MASK_LINE_SIDE_LEFT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 49

LV_DRAW_MASK_LINE_SIDE_RIGHT = (LV_DRAW_MASK_LINE_SIDE_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 49

LV_DRAW_MASK_LINE_SIDE_TOP = (LV_DRAW_MASK_LINE_SIDE_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 49

LV_DRAW_MASK_LINE_SIDE_BOTTOM = (LV_DRAW_MASK_LINE_SIDE_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 49

lv_draw_mask_xcb_t = CFUNCTYPE(UNCHECKED(lv_draw_mask_res_t), POINTER(lv_opa_t), lv_coord_t, lv_coord_t, lv_coord_t, POINTER(None))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 60

lv_draw_mask_line_side_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 64

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 69
class struct_anon_39(Structure):
    pass

struct_anon_39.__slots__ = [
    'cb',
    'type',
]
struct_anon_39._fields_ = [
    ('cb', lv_draw_mask_xcb_t),
    ('type', lv_draw_mask_type_t),
]

lv_draw_mask_common_dsc_t = struct_anon_39# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 69

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 75
class struct_anon_40(Structure):
    pass

struct_anon_40.__slots__ = [
    'p1',
    'p2',
    'side',
]
struct_anon_40._fields_ = [
    ('p1', lv_point_t),
    ('p2', lv_point_t),
    ('side', lv_draw_mask_line_side_t, 2),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 107
class struct_anon_41(Structure):
    pass

struct_anon_41.__slots__ = [
    'dsc',
    'cfg',
    'origo',
    'xy_steep',
    'yx_steep',
    'steep',
    'spx',
    'flat',
    'inv',
]
struct_anon_41._fields_ = [
    ('dsc', lv_draw_mask_common_dsc_t),
    ('cfg', struct_anon_40),
    ('origo', lv_point_t),
    ('xy_steep', c_int32),
    ('yx_steep', c_int32),
    ('steep', c_int32),
    ('spx', c_int32),
    ('flat', c_uint8, 1),
    ('inv', c_uint8, 1),
]

lv_draw_mask_line_param_t = struct_anon_41# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 107

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 113
class struct_anon_42(Structure):
    pass

struct_anon_42.__slots__ = [
    'vertex_p',
    'start_angle',
    'end_angle',
]
struct_anon_42._fields_ = [
    ('vertex_p', lv_point_t),
    ('start_angle', lv_coord_t),
    ('end_angle', lv_coord_t),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 122
class struct_anon_43(Structure):
    pass

struct_anon_43.__slots__ = [
    'dsc',
    'cfg',
    'start_line',
    'end_line',
    'delta_deg',
]
struct_anon_43._fields_ = [
    ('dsc', lv_draw_mask_common_dsc_t),
    ('cfg', struct_anon_42),
    ('start_line', lv_draw_mask_line_param_t),
    ('end_line', lv_draw_mask_line_param_t),
    ('delta_deg', c_uint16),
]

lv_draw_mask_angle_param_t = struct_anon_43# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 122

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 128
class struct_anon_44(Structure):
    pass

struct_anon_44.__slots__ = [
    'rect',
    'radius',
    'outer',
]
struct_anon_44._fields_ = [
    ('rect', lv_area_t),
    ('radius', lv_coord_t),
    ('outer', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 137
class struct_anon_45(Structure):
    pass

struct_anon_45.__slots__ = [
    'dsc',
    'cfg',
    'y_prev',
    'y_prev_x',
]
struct_anon_45._fields_ = [
    ('dsc', lv_draw_mask_common_dsc_t),
    ('cfg', struct_anon_44),
    ('y_prev', c_int32),
    ('y_prev_x', lv_sqrt_res_t),
]

lv_draw_mask_radius_param_t = struct_anon_45# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 137

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 143
class struct_anon_46(Structure):
    pass

struct_anon_46.__slots__ = [
    'coords',
    'y_top',
    'y_bottom',
    'opa_top',
    'opa_bottom',
]
struct_anon_46._fields_ = [
    ('coords', lv_area_t),
    ('y_top', lv_coord_t),
    ('y_bottom', lv_coord_t),
    ('opa_top', lv_opa_t),
    ('opa_bottom', lv_opa_t),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 151
class struct_anon_47(Structure):
    pass

struct_anon_47.__slots__ = [
    'dsc',
    'cfg',
]
struct_anon_47._fields_ = [
    ('dsc', lv_draw_mask_common_dsc_t),
    ('cfg', struct_anon_46),
]

lv_draw_mask_fade_param_t = struct_anon_47# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 151

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 157
class struct_anon_48(Structure):
    pass

struct_anon_48.__slots__ = [
    'coords',
    'map',
]
struct_anon_48._fields_ = [
    ('coords', lv_area_t),
    ('map', POINTER(lv_opa_t)),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 161
class struct__lv_draw_mask_map_param_t(Structure):
    pass

struct__lv_draw_mask_map_param_t.__slots__ = [
    'dsc',
    'cfg',
]
struct__lv_draw_mask_map_param_t._fields_ = [
    ('dsc', lv_draw_mask_common_dsc_t),
    ('cfg', struct_anon_48),
]

lv_draw_mask_map_param_t = struct__lv_draw_mask_map_param_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 161

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 166
class struct_anon_49(Structure):
    pass

struct_anon_49.__slots__ = [
    'param',
    'custom_id',
]
struct_anon_49._fields_ = [
    ('param', POINTER(None)),
    ('custom_id', POINTER(None)),
]

_lv_draw_mask_saved_t = struct_anon_49# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 166

_lv_draw_mask_saved_arr_t = _lv_draw_mask_saved_t * int(16)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 168

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 180
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_add", "cdecl"):
        continue
    lv_draw_mask_add = _lib.get("lv_draw_mask_add", "cdecl")
    lv_draw_mask_add.argtypes = [POINTER(None), POINTER(None)]
    lv_draw_mask_add.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 195
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_apply", "cdecl"):
        continue
    lv_draw_mask_apply = _lib.get("lv_draw_mask_apply", "cdecl")
    lv_draw_mask_apply.argtypes = [POINTER(lv_opa_t), lv_coord_t, lv_coord_t, lv_coord_t]
    lv_draw_mask_apply.restype = lv_draw_mask_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 206
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_remove_id", "cdecl"):
        continue
    lv_draw_mask_remove_id = _lib.get("lv_draw_mask_remove_id", "cdecl")
    lv_draw_mask_remove_id.argtypes = [c_int16]
    lv_draw_mask_remove_id.restype = POINTER(c_ubyte)
    lv_draw_mask_remove_id.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 214
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_remove_custom", "cdecl"):
        continue
    lv_draw_mask_remove_custom = _lib.get("lv_draw_mask_remove_custom", "cdecl")
    lv_draw_mask_remove_custom.argtypes = [POINTER(None)]
    lv_draw_mask_remove_custom.restype = POINTER(c_ubyte)
    lv_draw_mask_remove_custom.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 222
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_get_cnt", "cdecl"):
        continue
    lv_draw_mask_get_cnt = _lib.get("lv_draw_mask_get_cnt", "cdecl")
    lv_draw_mask_get_cnt.argtypes = []
    lv_draw_mask_get_cnt.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 237
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_line_points_init", "cdecl"):
        continue
    lv_draw_mask_line_points_init = _lib.get("lv_draw_mask_line_points_init", "cdecl")
    lv_draw_mask_line_points_init.argtypes = [POINTER(lv_draw_mask_line_param_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t, lv_draw_mask_line_side_t]
    lv_draw_mask_line_points_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 250
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_line_angle_init", "cdecl"):
        continue
    lv_draw_mask_line_angle_init = _lib.get("lv_draw_mask_line_angle_init", "cdecl")
    lv_draw_mask_line_angle_init.argtypes = [POINTER(lv_draw_mask_line_param_t), lv_coord_t, lv_coord_t, c_int16, lv_draw_mask_line_side_t]
    lv_draw_mask_line_angle_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 261
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_angle_init", "cdecl"):
        continue
    lv_draw_mask_angle_init = _lib.get("lv_draw_mask_angle_init", "cdecl")
    lv_draw_mask_angle_init.argtypes = [POINTER(lv_draw_mask_angle_param_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t]
    lv_draw_mask_angle_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 271
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_radius_init", "cdecl"):
        continue
    lv_draw_mask_radius_init = _lib.get("lv_draw_mask_radius_init", "cdecl")
    lv_draw_mask_radius_init.argtypes = [POINTER(lv_draw_mask_radius_param_t), POINTER(lv_area_t), lv_coord_t, c_bool]
    lv_draw_mask_radius_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 282
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_fade_init", "cdecl"):
        continue
    lv_draw_mask_fade_init = _lib.get("lv_draw_mask_fade_init", "cdecl")
    lv_draw_mask_fade_init.argtypes = [POINTER(lv_draw_mask_fade_param_t), POINTER(lv_area_t), lv_opa_t, lv_coord_t, lv_opa_t, lv_coord_t]
    lv_draw_mask_fade_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 292
for _lib in _libs.values():
    if not _lib.has("lv_draw_mask_map_init", "cdecl"):
        continue
    lv_draw_mask_map_init = _lib.get("lv_draw_mask_map_init", "cdecl")
    lv_draw_mask_map_init.argtypes = [POINTER(lv_draw_mask_map_param_t), POINTER(lv_area_t), POINTER(lv_opa_t)]
    lv_draw_mask_map_init.restype = None
    break

enum_anon_50 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 27

LV_BLEND_MODE_NORMAL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 27

LV_BLEND_MODE_ADDITIVE = (LV_BLEND_MODE_NORMAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 27

LV_BLEND_MODE_SUBTRACTIVE = (LV_BLEND_MODE_ADDITIVE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 27

lv_blend_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 35

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 42
for _lib in _libs.values():
    if not _lib.has("_lv_blend_fill", "cdecl"):
        continue
    _lv_blend_fill = _lib.get("_lv_blend_fill", "cdecl")
    _lv_blend_fill.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), lv_color_t, POINTER(lv_opa_t), lv_draw_mask_res_t, lv_opa_t, lv_blend_mode_t]
    _lv_blend_fill.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_blend.h: 45
for _lib in _libs.values():
    if not _lib.has("_lv_blend_map", "cdecl"):
        continue
    _lv_blend_map = _lib.get("_lv_blend_map", "cdecl")
    _lv_blend_map.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(lv_color_t), POINTER(lv_opa_t), lv_draw_mask_res_t, lv_opa_t, lv_blend_mode_t]
    _lv_blend_map.restype = None
    break

enum_anon_51 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_BOTTOM = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_TOP = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_LEFT = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_RIGHT = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_FULL = 15# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

LV_BORDER_SIDE_INTERNAL = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

_LV_BORDER_SIDE_LAST = (LV_BORDER_SIDE_INTERNAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 53

lv_border_side_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 63

enum_anon_52 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 65

LV_GRAD_DIR_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 65

LV_GRAD_DIR_VER = (LV_GRAD_DIR_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 65

LV_GRAD_DIR_HOR = (LV_GRAD_DIR_VER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 65

_LV_GRAD_DIR_LAST = (LV_GRAD_DIR_HOR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 65

lv_grad_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 72

enum_anon_53 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 75

LV_TEXT_DECOR_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 75

LV_TEXT_DECOR_UNDERLINE = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 75

LV_TEXT_DECOR_STRIKETHROUGH = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 75

_LV_TEXT_DECOR_LAST = (LV_TEXT_DECOR_STRIKETHROUGH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 75

lv_text_decor_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 82

lv_style_attr_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 84

enum_anon_54 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_RADIUS = ((((0 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_CLIP_CORNER = ((((0 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SIZE = ((((0 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSFORM_WIDTH = ((((0 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSFORM_HEIGHT = ((((0 << 4) + 0) + 5) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSFORM_ANGLE = ((((0 << 4) + 0) + 6) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSFORM_ZOOM = ((((0 << 4) + 0) + 7) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OPA_SCALE = ((((0 << 4) + 12) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PAD_TOP = ((((1 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PAD_BOTTOM = ((((1 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PAD_LEFT = ((((1 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PAD_RIGHT = ((((1 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PAD_INNER = ((((1 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_MARGIN_TOP = ((((1 << 4) + 0) + 5) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_MARGIN_BOTTOM = ((((1 << 4) + 0) + 6) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_MARGIN_LEFT = ((((1 << 4) + 0) + 7) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_MARGIN_RIGHT = ((((1 << 4) + 0) + 8) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_BLEND_MODE = ((((2 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_MAIN_STOP = ((((2 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_GRAD_STOP = ((((2 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_GRAD_DIR = ((((2 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_COLOR = ((((2 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_GRAD_COLOR = ((((2 << 4) + 9) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BG_OPA = ((((2 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_WIDTH = ((((3 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_SIDE = ((((3 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_BLEND_MODE = ((((3 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_POST = ((((3 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_COLOR = ((((3 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_BORDER_OPA = ((((3 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OUTLINE_WIDTH = ((((4 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OUTLINE_PAD = ((((4 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OUTLINE_BLEND_MODE = ((((4 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OUTLINE_COLOR = ((((4 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_OUTLINE_OPA = ((((4 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_WIDTH = ((((5 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_OFS_X = ((((5 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_OFS_Y = ((((5 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_SPREAD = ((((5 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_BLEND_MODE = ((((5 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_COLOR = ((((5 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SHADOW_OPA = ((((5 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_BLEND_MODE = ((((6 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_REPEAT = ((((6 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_RECOLOR = ((((6 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_OPA = ((((6 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_RECOLOR_OPA = ((((6 << 4) + 12) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_PATTERN_IMAGE = ((((6 << 4) + 14) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_LETTER_SPACE = ((((7 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_LINE_SPACE = ((((7 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_BLEND_MODE = ((((7 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_OFS_X = ((((7 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_OFS_Y = ((((7 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_ALIGN = ((((7 << 4) + 0) + 5) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_COLOR = ((((7 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_OPA = ((((7 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_FONT = ((((7 << 4) + 14) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_VALUE_STR = ((((7 << 4) + 14) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_LETTER_SPACE = ((((8 << 4) + 0) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_LINE_SPACE = ((((8 << 4) + 0) + 1) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_DECOR = ((((8 << 4) + 0) + 2) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_BLEND_MODE = ((((8 << 4) + 0) + 3) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_COLOR = ((((8 << 4) + 9) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_SEL_COLOR = ((((8 << 4) + 9) + 1) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_SEL_BG_COLOR = ((((8 << 4) + 9) + 2) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_OPA = ((((8 << 4) + 12) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TEXT_FONT = ((((8 << 4) + 14) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_WIDTH = ((((9 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_BLEND_MODE = ((((9 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_DASH_WIDTH = ((((9 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_DASH_GAP = ((((9 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_ROUNDED = ((((9 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_COLOR = ((((9 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_LINE_OPA = ((((9 << 4) + 12) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_IMAGE_BLEND_MODE = ((((10 << 4) + 0) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_IMAGE_RECOLOR = ((((10 << 4) + 9) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_IMAGE_OPA = ((((10 << 4) + 12) + 0) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_IMAGE_RECOLOR_OPA = ((((10 << 4) + 12) + 1) | ((1 << 7) << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_TIME = ((((11 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_DELAY = ((((11 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_1 = ((((11 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_2 = ((((11 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_3 = ((((11 << 4) + 0) + 4) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_4 = ((((11 << 4) + 0) + 5) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_5 = ((((11 << 4) + 0) + 6) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PROP_6 = ((((11 << 4) + 0) + 7) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_TRANSITION_PATH = ((((11 << 4) + 14) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_WIDTH = ((((12 << 4) + 0) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_BORDER_WIDTH = ((((12 << 4) + 0) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_END_BORDER_WIDTH = ((((12 << 4) + 0) + 2) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_END_LINE_WIDTH = ((((12 << 4) + 0) + 3) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_GRAD_COLOR = ((((12 << 4) + 9) + 0) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

LV_STYLE_SCALE_END_COLOR = ((((12 << 4) + 9) + 1) | (0 << 8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 94

lv_style_property_t = c_uint16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 203

lv_style_state_t = c_uint16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 209

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 216
class struct_anon_55(Structure):
    pass

struct_anon_55.__slots__ = [
    'map',
]
struct_anon_55._fields_ = [
    ('map', POINTER(c_uint8)),
]

lv_style_t = struct_anon_55# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 216

lv_style_int_t = c_int16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 218

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 256
class struct_anon_56(Structure):
    pass

struct_anon_56.__slots__ = [
    'style_list',
    'style_cnt',
    'has_local',
    'has_trans',
    'skip_trans',
    'ignore_trans',
    'valid_cache',
    'ignore_cache',
    'radius_zero',
    'opa_scale_cover',
    'clip_corner_off',
    'transform_all_zero',
    'pad_all_zero',
    'margin_all_zero',
    'blend_mode_all_normal',
    'bg_opa_transp',
    'bg_opa_cover',
    'border_width_zero',
    'border_side_full',
    'border_post_off',
    'outline_width_zero',
    'pattern_img_null',
    'shadow_width_zero',
    'value_txt_str',
    'img_recolor_opa_transp',
    'text_space_zero',
    'text_decor_none',
    'text_font_normal',
]
struct_anon_56._fields_ = [
    ('style_list', POINTER(POINTER(lv_style_t))),
    ('style_cnt', c_uint32, 6),
    ('has_local', c_uint32, 1),
    ('has_trans', c_uint32, 1),
    ('skip_trans', c_uint32, 1),
    ('ignore_trans', c_uint32, 1),
    ('valid_cache', c_uint32, 1),
    ('ignore_cache', c_uint32, 1),
    ('radius_zero', c_uint32, 1),
    ('opa_scale_cover', c_uint32, 1),
    ('clip_corner_off', c_uint32, 1),
    ('transform_all_zero', c_uint32, 1),
    ('pad_all_zero', c_uint32, 1),
    ('margin_all_zero', c_uint32, 1),
    ('blend_mode_all_normal', c_uint32, 1),
    ('bg_opa_transp', c_uint32, 1),
    ('bg_opa_cover', c_uint32, 1),
    ('border_width_zero', c_uint32, 1),
    ('border_side_full', c_uint32, 1),
    ('border_post_off', c_uint32, 1),
    ('outline_width_zero', c_uint32, 1),
    ('pattern_img_null', c_uint32, 1),
    ('shadow_width_zero', c_uint32, 1),
    ('value_txt_str', c_uint32, 1),
    ('img_recolor_opa_transp', c_uint32, 1),
    ('text_space_zero', c_uint32, 1),
    ('text_decor_none', c_uint32, 1),
    ('text_font_normal', c_uint32, 1),
]

lv_style_list_t = struct_anon_56# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 256

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 266
for _lib in _libs.values():
    if not _lib.has("lv_style_init", "cdecl"):
        continue
    lv_style_init = _lib.get("lv_style_init", "cdecl")
    lv_style_init.argtypes = [POINTER(lv_style_t)]
    lv_style_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 273
for _lib in _libs.values():
    if not _lib.has("lv_style_copy", "cdecl"):
        continue
    lv_style_copy = _lib.get("lv_style_copy", "cdecl")
    lv_style_copy.argtypes = [POINTER(lv_style_t), POINTER(lv_style_t)]
    lv_style_copy.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 279
for _lib in _libs.values():
    if not _lib.has("lv_style_list_init", "cdecl"):
        continue
    lv_style_list_init = _lib.get("lv_style_list_init", "cdecl")
    lv_style_list_init.argtypes = [POINTER(lv_style_list_t)]
    lv_style_list_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 286
for _lib in _libs.values():
    if not _lib.has("lv_style_list_copy", "cdecl"):
        continue
    lv_style_list_copy = _lib.get("lv_style_list_copy", "cdecl")
    lv_style_list_copy.argtypes = [POINTER(lv_style_list_t), POINTER(lv_style_list_t)]
    lv_style_list_copy.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 295
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_add_style", "cdecl"):
        continue
    _lv_style_list_add_style = _lib.get("_lv_style_list_add_style", "cdecl")
    _lv_style_list_add_style.argtypes = [POINTER(lv_style_list_t), POINTER(lv_style_t)]
    _lv_style_list_add_style.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 302
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_remove_style", "cdecl"):
        continue
    _lv_style_list_remove_style = _lib.get("_lv_style_list_remove_style", "cdecl")
    _lv_style_list_remove_style.argtypes = [POINTER(lv_style_list_t), POINTER(lv_style_t)]
    _lv_style_list_remove_style.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 309
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_reset", "cdecl"):
        continue
    _lv_style_list_reset = _lib.get("_lv_style_list_reset", "cdecl")
    _lv_style_list_reset.argtypes = [POINTER(lv_style_list_t)]
    _lv_style_list_reset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 322
for _lib in _libs.values():
    if not _lib.has("lv_style_reset", "cdecl"):
        continue
    lv_style_reset = _lib.get("lv_style_reset", "cdecl")
    lv_style_reset.argtypes = [POINTER(lv_style_t)]
    lv_style_reset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 329
for _lib in _libs.values():
    if not _lib.has("_lv_style_get_mem_size", "cdecl"):
        continue
    _lv_style_get_mem_size = _lib.get("_lv_style_get_mem_size", "cdecl")
    _lv_style_get_mem_size.argtypes = [POINTER(lv_style_t)]
    _lv_style_get_mem_size.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 336
for _lib in _libs.values():
    if not _lib.has("lv_style_copy", "cdecl"):
        continue
    lv_style_copy = _lib.get("lv_style_copy", "cdecl")
    lv_style_copy.argtypes = [POINTER(lv_style_t), POINTER(lv_style_t)]
    lv_style_copy.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 345
for _lib in _libs.values():
    if not _lib.has("lv_style_remove_prop", "cdecl"):
        continue
    lv_style_remove_prop = _lib.get("lv_style_remove_prop", "cdecl")
    lv_style_remove_prop.argtypes = [POINTER(lv_style_t), lv_style_property_t]
    lv_style_remove_prop.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 357
for _lib in _libs.values():
    if not _lib.has("_lv_style_set_int", "cdecl"):
        continue
    _lv_style_set_int = _lib.get("_lv_style_set_int", "cdecl")
    _lv_style_set_int.argtypes = [POINTER(lv_style_t), lv_style_property_t, lv_style_int_t]
    _lv_style_set_int.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 369
for _lib in _libs.values():
    if not _lib.has("_lv_style_set_color", "cdecl"):
        continue
    _lv_style_set_color = _lib.get("_lv_style_set_color", "cdecl")
    _lv_style_set_color.argtypes = [POINTER(lv_style_t), lv_style_property_t, lv_color_t]
    _lv_style_set_color.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 381
for _lib in _libs.values():
    if not _lib.has("_lv_style_set_opa", "cdecl"):
        continue
    _lv_style_set_opa = _lib.get("_lv_style_set_opa", "cdecl")
    _lv_style_set_opa.argtypes = [POINTER(lv_style_t), lv_style_property_t, lv_opa_t]
    _lv_style_set_opa.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 393
for _lib in _libs.values():
    if not _lib.has("_lv_style_set_ptr", "cdecl"):
        continue
    _lv_style_set_ptr = _lib.get("_lv_style_set_ptr", "cdecl")
    _lv_style_set_ptr.argtypes = [POINTER(lv_style_t), lv_style_property_t, POINTER(None)]
    _lv_style_set_ptr.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 408
for _lib in _libs.values():
    if not _lib.has("_lv_style_get_int", "cdecl"):
        continue
    _lv_style_get_int = _lib.get("_lv_style_get_int", "cdecl")
    _lv_style_get_int.argtypes = [POINTER(lv_style_t), lv_style_property_t, POINTER(None)]
    _lv_style_get_int.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 423
for _lib in _libs.values():
    if not _lib.has("_lv_style_get_color", "cdecl"):
        continue
    _lv_style_get_color = _lib.get("_lv_style_get_color", "cdecl")
    _lv_style_get_color.argtypes = [POINTER(lv_style_t), lv_style_property_t, POINTER(None)]
    _lv_style_get_color.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 438
for _lib in _libs.values():
    if not _lib.has("_lv_style_get_opa", "cdecl"):
        continue
    _lv_style_get_opa = _lib.get("_lv_style_get_opa", "cdecl")
    _lv_style_get_opa.argtypes = [POINTER(lv_style_t), lv_style_property_t, POINTER(None)]
    _lv_style_get_opa.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 453
for _lib in _libs.values():
    if not _lib.has("_lv_style_get_ptr", "cdecl"):
        continue
    _lv_style_get_ptr = _lib.get("_lv_style_get_ptr", "cdecl")
    _lv_style_get_ptr.argtypes = [POINTER(lv_style_t), lv_style_property_t, POINTER(None)]
    _lv_style_get_ptr.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 460
for _lib in _libs.values():
    if not _lib.has("lv_style_list_get_local_style", "cdecl"):
        continue
    lv_style_list_get_local_style = _lib.get("lv_style_list_get_local_style", "cdecl")
    lv_style_list_get_local_style.argtypes = [POINTER(lv_style_list_t)]
    lv_style_list_get_local_style.restype = POINTER(lv_style_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 467
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_get_transition_style", "cdecl"):
        continue
    _lv_style_list_get_transition_style = _lib.get("_lv_style_list_get_transition_style", "cdecl")
    _lv_style_list_get_transition_style.argtypes = [POINTER(lv_style_list_t)]
    _lv_style_list_get_transition_style.restype = POINTER(lv_style_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 474
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_add_trans_style", "cdecl"):
        continue
    _lv_style_list_add_trans_style = _lib.get("_lv_style_list_add_trans_style", "cdecl")
    _lv_style_list_add_trans_style.argtypes = [POINTER(lv_style_list_t)]
    _lv_style_list_add_trans_style.restype = POINTER(lv_style_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 484
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_set_local_int", "cdecl"):
        continue
    _lv_style_list_set_local_int = _lib.get("_lv_style_list_set_local_int", "cdecl")
    _lv_style_list_set_local_int.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, lv_style_int_t]
    _lv_style_list_set_local_int.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 494
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_set_local_color", "cdecl"):
        continue
    _lv_style_list_set_local_color = _lib.get("_lv_style_list_set_local_color", "cdecl")
    _lv_style_list_set_local_color.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, lv_color_t]
    _lv_style_list_set_local_color.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 504
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_set_local_opa", "cdecl"):
        continue
    _lv_style_list_set_local_opa = _lib.get("_lv_style_list_set_local_opa", "cdecl")
    _lv_style_list_set_local_opa.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, lv_opa_t]
    _lv_style_list_set_local_opa.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 514
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_set_local_ptr", "cdecl"):
        continue
    _lv_style_list_set_local_ptr = _lib.get("_lv_style_list_set_local_ptr", "cdecl")
    _lv_style_list_set_local_ptr.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, POINTER(None)]
    _lv_style_list_set_local_ptr.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 527
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_get_int", "cdecl"):
        continue
    _lv_style_list_get_int = _lib.get("_lv_style_list_get_int", "cdecl")
    _lv_style_list_get_int.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, POINTER(lv_style_int_t)]
    _lv_style_list_get_int.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 540
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_get_color", "cdecl"):
        continue
    _lv_style_list_get_color = _lib.get("_lv_style_list_get_color", "cdecl")
    _lv_style_list_get_color.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, POINTER(lv_color_t)]
    _lv_style_list_get_color.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 553
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_get_opa", "cdecl"):
        continue
    _lv_style_list_get_opa = _lib.get("_lv_style_list_get_opa", "cdecl")
    _lv_style_list_get_opa.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, POINTER(lv_opa_t)]
    _lv_style_list_get_opa.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 566
for _lib in _libs.values():
    if not _lib.has("_lv_style_list_get_ptr", "cdecl"):
        continue
    _lv_style_list_get_ptr = _lib.get("_lv_style_list_get_ptr", "cdecl")
    _lv_style_list_get_ptr.argtypes = [POINTER(lv_style_list_t), lv_style_property_t, POINTER(POINTER(None))]
    _lv_style_list_get_ptr.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 573
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_style", "cdecl"):
        continue
    lv_debug_check_style = _lib.get("lv_debug_check_style", "cdecl")
    lv_debug_check_style.argtypes = [POINTER(lv_style_t)]
    lv_debug_check_style.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 580
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_style_list", "cdecl"):
        continue
    lv_debug_check_style_list = _lib.get("lv_debug_check_style_list", "cdecl")
    lv_debug_check_style_list.argtypes = [POINTER(lv_style_list_t)]
    lv_debug_check_style_list.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_rect.h: 82
class struct_anon_57(Structure):
    pass

struct_anon_57.__slots__ = [
    'radius',
    'bg_color',
    'bg_grad_color',
    'bg_grad_dir',
    'bg_main_color_stop',
    'bg_grad_color_stop',
    'bg_opa',
    'bg_blend_mode',
    'border_color',
    'border_width',
    'border_side',
    'border_opa',
    'border_blend_mode',
    'border_post',
    'outline_color',
    'outline_width',
    'outline_pad',
    'outline_opa',
    'outline_blend_mode',
    'shadow_color',
    'shadow_width',
    'shadow_ofs_x',
    'shadow_ofs_y',
    'shadow_spread',
    'shadow_opa',
    'shadow_blend_mode',
    'pattern_image',
    'pattern_font',
    'pattern_recolor',
    'pattern_opa',
    'pattern_recolor_opa',
    'pattern_repeat',
    'pattern_blend_mode',
    'value_str',
    'value_font',
    'value_opa',
    'value_color',
    'value_ofs_x',
    'value_ofs_y',
    'value_letter_space',
    'value_line_space',
    'value_align',
    'value_blend_mode',
]
struct_anon_57._fields_ = [
    ('radius', lv_style_int_t),
    ('bg_color', lv_color_t),
    ('bg_grad_color', lv_color_t),
    ('bg_grad_dir', lv_grad_dir_t),
    ('bg_main_color_stop', lv_style_int_t),
    ('bg_grad_color_stop', lv_style_int_t),
    ('bg_opa', lv_opa_t),
    ('bg_blend_mode', lv_blend_mode_t),
    ('border_color', lv_color_t),
    ('border_width', lv_style_int_t),
    ('border_side', lv_style_int_t),
    ('border_opa', lv_opa_t),
    ('border_blend_mode', lv_blend_mode_t),
    ('border_post', c_uint8, 1),
    ('outline_color', lv_color_t),
    ('outline_width', lv_style_int_t),
    ('outline_pad', lv_style_int_t),
    ('outline_opa', lv_opa_t),
    ('outline_blend_mode', lv_blend_mode_t),
    ('shadow_color', lv_color_t),
    ('shadow_width', lv_style_int_t),
    ('shadow_ofs_x', lv_style_int_t),
    ('shadow_ofs_y', lv_style_int_t),
    ('shadow_spread', lv_style_int_t),
    ('shadow_opa', lv_opa_t),
    ('shadow_blend_mode', lv_blend_mode_t),
    ('pattern_image', POINTER(None)),
    ('pattern_font', POINTER(lv_font_t)),
    ('pattern_recolor', lv_color_t),
    ('pattern_opa', lv_opa_t),
    ('pattern_recolor_opa', lv_opa_t),
    ('pattern_repeat', c_uint8, 1),
    ('pattern_blend_mode', lv_blend_mode_t),
    ('value_str', String),
    ('value_font', POINTER(lv_font_t)),
    ('value_opa', lv_opa_t),
    ('value_color', lv_color_t),
    ('value_ofs_x', lv_style_int_t),
    ('value_ofs_y', lv_style_int_t),
    ('value_letter_space', lv_style_int_t),
    ('value_line_space', lv_style_int_t),
    ('value_align', lv_align_t),
    ('value_blend_mode', lv_blend_mode_t),
]

lv_draw_rect_dsc_t = struct_anon_57# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_rect.h: 82

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_rect.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_draw_rect_dsc_init", "cdecl"):
        continue
    lv_draw_rect_dsc_init = _lib.get("lv_draw_rect_dsc_init", "cdecl")
    lv_draw_rect_dsc_init.argtypes = [POINTER(lv_draw_rect_dsc_t)]
    lv_draw_rect_dsc_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_rect.h: 98
for _lib in _libs.values():
    if not _lib.has("lv_draw_rect", "cdecl"):
        continue
    lv_draw_rect = _lib.get("lv_draw_rect", "cdecl")
    lv_draw_rect.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(lv_draw_rect_dsc_t)]
    lv_draw_rect.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_rect.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_draw_px", "cdecl"):
        continue
    lv_draw_px = _lib.get("lv_draw_px", "cdecl")
    lv_draw_px.argtypes = [POINTER(lv_point_t), POINTER(lv_area_t), POINTER(lv_style_t)]
    lv_draw_px.restype = None
    break

enum_anon_58 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_LTR = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_RTL = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_AUTO = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_INHERIT = 3# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_NEUTRAL = 32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

LV_BIDI_DIR_WEAK = 33# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 32

lv_bidi_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 43

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_printf.h: 56
for _lib in _libs.values():
    if _lib.has("lv_snprintf", "cdecl"):
        _func = _lib.get("lv_snprintf", "cdecl")
        _restype = c_int
        _errcheck = None
        _argtypes = [String, c_size_t, String]
        lv_snprintf = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_printf.h: 57
for _lib in _libs.values():
    if not _lib.has("lv_vsnprintf", "cdecl"):
        continue
    lv_vsnprintf = _lib.get("lv_vsnprintf", "cdecl")
    lv_vsnprintf.argtypes = [String, c_size_t, String, c_void_p]
    lv_vsnprintf.restype = c_int
    break

enum_anon_59 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_RECOLOR = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_EXPAND = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_CENTER = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_RIGHT = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

LV_TXT_FLAG_FIT = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 41

lv_txt_flag_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 49

enum_anon_60 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 53

LV_TXT_CMD_STATE_WAIT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 53

LV_TXT_CMD_STATE_PAR = (LV_TXT_CMD_STATE_WAIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 53

LV_TXT_CMD_STATE_IN = (LV_TXT_CMD_STATE_PAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 53

lv_txt_cmd_state_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 58

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 75
for _lib in _libs.values():
    if not _lib.has("_lv_txt_get_size", "cdecl"):
        continue
    _lv_txt_get_size = _lib.get("_lv_txt_get_size", "cdecl")
    _lv_txt_get_size.argtypes = [POINTER(lv_point_t), String, POINTER(lv_font_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_txt_flag_t]
    _lv_txt_get_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 89
for _lib in _libs.values():
    if not _lib.has("_lv_txt_get_next_line", "cdecl"):
        continue
    _lv_txt_get_next_line = _lib.get("_lv_txt_get_next_line", "cdecl")
    _lv_txt_get_next_line.argtypes = [String, POINTER(lv_font_t), lv_coord_t, lv_coord_t, lv_txt_flag_t]
    _lv_txt_get_next_line.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 102
for _lib in _libs.values():
    if not _lib.has("_lv_txt_get_width", "cdecl"):
        continue
    _lv_txt_get_width = _lib.get("_lv_txt_get_width", "cdecl")
    _lv_txt_get_width.argtypes = [String, c_uint32, POINTER(lv_font_t), lv_coord_t, lv_txt_flag_t]
    _lv_txt_get_width.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 113
for _lib in _libs.values():
    if not _lib.has("_lv_txt_is_cmd", "cdecl"):
        continue
    _lv_txt_is_cmd = _lib.get("_lv_txt_is_cmd", "cdecl")
    _lv_txt_is_cmd.argtypes = [POINTER(lv_txt_cmd_state_t), c_uint32]
    _lv_txt_is_cmd.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 121
for _lib in _libs.values():
    if not _lib.has("_lv_txt_ins", "cdecl"):
        continue
    _lv_txt_ins = _lib.get("_lv_txt_ins", "cdecl")
    _lv_txt_ins.argtypes = [String, c_uint32, String]
    _lv_txt_ins.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 130
for _lib in _libs.values():
    if not _lib.has("_lv_txt_cut", "cdecl"):
        continue
    _lv_txt_cut = _lib.get("_lv_txt_cut", "cdecl")
    _lv_txt_cut.argtypes = [String, c_uint32, c_uint32]
    _lv_txt_cut.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 137
for _lib in _libs.values():
    if not _lib.has("_lv_txt_set_text_vfmt", "cdecl"):
        continue
    _lv_txt_set_text_vfmt = _lib.get("_lv_txt_set_text_vfmt", "cdecl")
    _lv_txt_set_text_vfmt.argtypes = [String, c_void_p]
    if sizeof(c_int) == sizeof(c_void_p):
        _lv_txt_set_text_vfmt.restype = ReturnString
    else:
        _lv_txt_set_text_vfmt.restype = String
        _lv_txt_set_text_vfmt.errcheck = ReturnString
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 148
for _lib in _libs.values():
    try:
        _lv_txt_encoded_size = (POINTER(CFUNCTYPE(UNCHECKED(c_uint8), String))).in_dll(_lib, "_lv_txt_encoded_size")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 155
for _lib in _libs.values():
    try:
        _lv_txt_unicode_to_encoded = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), c_uint32))).in_dll(_lib, "_lv_txt_unicode_to_encoded")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 162
for _lib in _libs.values():
    try:
        _lv_txt_encoded_conv_wc = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), c_uint32))).in_dll(_lib, "_lv_txt_encoded_conv_wc")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 172
for _lib in _libs.values():
    try:
        _lv_txt_encoded_next = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), String, POINTER(c_uint32)))).in_dll(_lib, "_lv_txt_encoded_next")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 181
for _lib in _libs.values():
    try:
        _lv_txt_encoded_prev = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), String, POINTER(c_uint32)))).in_dll(_lib, "_lv_txt_encoded_prev")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 190
for _lib in _libs.values():
    try:
        _lv_txt_encoded_get_byte_id = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), String, c_uint32))).in_dll(_lib, "_lv_txt_encoded_get_byte_id")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 199
for _lib in _libs.values():
    try:
        _lv_txt_encoded_get_char_id = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), String, c_uint32))).in_dll(_lib, "_lv_txt_encoded_get_char_id")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 207
for _lib in _libs.values():
    try:
        _lv_txt_get_encoded_length = (POINTER(CFUNCTYPE(UNCHECKED(c_uint32), String))).in_dll(_lib, "_lv_txt_get_encoded_length")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 45
class struct_anon_61(Structure):
    pass

struct_anon_61.__slots__ = [
    'color',
    'sel_color',
    'sel_bg_color',
    'font',
    'opa',
    'line_space',
    'letter_space',
    'sel_start',
    'sel_end',
    'ofs_x',
    'ofs_y',
    'bidi_dir',
    'flag',
    'decor',
    'blend_mode',
]
struct_anon_61._fields_ = [
    ('color', lv_color_t),
    ('sel_color', lv_color_t),
    ('sel_bg_color', lv_color_t),
    ('font', POINTER(lv_font_t)),
    ('opa', lv_opa_t),
    ('line_space', lv_style_int_t),
    ('letter_space', lv_style_int_t),
    ('sel_start', c_uint32),
    ('sel_end', c_uint32),
    ('ofs_x', lv_coord_t),
    ('ofs_y', lv_coord_t),
    ('bidi_dir', lv_bidi_dir_t),
    ('flag', lv_txt_flag_t),
    ('decor', lv_text_decor_t),
    ('blend_mode', lv_blend_mode_t),
]

lv_draw_label_dsc_t = struct_anon_61# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 45

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 62
class struct_anon_62(Structure):
    pass

struct_anon_62.__slots__ = [
    'line_start',
    'y',
    'coord_y',
]
struct_anon_62._fields_ = [
    ('line_start', c_int32),
    ('y', c_int32),
    ('coord_y', c_int32),
]

lv_draw_label_hint_t = struct_anon_62# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 62

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 70
for _lib in _libs.values():
    if not _lib.has("lv_draw_label_dsc_init", "cdecl"):
        continue
    lv_draw_label_dsc_init = _lib.get("lv_draw_label_dsc_init", "cdecl")
    lv_draw_label_dsc_init.argtypes = [POINTER(lv_draw_label_dsc_t)]
    lv_draw_label_dsc_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 81
for _lib in _libs.values():
    if not _lib.has("lv_draw_label", "cdecl"):
        continue
    lv_draw_label = _lib.get("lv_draw_label", "cdecl")
    lv_draw_label.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(lv_draw_label_dsc_t), String, POINTER(lv_draw_label_hint_t)]
    lv_draw_label.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 89
for _lib in _libs.values():
    try:
        _lv_bpp2_opa_table = (POINTER(c_uint8)).in_dll(_lib, "_lv_bpp2_opa_table")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 90
for _lib in _libs.values():
    try:
        _lv_bpp3_opa_table = (POINTER(c_uint8)).in_dll(_lib, "_lv_bpp3_opa_table")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 91
for _lib in _libs.values():
    try:
        _lv_bpp1_opa_table = (POINTER(c_uint8)).in_dll(_lib, "_lv_bpp1_opa_table")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 92
for _lib in _libs.values():
    try:
        _lv_bpp4_opa_table = (POINTER(c_uint8)).in_dll(_lib, "_lv_bpp4_opa_table")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 93
for _lib in _libs.values():
    try:
        _lv_bpp8_opa_table = (POINTER(c_uint8)).in_dll(_lib, "_lv_bpp8_opa_table")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_line.h: 35
class struct_anon_63(Structure):
    pass

struct_anon_63.__slots__ = [
    'color',
    'width',
    'dash_width',
    'dash_gap',
    'opa',
    'blend_mode',
    'round_start',
    'round_end',
    'raw_end',
]
struct_anon_63._fields_ = [
    ('color', lv_color_t),
    ('width', lv_style_int_t),
    ('dash_width', lv_style_int_t),
    ('dash_gap', lv_style_int_t),
    ('opa', lv_opa_t),
    ('blend_mode', lv_blend_mode_t, 2),
    ('round_start', c_uint8, 1),
    ('round_end', c_uint8, 1),
    ('raw_end', c_uint8, 1),
]

lv_draw_line_dsc_t = struct_anon_63# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_line.h: 35

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_line.h: 49
for _lib in _libs.values():
    if not _lib.has("lv_draw_line", "cdecl"):
        continue
    lv_draw_line = _lib.get("lv_draw_line", "cdecl")
    lv_draw_line.argtypes = [POINTER(lv_point_t), POINTER(lv_point_t), POINTER(lv_area_t), POINTER(lv_draw_line_dsc_t)]
    lv_draw_line.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_line.h: 52
for _lib in _libs.values():
    if not _lib.has("lv_draw_line_dsc_init", "cdecl"):
        continue
    lv_draw_line_dsc_init = _lib.get("lv_draw_line_dsc_init", "cdecl")
    lv_draw_line_dsc_init.argtypes = [POINTER(lv_draw_line_dsc_t)]
    lv_draw_line_dsc_init.restype = None
    break

enum_anon_64 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_UNKNOWN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RAW = (LV_IMG_CF_UNKNOWN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RAW_ALPHA = (LV_IMG_CF_RAW + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RAW_CHROMA_KEYED = (LV_IMG_CF_RAW_ALPHA + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_TRUE_COLOR = (LV_IMG_CF_RAW_CHROMA_KEYED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_TRUE_COLOR_ALPHA = (LV_IMG_CF_TRUE_COLOR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED = (LV_IMG_CF_TRUE_COLOR_ALPHA + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_INDEXED_1BIT = (LV_IMG_CF_TRUE_COLOR_CHROMA_KEYED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_INDEXED_2BIT = (LV_IMG_CF_INDEXED_1BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_INDEXED_4BIT = (LV_IMG_CF_INDEXED_2BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_INDEXED_8BIT = (LV_IMG_CF_INDEXED_4BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_ALPHA_1BIT = (LV_IMG_CF_INDEXED_8BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_ALPHA_2BIT = (LV_IMG_CF_ALPHA_1BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_ALPHA_4BIT = (LV_IMG_CF_ALPHA_2BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_ALPHA_8BIT = (LV_IMG_CF_ALPHA_4BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_15 = (LV_IMG_CF_ALPHA_8BIT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_16 = (LV_IMG_CF_RESERVED_15 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_17 = (LV_IMG_CF_RESERVED_16 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_18 = (LV_IMG_CF_RESERVED_17 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_19 = (LV_IMG_CF_RESERVED_18 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_20 = (LV_IMG_CF_RESERVED_19 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_21 = (LV_IMG_CF_RESERVED_20 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_22 = (LV_IMG_CF_RESERVED_21 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_RESERVED_23 = (LV_IMG_CF_RESERVED_22 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_0 = (LV_IMG_CF_RESERVED_23 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_1 = (LV_IMG_CF_USER_ENCODED_0 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_2 = (LV_IMG_CF_USER_ENCODED_1 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_3 = (LV_IMG_CF_USER_ENCODED_2 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_4 = (LV_IMG_CF_USER_ENCODED_3 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_5 = (LV_IMG_CF_USER_ENCODED_4 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_6 = (LV_IMG_CF_USER_ENCODED_5 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

LV_IMG_CF_USER_ENCODED_7 = (LV_IMG_CF_USER_ENCODED_6 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 58

lv_img_cf_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 101

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 133
class struct_anon_65(Structure):
    pass

struct_anon_65.__slots__ = [
    'cf',
    'always_zero',
    'reserved',
    'w',
    'h',
]
struct_anon_65._fields_ = [
    ('cf', c_uint32, 5),
    ('always_zero', c_uint32, 3),
    ('reserved', c_uint32, 2),
    ('w', c_uint32, 11),
    ('h', c_uint32, 11),
]

lv_img_header_t = struct_anon_65# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 133

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 142
class struct_anon_66(Structure):
    pass

struct_anon_66.__slots__ = [
    'header',
    'data_size',
    'data',
]
struct_anon_66._fields_ = [
    ('header', lv_img_header_t),
    ('data_size', c_uint32),
    ('data', POINTER(c_uint8)),
]

lv_img_dsc_t = struct_anon_66# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 142

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 145
class struct_anon_67(Structure):
    pass

struct_anon_67.__slots__ = [
    'src',
    'src_w',
    'src_h',
    'pivot_x',
    'pivot_y',
    'angle',
    'zoom',
    'color',
    'cf',
    'antialias',
]
struct_anon_67._fields_ = [
    ('src', POINTER(None)),
    ('src_w', lv_coord_t),
    ('src_h', lv_coord_t),
    ('pivot_x', lv_coord_t),
    ('pivot_y', lv_coord_t),
    ('angle', c_int16),
    ('zoom', c_uint16),
    ('color', lv_color_t),
    ('cf', lv_img_cf_t),
    ('antialias', c_bool),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 158
class struct_anon_68(Structure):
    pass

struct_anon_68.__slots__ = [
    'color',
    'opa',
]
struct_anon_68._fields_ = [
    ('color', lv_color_t),
    ('opa', lv_opa_t),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 163
class struct_anon_69(Structure):
    pass

struct_anon_69.__slots__ = [
    'img_dsc',
    'pivot_x_256',
    'pivot_y_256',
    'sinma',
    'cosma',
    'chroma_keyed',
    'has_alpha',
    'native_color',
    'zoom_inv',
    'xs',
    'ys',
    'xs_int',
    'ys_int',
    'pxi',
    'px_size',
]
struct_anon_69._fields_ = [
    ('img_dsc', lv_img_dsc_t),
    ('pivot_x_256', c_int32),
    ('pivot_y_256', c_int32),
    ('sinma', c_int32),
    ('cosma', c_int32),
    ('chroma_keyed', c_uint8, 1),
    ('has_alpha', c_uint8, 1),
    ('native_color', c_uint8, 1),
    ('zoom_inv', c_uint32),
    ('xs', lv_coord_t),
    ('ys', lv_coord_t),
    ('xs_int', lv_coord_t),
    ('ys_int', lv_coord_t),
    ('pxi', c_uint32),
    ('px_size', c_uint8),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 184
class struct_anon_70(Structure):
    pass

struct_anon_70.__slots__ = [
    'cfg',
    'res',
    'tmp',
]
struct_anon_70._fields_ = [
    ('cfg', struct_anon_67),
    ('res', struct_anon_68),
    ('tmp', struct_anon_69),
]

lv_img_transform_dsc_t = struct_anon_70# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 184

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 197
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_alloc", "cdecl"):
        continue
    lv_img_buf_alloc = _lib.get("lv_img_buf_alloc", "cdecl")
    lv_img_buf_alloc.argtypes = [lv_coord_t, lv_coord_t, lv_img_cf_t]
    lv_img_buf_alloc.restype = POINTER(lv_img_dsc_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 209
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_get_px_color", "cdecl"):
        continue
    lv_img_buf_get_px_color = _lib.get("lv_img_buf_get_px_color", "cdecl")
    lv_img_buf_get_px_color.argtypes = [POINTER(lv_img_dsc_t), lv_coord_t, lv_coord_t, lv_color_t]
    lv_img_buf_get_px_color.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 219
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_get_px_alpha", "cdecl"):
        continue
    lv_img_buf_get_px_alpha = _lib.get("lv_img_buf_get_px_alpha", "cdecl")
    lv_img_buf_get_px_alpha.argtypes = [POINTER(lv_img_dsc_t), lv_coord_t, lv_coord_t]
    lv_img_buf_get_px_alpha.restype = lv_opa_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_set_px_color", "cdecl"):
        continue
    lv_img_buf_set_px_color = _lib.get("lv_img_buf_set_px_color", "cdecl")
    lv_img_buf_set_px_color.argtypes = [POINTER(lv_img_dsc_t), lv_coord_t, lv_coord_t, lv_color_t]
    lv_img_buf_set_px_color.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 239
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_set_px_alpha", "cdecl"):
        continue
    lv_img_buf_set_px_alpha = _lib.get("lv_img_buf_set_px_alpha", "cdecl")
    lv_img_buf_set_px_alpha.argtypes = [POINTER(lv_img_dsc_t), lv_coord_t, lv_coord_t, lv_opa_t]
    lv_img_buf_set_px_alpha.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 251
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_set_palette", "cdecl"):
        continue
    lv_img_buf_set_palette = _lib.get("lv_img_buf_set_palette", "cdecl")
    lv_img_buf_set_palette.argtypes = [POINTER(lv_img_dsc_t), c_uint8, lv_color_t]
    lv_img_buf_set_palette.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 257
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_free", "cdecl"):
        continue
    lv_img_buf_free = _lib.get("lv_img_buf_free", "cdecl")
    lv_img_buf_free.argtypes = [POINTER(lv_img_dsc_t)]
    lv_img_buf_free.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 266
for _lib in _libs.values():
    if not _lib.has("lv_img_buf_get_img_size", "cdecl"):
        continue
    lv_img_buf_get_img_size = _lib.get("lv_img_buf_get_img_size", "cdecl")
    lv_img_buf_get_img_size.argtypes = [lv_coord_t, lv_coord_t, lv_img_cf_t]
    lv_img_buf_get_img_size.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 273
for _lib in _libs.values():
    if not _lib.has("_lv_img_buf_transform_init", "cdecl"):
        continue
    _lv_img_buf_transform_init = _lib.get("_lv_img_buf_transform_init", "cdecl")
    _lv_img_buf_transform_init.argtypes = [POINTER(lv_img_transform_dsc_t)]
    _lv_img_buf_transform_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 279
for _lib in _libs.values():
    if not _lib.has("_lv_img_buf_transform_anti_alias", "cdecl"):
        continue
    _lv_img_buf_transform_anti_alias = _lib.get("_lv_img_buf_transform_anti_alias", "cdecl")
    _lv_img_buf_transform_anti_alias.argtypes = [POINTER(lv_img_transform_dsc_t)]
    _lv_img_buf_transform_anti_alias.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 291
for _lib in _libs.values():
    try:
        src_u8 = (POINTER(c_uint8)).in_dll(_lib, "src_u8")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 294
for _lib in _libs.values():
    try:
        xt = (c_int32).in_dll(_lib, "xt")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 295
for _lib in _libs.values():
    try:
        yt = (c_int32).in_dll(_lib, "yt")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 297
for _lib in _libs.values():
    try:
        xs = (c_int32).in_dll(_lib, "xs")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 298
for _lib in _libs.values():
    try:
        ys = (c_int32).in_dll(_lib, "ys")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 364
for _lib in _libs.values():
    try:
        ret = (c_bool).in_dll(_lib, "ret")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 379
for _lib in _libs.values():
    if not _lib.has("_lv_img_buf_get_transformed_area", "cdecl"):
        continue
    _lv_img_buf_get_transformed_area = _lib.get("_lv_img_buf_get_transformed_area", "cdecl")
    _lv_img_buf_get_transformed_area.argtypes = [POINTER(lv_area_t), lv_coord_t, lv_coord_t, c_int16, c_uint16, POINTER(lv_point_t)]
    _lv_img_buf_get_transformed_area.restype = None
    break

enum_anon_71 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_OK = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_HW_ERR = (LV_FS_RES_OK + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_FS_ERR = (LV_FS_RES_HW_ERR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_NOT_EX = (LV_FS_RES_FS_ERR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_FULL = (LV_FS_RES_NOT_EX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_LOCKED = (LV_FS_RES_FULL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_DENIED = (LV_FS_RES_LOCKED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_BUSY = (LV_FS_RES_DENIED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_TOUT = (LV_FS_RES_BUSY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_NOT_IMP = (LV_FS_RES_TOUT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_OUT_OF_MEM = (LV_FS_RES_NOT_IMP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_INV_PARAM = (LV_FS_RES_OUT_OF_MEM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

LV_FS_RES_UNKNOWN = (LV_FS_RES_INV_PARAM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 37

lv_fs_res_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 52

enum_anon_72 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 57

LV_FS_MODE_WR = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 57

LV_FS_MODE_RD = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 57

lv_fs_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 61

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 63
class struct__lv_fs_drv_t(Structure):
    pass

struct__lv_fs_drv_t.__slots__ = [
    'letter',
    'file_size',
    'rddir_size',
    'ready_cb',
    'open_cb',
    'close_cb',
    'remove_cb',
    'read_cb',
    'write_cb',
    'seek_cb',
    'tell_cb',
    'trunc_cb',
    'size_cb',
    'rename_cb',
    'free_space_cb',
    'dir_open_cb',
    'dir_read_cb',
    'dir_close_cb',
]
struct__lv_fs_drv_t._fields_ = [
    ('letter', c_char),
    ('file_size', c_uint16),
    ('rddir_size', c_uint16),
    ('ready_cb', CFUNCTYPE(UNCHECKED(c_bool), POINTER(struct__lv_fs_drv_t))),
    ('open_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), String, lv_fs_mode_t)),
    ('close_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None))),
    ('remove_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), String)),
    ('read_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), POINTER(None), c_uint32, POINTER(c_uint32))),
    ('write_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), POINTER(None), c_uint32, POINTER(c_uint32))),
    ('seek_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), c_uint32)),
    ('tell_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), POINTER(c_uint32))),
    ('trunc_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None))),
    ('size_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), POINTER(c_uint32))),
    ('rename_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), String, String)),
    ('free_space_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(c_uint32), POINTER(c_uint32))),
    ('dir_open_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), String)),
    ('dir_read_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None), String)),
    ('dir_close_cb', CFUNCTYPE(UNCHECKED(lv_fs_res_t), POINTER(struct__lv_fs_drv_t), POINTER(None))),
]

lv_fs_drv_t = struct__lv_fs_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 88

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 93
class struct_anon_73(Structure):
    pass

struct_anon_73.__slots__ = [
    'file_d',
    'drv',
]
struct_anon_73._fields_ = [
    ('file_d', POINTER(None)),
    ('drv', POINTER(lv_fs_drv_t)),
]

lv_fs_file_t = struct_anon_73# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 93

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 98
class struct_anon_74(Structure):
    pass

struct_anon_74.__slots__ = [
    'dir_d',
    'drv',
]
struct_anon_74._fields_ = [
    ('dir_d', POINTER(None)),
    ('drv', POINTER(lv_fs_drv_t)),
]

lv_fs_dir_t = struct_anon_74# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 98

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 107
for _lib in _libs.values():
    if not _lib.has("_lv_fs_init", "cdecl"):
        continue
    _lv_fs_init = _lib.get("_lv_fs_init", "cdecl")
    _lv_fs_init.argtypes = []
    _lv_fs_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 115
for _lib in _libs.values():
    if not _lib.has("lv_fs_drv_init", "cdecl"):
        continue
    lv_fs_drv_init = _lib.get("lv_fs_drv_init", "cdecl")
    lv_fs_drv_init.argtypes = [POINTER(lv_fs_drv_t)]
    lv_fs_drv_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 122
for _lib in _libs.values():
    if not _lib.has("lv_fs_drv_register", "cdecl"):
        continue
    lv_fs_drv_register = _lib.get("lv_fs_drv_register", "cdecl")
    lv_fs_drv_register.argtypes = [POINTER(lv_fs_drv_t)]
    lv_fs_drv_register.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_fs_get_drv", "cdecl"):
        continue
    lv_fs_get_drv = _lib.get("lv_fs_get_drv", "cdecl")
    lv_fs_get_drv.argtypes = [c_char]
    lv_fs_get_drv.restype = POINTER(lv_fs_drv_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 137
for _lib in _libs.values():
    if not _lib.has("lv_fs_is_ready", "cdecl"):
        continue
    lv_fs_is_ready = _lib.get("lv_fs_is_ready", "cdecl")
    lv_fs_is_ready.argtypes = [c_char]
    lv_fs_is_ready.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 146
for _lib in _libs.values():
    if not _lib.has("lv_fs_open", "cdecl"):
        continue
    lv_fs_open = _lib.get("lv_fs_open", "cdecl")
    lv_fs_open.argtypes = [POINTER(lv_fs_file_t), String, lv_fs_mode_t]
    lv_fs_open.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 153
for _lib in _libs.values():
    if not _lib.has("lv_fs_close", "cdecl"):
        continue
    lv_fs_close = _lib.get("lv_fs_close", "cdecl")
    lv_fs_close.argtypes = [POINTER(lv_fs_file_t)]
    lv_fs_close.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 160
for _lib in _libs.values():
    if not _lib.has("lv_fs_remove", "cdecl"):
        continue
    lv_fs_remove = _lib.get("lv_fs_remove", "cdecl")
    lv_fs_remove.argtypes = [String]
    lv_fs_remove.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 170
for _lib in _libs.values():
    if not _lib.has("lv_fs_read", "cdecl"):
        continue
    lv_fs_read = _lib.get("lv_fs_read", "cdecl")
    lv_fs_read.argtypes = [POINTER(lv_fs_file_t), POINTER(None), c_uint32, POINTER(c_uint32)]
    lv_fs_read.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 180
for _lib in _libs.values():
    if not _lib.has("lv_fs_write", "cdecl"):
        continue
    lv_fs_write = _lib.get("lv_fs_write", "cdecl")
    lv_fs_write.argtypes = [POINTER(lv_fs_file_t), POINTER(None), c_uint32, POINTER(c_uint32)]
    lv_fs_write.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 188
for _lib in _libs.values():
    if not _lib.has("lv_fs_seek", "cdecl"):
        continue
    lv_fs_seek = _lib.get("lv_fs_seek", "cdecl")
    lv_fs_seek.argtypes = [POINTER(lv_fs_file_t), c_uint32]
    lv_fs_seek.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 196
for _lib in _libs.values():
    if not _lib.has("lv_fs_tell", "cdecl"):
        continue
    lv_fs_tell = _lib.get("lv_fs_tell", "cdecl")
    lv_fs_tell.argtypes = [POINTER(lv_fs_file_t), POINTER(c_uint32)]
    lv_fs_tell.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 204
for _lib in _libs.values():
    if not _lib.has("lv_fs_trunc", "cdecl"):
        continue
    lv_fs_trunc = _lib.get("lv_fs_trunc", "cdecl")
    lv_fs_trunc.argtypes = [POINTER(lv_fs_file_t)]
    lv_fs_trunc.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 212
for _lib in _libs.values():
    if not _lib.has("lv_fs_size", "cdecl"):
        continue
    lv_fs_size = _lib.get("lv_fs_size", "cdecl")
    lv_fs_size.argtypes = [POINTER(lv_fs_file_t), POINTER(c_uint32)]
    lv_fs_size.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 220
for _lib in _libs.values():
    if not _lib.has("lv_fs_rename", "cdecl"):
        continue
    lv_fs_rename = _lib.get("lv_fs_rename", "cdecl")
    lv_fs_rename.argtypes = [String, String]
    lv_fs_rename.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 228
for _lib in _libs.values():
    if not _lib.has("lv_fs_dir_open", "cdecl"):
        continue
    lv_fs_dir_open = _lib.get("lv_fs_dir_open", "cdecl")
    lv_fs_dir_open.argtypes = [POINTER(lv_fs_dir_t), String]
    lv_fs_dir_open.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 237
for _lib in _libs.values():
    if not _lib.has("lv_fs_dir_read", "cdecl"):
        continue
    lv_fs_dir_read = _lib.get("lv_fs_dir_read", "cdecl")
    lv_fs_dir_read.argtypes = [POINTER(lv_fs_dir_t), String]
    lv_fs_dir_read.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 244
for _lib in _libs.values():
    if not _lib.has("lv_fs_dir_close", "cdecl"):
        continue
    lv_fs_dir_close = _lib.get("lv_fs_dir_close", "cdecl")
    lv_fs_dir_close.argtypes = [POINTER(lv_fs_dir_t)]
    lv_fs_dir_close.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 253
for _lib in _libs.values():
    if not _lib.has("lv_fs_free_space", "cdecl"):
        continue
    lv_fs_free_space = _lib.get("lv_fs_free_space", "cdecl")
    lv_fs_free_space.argtypes = [c_char, POINTER(c_uint32), POINTER(c_uint32)]
    lv_fs_free_space.restype = lv_fs_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 260
for _lib in _libs.values():
    if not _lib.has("lv_fs_get_letters", "cdecl"):
        continue
    lv_fs_get_letters = _lib.get("lv_fs_get_letters", "cdecl")
    lv_fs_get_letters.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        lv_fs_get_letters.restype = ReturnString
    else:
        lv_fs_get_letters.restype = String
        lv_fs_get_letters.errcheck = ReturnString
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 267
for _lib in _libs.values():
    if not _lib.has("lv_fs_get_ext", "cdecl"):
        continue
    lv_fs_get_ext = _lib.get("lv_fs_get_ext", "cdecl")
    lv_fs_get_ext.argtypes = [String]
    lv_fs_get_ext.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 274
for _lib in _libs.values():
    if not _lib.has("lv_fs_up", "cdecl"):
        continue
    lv_fs_up = _lib.get("lv_fs_up", "cdecl")
    lv_fs_up.argtypes = [String]
    if sizeof(c_int) == sizeof(c_void_p):
        lv_fs_up.restype = ReturnString
    else:
        lv_fs_up.restype = String
        lv_fs_up.errcheck = ReturnString
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 281
for _lib in _libs.values():
    if not _lib.has("lv_fs_get_last", "cdecl"):
        continue
    lv_fs_get_last = _lib.get("lv_fs_get_last", "cdecl")
    lv_fs_get_last.argtypes = [String]
    lv_fs_get_last.restype = c_char_p
    break

enum_anon_75 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 35

LV_IMG_SRC_VARIABLE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 35

LV_IMG_SRC_FILE = (LV_IMG_SRC_VARIABLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 35

LV_IMG_SRC_SYMBOL = (LV_IMG_SRC_FILE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 35

LV_IMG_SRC_UNKNOWN = (LV_IMG_SRC_SYMBOL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 35

lv_img_src_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 42

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 87
class struct__lv_img_decoder(Structure):
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 99
class struct__lv_img_decoder_dsc(Structure):
    pass

lv_img_decoder_info_f_t = CFUNCTYPE(UNCHECKED(lv_res_t), POINTER(struct__lv_img_decoder), POINTER(None), POINTER(lv_img_header_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 56

lv_img_decoder_open_f_t = CFUNCTYPE(UNCHECKED(lv_res_t), POINTER(struct__lv_img_decoder), POINTER(struct__lv_img_decoder_dsc))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 64

lv_img_decoder_read_line_f_t = CFUNCTYPE(UNCHECKED(lv_res_t), POINTER(struct__lv_img_decoder), POINTER(struct__lv_img_decoder_dsc), lv_coord_t, lv_coord_t, lv_coord_t, POINTER(c_uint8))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 77

lv_img_decoder_close_f_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_img_decoder), POINTER(struct__lv_img_decoder_dsc))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 85

struct__lv_img_decoder.__slots__ = [
    'info_cb',
    'open_cb',
    'read_line_cb',
    'close_cb',
]
struct__lv_img_decoder._fields_ = [
    ('info_cb', lv_img_decoder_info_f_t),
    ('open_cb', lv_img_decoder_open_f_t),
    ('read_line_cb', lv_img_decoder_read_line_f_t),
    ('close_cb', lv_img_decoder_close_f_t),
]

lv_img_decoder_t = struct__lv_img_decoder# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 96

struct__lv_img_decoder_dsc.__slots__ = [
    'decoder',
    'src',
    'color',
    'src_type',
    'header',
    'img_data',
    'time_to_open',
    'error_msg',
    'user_data',
]
struct__lv_img_decoder_dsc._fields_ = [
    ('decoder', POINTER(lv_img_decoder_t)),
    ('src', POINTER(None)),
    ('color', lv_color_t),
    ('src_type', lv_img_src_t),
    ('header', lv_img_header_t),
    ('img_data', POINTER(c_uint8)),
    ('time_to_open', c_uint32),
    ('error_msg', String),
    ('user_data', POINTER(None)),
]

lv_img_decoder_dsc_t = struct__lv_img_decoder_dsc# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 129

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 138
for _lib in _libs.values():
    if not _lib.has("_lv_img_decoder_init", "cdecl"):
        continue
    _lv_img_decoder_init = _lib.get("_lv_img_decoder_init", "cdecl")
    _lv_img_decoder_init.argtypes = []
    _lv_img_decoder_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_get_info", "cdecl"):
        continue
    lv_img_decoder_get_info = _lib.get("lv_img_decoder_get_info", "cdecl")
    lv_img_decoder_get_info.argtypes = [String, POINTER(lv_img_header_t)]
    lv_img_decoder_get_info.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 164
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_open", "cdecl"):
        continue
    lv_img_decoder_open = _lib.get("lv_img_decoder_open", "cdecl")
    lv_img_decoder_open.argtypes = [POINTER(lv_img_decoder_dsc_t), POINTER(None), lv_color_t]
    lv_img_decoder_open.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 175
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_read_line", "cdecl"):
        continue
    lv_img_decoder_read_line = _lib.get("lv_img_decoder_read_line", "cdecl")
    lv_img_decoder_read_line.argtypes = [POINTER(lv_img_decoder_dsc_t), lv_coord_t, lv_coord_t, lv_coord_t, POINTER(c_uint8)]
    lv_img_decoder_read_line.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 182
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_close", "cdecl"):
        continue
    lv_img_decoder_close = _lib.get("lv_img_decoder_close", "cdecl")
    lv_img_decoder_close.argtypes = [POINTER(lv_img_decoder_dsc_t)]
    lv_img_decoder_close.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 188
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_create", "cdecl"):
        continue
    lv_img_decoder_create = _lib.get("lv_img_decoder_create", "cdecl")
    lv_img_decoder_create.argtypes = []
    lv_img_decoder_create.restype = POINTER(lv_img_decoder_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 194
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_delete", "cdecl"):
        continue
    lv_img_decoder_delete = _lib.get("lv_img_decoder_delete", "cdecl")
    lv_img_decoder_delete.argtypes = [POINTER(lv_img_decoder_t)]
    lv_img_decoder_delete.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 201
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_set_info_cb", "cdecl"):
        continue
    lv_img_decoder_set_info_cb = _lib.get("lv_img_decoder_set_info_cb", "cdecl")
    lv_img_decoder_set_info_cb.argtypes = [POINTER(lv_img_decoder_t), lv_img_decoder_info_f_t]
    lv_img_decoder_set_info_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 208
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_set_open_cb", "cdecl"):
        continue
    lv_img_decoder_set_open_cb = _lib.get("lv_img_decoder_set_open_cb", "cdecl")
    lv_img_decoder_set_open_cb.argtypes = [POINTER(lv_img_decoder_t), lv_img_decoder_open_f_t]
    lv_img_decoder_set_open_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 215
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_set_read_line_cb", "cdecl"):
        continue
    lv_img_decoder_set_read_line_cb = _lib.get("lv_img_decoder_set_read_line_cb", "cdecl")
    lv_img_decoder_set_read_line_cb.argtypes = [POINTER(lv_img_decoder_t), lv_img_decoder_read_line_f_t]
    lv_img_decoder_set_read_line_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 222
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_set_close_cb", "cdecl"):
        continue
    lv_img_decoder_set_close_cb = _lib.get("lv_img_decoder_set_close_cb", "cdecl")
    lv_img_decoder_set_close_cb.argtypes = [POINTER(lv_img_decoder_t), lv_img_decoder_close_f_t]
    lv_img_decoder_set_close_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 231
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_built_in_info", "cdecl"):
        continue
    lv_img_decoder_built_in_info = _lib.get("lv_img_decoder_built_in_info", "cdecl")
    lv_img_decoder_built_in_info.argtypes = [POINTER(lv_img_decoder_t), POINTER(None), POINTER(lv_img_header_t)]
    lv_img_decoder_built_in_info.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 239
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_built_in_open", "cdecl"):
        continue
    lv_img_decoder_built_in_open = _lib.get("lv_img_decoder_built_in_open", "cdecl")
    lv_img_decoder_built_in_open.argtypes = [POINTER(lv_img_decoder_t), POINTER(lv_img_decoder_dsc_t)]
    lv_img_decoder_built_in_open.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 252
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_built_in_read_line", "cdecl"):
        continue
    lv_img_decoder_built_in_read_line = _lib.get("lv_img_decoder_built_in_read_line", "cdecl")
    lv_img_decoder_built_in_read_line.argtypes = [POINTER(lv_img_decoder_t), POINTER(lv_img_decoder_dsc_t), lv_coord_t, lv_coord_t, lv_coord_t, POINTER(c_uint8)]
    lv_img_decoder_built_in_read_line.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 260
for _lib in _libs.values():
    if not _lib.has("lv_img_decoder_built_in_close", "cdecl"):
        continue
    lv_img_decoder_built_in_close = _lib.get("lv_img_decoder_built_in_close", "cdecl")
    lv_img_decoder_built_in_close.argtypes = [POINTER(lv_img_decoder_t), POINTER(lv_img_decoder_dsc_t)]
    lv_img_decoder_built_in_close.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 44
class struct_anon_76(Structure):
    pass

struct_anon_76.__slots__ = [
    'opa',
    'angle',
    'pivot',
    'zoom',
    'recolor_opa',
    'recolor',
    'blend_mode',
    'antialias',
]
struct_anon_76._fields_ = [
    ('opa', lv_opa_t),
    ('angle', c_uint16),
    ('pivot', lv_point_t),
    ('zoom', c_uint16),
    ('recolor_opa', lv_opa_t),
    ('recolor', lv_color_t),
    ('blend_mode', lv_blend_mode_t),
    ('antialias', c_uint8, 1),
]

lv_draw_img_dsc_t = struct_anon_76# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 44

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 50
for _lib in _libs.values():
    if not _lib.has("lv_draw_img_dsc_init", "cdecl"):
        continue
    lv_draw_img_dsc_init = _lib.get("lv_draw_img_dsc_init", "cdecl")
    lv_draw_img_dsc_init.argtypes = [POINTER(lv_draw_img_dsc_t)]
    lv_draw_img_dsc_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 58
for _lib in _libs.values():
    if not _lib.has("lv_draw_img", "cdecl"):
        continue
    lv_draw_img = _lib.get("lv_draw_img", "cdecl")
    lv_draw_img.argtypes = [POINTER(lv_area_t), POINTER(lv_area_t), POINTER(None), POINTER(lv_draw_img_dsc_t)]
    lv_draw_img.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 68
for _lib in _libs.values():
    if not _lib.has("lv_img_src_get_type", "cdecl"):
        continue
    lv_img_src_get_type = _lib.get("lv_img_src_get_type", "cdecl")
    lv_img_src_get_type.argtypes = [POINTER(None)]
    lv_img_src_get_type.restype = lv_img_src_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_img_cf_get_px_size", "cdecl"):
        continue
    lv_img_cf_get_px_size = _lib.get("lv_img_cf_get_px_size", "cdecl")
    lv_img_cf_get_px_size.argtypes = [lv_img_cf_t]
    lv_img_cf_get_px_size.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_img_cf_is_chroma_keyed", "cdecl"):
        continue
    lv_img_cf_is_chroma_keyed = _lib.get("lv_img_cf_is_chroma_keyed", "cdecl")
    lv_img_cf_is_chroma_keyed.argtypes = [lv_img_cf_t]
    lv_img_cf_is_chroma_keyed.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_img.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_img_cf_has_alpha", "cdecl"):
        continue
    lv_img_cf_has_alpha = _lib.get("lv_img_cf_has_alpha", "cdecl")
    lv_img_cf_has_alpha.argtypes = [lv_img_cf_t]
    lv_img_cf_has_alpha.restype = c_bool
    break

enum_anon_77 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 60

LV_DESIGN_DRAW_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 60

LV_DESIGN_DRAW_POST = (LV_DESIGN_DRAW_MAIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 60

LV_DESIGN_COVER_CHK = (LV_DESIGN_DRAW_POST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 60

lv_design_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 65

enum_anon_78 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 68

LV_DESIGN_RES_OK = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 68

LV_DESIGN_RES_COVER = (LV_DESIGN_RES_OK + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 68

LV_DESIGN_RES_NOT_COVER = (LV_DESIGN_RES_COVER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 68

LV_DESIGN_RES_MASKED = (LV_DESIGN_RES_NOT_COVER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 68

lv_design_res_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 74

lv_design_cb_t = CFUNCTYPE(UNCHECKED(lv_design_res_t), POINTER(struct__lv_obj_t), POINTER(lv_area_t), lv_design_mode_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 80

enum_anon_79 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_PRESSED = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_PRESSING = (LV_EVENT_PRESSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_PRESS_LOST = (LV_EVENT_PRESSING + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_SHORT_CLICKED = (LV_EVENT_PRESS_LOST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_LONG_PRESSED = (LV_EVENT_SHORT_CLICKED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_LONG_PRESSED_REPEAT = (LV_EVENT_LONG_PRESSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_CLICKED = (LV_EVENT_LONG_PRESSED_REPEAT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_RELEASED = (LV_EVENT_CLICKED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_DRAG_BEGIN = (LV_EVENT_RELEASED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_DRAG_END = (LV_EVENT_DRAG_BEGIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_DRAG_THROW_BEGIN = (LV_EVENT_DRAG_END + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_GESTURE = (LV_EVENT_DRAG_THROW_BEGIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_KEY = (LV_EVENT_GESTURE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_FOCUSED = (LV_EVENT_KEY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_DEFOCUSED = (LV_EVENT_FOCUSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_LEAVE = (LV_EVENT_DEFOCUSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_VALUE_CHANGED = (LV_EVENT_LEAVE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_INSERT = (LV_EVENT_VALUE_CHANGED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_REFRESH = (LV_EVENT_INSERT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_APPLY = (LV_EVENT_REFRESH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_CANCEL = (LV_EVENT_APPLY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

LV_EVENT_DELETE = (LV_EVENT_CANCEL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

_LV_EVENT_LAST = (LV_EVENT_DELETE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 82

lv_event_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 108

lv_event_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_obj_t), lv_event_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 115

enum_anon_80 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_CLEANUP = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_CHILD_CHG = (LV_SIGNAL_CLEANUP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_COORD_CHG = (LV_SIGNAL_CHILD_CHG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_PARENT_SIZE_CHG = (LV_SIGNAL_COORD_CHG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_STYLE_CHG = (LV_SIGNAL_PARENT_SIZE_CHG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_BASE_DIR_CHG = (LV_SIGNAL_STYLE_CHG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_REFR_EXT_DRAW_PAD = (LV_SIGNAL_BASE_DIR_CHG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_GET_TYPE = (LV_SIGNAL_REFR_EXT_DRAW_PAD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_GET_STYLE = (LV_SIGNAL_GET_TYPE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_GET_STATE_DSC = (LV_SIGNAL_GET_STYLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_HIT_TEST = (LV_SIGNAL_GET_STATE_DSC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_PRESSED = (LV_SIGNAL_HIT_TEST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_PRESSING = (LV_SIGNAL_PRESSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_PRESS_LOST = (LV_SIGNAL_PRESSING + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_RELEASED = (LV_SIGNAL_PRESS_LOST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_LONG_PRESS = (LV_SIGNAL_RELEASED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_LONG_PRESS_REP = (LV_SIGNAL_LONG_PRESS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_DRAG_BEGIN = (LV_SIGNAL_LONG_PRESS_REP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_DRAG_THROW_BEGIN = (LV_SIGNAL_DRAG_BEGIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_DRAG_END = (LV_SIGNAL_DRAG_THROW_BEGIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_GESTURE = (LV_SIGNAL_DRAG_END + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_LEAVE = (LV_SIGNAL_GESTURE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_FOCUS = (LV_SIGNAL_LEAVE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_DEFOCUS = (LV_SIGNAL_FOCUS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_CONTROL = (LV_SIGNAL_DEFOCUS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

LV_SIGNAL_GET_EDITABLE = (LV_SIGNAL_CONTROL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 120

lv_signal_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 153

lv_signal_cb_t = CFUNCTYPE(UNCHECKED(lv_res_t), POINTER(struct__lv_obj_t), lv_signal_t, POINTER(None))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 155

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 166
class struct_anon_81(Structure):
    pass

struct_anon_81.__slots__ = [
    'base',
    'xofs',
    'yofs',
    'align',
    'auto_realign',
    'mid_align',
]
struct_anon_81._fields_ = [
    ('base', POINTER(struct__lv_obj_t)),
    ('xofs', lv_coord_t),
    ('yofs', lv_coord_t),
    ('align', lv_align_t),
    ('auto_realign', c_uint8, 1),
    ('mid_align', c_uint8, 1),
]

lv_realign_t = struct_anon_81# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 166

enum_anon_82 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_CHILD_CHG = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_PARENT = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_POS = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_FOLLOW = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_PRESS_LOST = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

LV_PROTECT_CLICK_FOCUS = 32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 170

lv_protect_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 181

enum_anon_83 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_DEFAULT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_CHECKED = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_FOCUSED = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_EDITED = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_HOVERED = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_PRESSED = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

LV_STATE_DISABLED = 32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 183

lv_state_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 193

struct__lv_obj_t.__slots__ = [
    'parent',
    'child_ll',
    'coords',
    'event_cb',
    'signal_cb',
    'design_cb',
    'ext_attr',
    'style_list',
    'ext_click_pad_hor',
    'ext_click_pad_ver',
    'ext_draw_pad',
    'click',
    'drag',
    'drag_throw',
    'drag_parent',
    'hidden',
    'top',
    'parent_event',
    'adv_hittest',
    'gesture_parent',
    'focus_parent',
    'drag_dir',
    'base_dir',
    'group_p',
    'protect',
    'state',
    'realign',
]
struct__lv_obj_t._fields_ = [
    ('parent', POINTER(struct__lv_obj_t)),
    ('child_ll', lv_ll_t),
    ('coords', lv_area_t),
    ('event_cb', lv_event_cb_t),
    ('signal_cb', lv_signal_cb_t),
    ('design_cb', lv_design_cb_t),
    ('ext_attr', POINTER(None)),
    ('style_list', lv_style_list_t),
    ('ext_click_pad_hor', c_uint8),
    ('ext_click_pad_ver', c_uint8),
    ('ext_draw_pad', lv_coord_t),
    ('click', c_uint8, 1),
    ('drag', c_uint8, 1),
    ('drag_throw', c_uint8, 1),
    ('drag_parent', c_uint8, 1),
    ('hidden', c_uint8, 1),
    ('top', c_uint8, 1),
    ('parent_event', c_uint8, 1),
    ('adv_hittest', c_uint8, 1),
    ('gesture_parent', c_uint8, 1),
    ('focus_parent', c_uint8, 1),
    ('drag_dir', lv_drag_dir_t, 3),
    ('base_dir', lv_bidi_dir_t, 2),
    ('group_p', POINTER(None)),
    ('protect', c_uint8),
    ('state', lv_state_t),
    ('realign', lv_realign_t),
]

lv_obj_t = struct__lv_obj_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 248

enum_anon_84 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 250

LV_OBJ_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 250

_LV_OBJ_PART_VIRTUAL_LAST = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 250

_LV_OBJ_PART_REAL_LAST = 64# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 250

LV_OBJ_PART_ALL = 255# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 250

lv_obj_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 257

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 263
class struct_anon_85(Structure):
    pass

struct_anon_85.__slots__ = [
    'type',
]
struct_anon_85._fields_ = [
    ('type', POINTER(c_char) * int(8)),
]

lv_obj_type_t = struct_anon_85# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 263

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 268
class struct_anon_86(Structure):
    pass

struct_anon_86.__slots__ = [
    'point',
    'result',
]
struct_anon_86._fields_ = [
    ('point', POINTER(lv_point_t)),
    ('result', c_bool),
]

lv_hit_test_info_t = struct_anon_86# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 268

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 273
class struct_anon_87(Structure):
    pass

struct_anon_87.__slots__ = [
    'part',
    'result',
]
struct_anon_87._fields_ = [
    ('part', c_uint8),
    ('result', POINTER(lv_style_list_t)),
]

lv_get_style_info_t = struct_anon_87# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 273

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 278
class struct_anon_88(Structure):
    pass

struct_anon_88.__slots__ = [
    'part',
    'result',
]
struct_anon_88._fields_ = [
    ('part', c_uint8),
    ('result', lv_state_t),
]

lv_get_state_info_t = struct_anon_88# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 278

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 287
for _lib in _libs.values():
    if not _lib.has("lv_init", "cdecl"):
        continue
    lv_init = _lib.get("lv_init", "cdecl")
    lv_init.argtypes = []
    lv_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 294
for _lib in _libs.values():
    if not _lib.has("lv_deinit", "cdecl"):
        continue
    lv_deinit = _lib.get("lv_deinit", "cdecl")
    lv_deinit.argtypes = []
    lv_deinit.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 308
for _lib in _libs.values():
    if not _lib.has("lv_obj_create", "cdecl"):
        continue
    lv_obj_create = _lib.get("lv_obj_create", "cdecl")
    lv_obj_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_obj_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 315
for _lib in _libs.values():
    if not _lib.has("lv_obj_del", "cdecl"):
        continue
    lv_obj_del = _lib.get("lv_obj_del", "cdecl")
    lv_obj_del.argtypes = [POINTER(lv_obj_t)]
    lv_obj_del.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 322
for _lib in _libs.values():
    if not _lib.has("lv_obj_del_anim_ready_cb", "cdecl"):
        continue
    lv_obj_del_anim_ready_cb = _lib.get("lv_obj_del_anim_ready_cb", "cdecl")
    lv_obj_del_anim_ready_cb.argtypes = [POINTER(lv_anim_t)]
    lv_obj_del_anim_ready_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 331
for _lib in _libs.values():
    if not _lib.has("lv_obj_del_async", "cdecl"):
        continue
    lv_obj_del_async = _lib.get("lv_obj_del_async", "cdecl")
    lv_obj_del_async.argtypes = [POINTER(struct__lv_obj_t)]
    lv_obj_del_async.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 337
for _lib in _libs.values():
    if not _lib.has("lv_obj_clean", "cdecl"):
        continue
    lv_obj_clean = _lib.get("lv_obj_clean", "cdecl")
    lv_obj_clean.argtypes = [POINTER(lv_obj_t)]
    lv_obj_clean.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 345
for _lib in _libs.values():
    if not _lib.has("lv_obj_invalidate_area", "cdecl"):
        continue
    lv_obj_invalidate_area = _lib.get("lv_obj_invalidate_area", "cdecl")
    lv_obj_invalidate_area.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t)]
    lv_obj_invalidate_area.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 351
for _lib in _libs.values():
    if not _lib.has("lv_obj_invalidate", "cdecl"):
        continue
    lv_obj_invalidate = _lib.get("lv_obj_invalidate", "cdecl")
    lv_obj_invalidate.argtypes = [POINTER(lv_obj_t)]
    lv_obj_invalidate.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 359
for _lib in _libs.values():
    if not _lib.has("lv_obj_area_is_visible", "cdecl"):
        continue
    lv_obj_area_is_visible = _lib.get("lv_obj_area_is_visible", "cdecl")
    lv_obj_area_is_visible.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t)]
    lv_obj_area_is_visible.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 366
for _lib in _libs.values():
    if not _lib.has("lv_obj_is_visible", "cdecl"):
        continue
    lv_obj_is_visible = _lib.get("lv_obj_is_visible", "cdecl")
    lv_obj_is_visible.argtypes = [POINTER(lv_obj_t)]
    lv_obj_is_visible.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 381
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_parent", "cdecl"):
        continue
    lv_obj_set_parent = _lib.get("lv_obj_set_parent", "cdecl")
    lv_obj_set_parent.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_obj_set_parent.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 387
for _lib in _libs.values():
    if not _lib.has("lv_obj_move_foreground", "cdecl"):
        continue
    lv_obj_move_foreground = _lib.get("lv_obj_move_foreground", "cdecl")
    lv_obj_move_foreground.argtypes = [POINTER(lv_obj_t)]
    lv_obj_move_foreground.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 393
for _lib in _libs.values():
    if not _lib.has("lv_obj_move_background", "cdecl"):
        continue
    lv_obj_move_background = _lib.get("lv_obj_move_background", "cdecl")
    lv_obj_move_background.argtypes = [POINTER(lv_obj_t)]
    lv_obj_move_background.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 405
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_pos", "cdecl"):
        continue
    lv_obj_set_pos = _lib.get("lv_obj_set_pos", "cdecl")
    lv_obj_set_pos.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t]
    lv_obj_set_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 412
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_x", "cdecl"):
        continue
    lv_obj_set_x = _lib.get("lv_obj_set_x", "cdecl")
    lv_obj_set_x.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_x.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 419
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_y", "cdecl"):
        continue
    lv_obj_set_y = _lib.get("lv_obj_set_y", "cdecl")
    lv_obj_set_y.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_y.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 427
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_size", "cdecl"):
        continue
    lv_obj_set_size = _lib.get("lv_obj_set_size", "cdecl")
    lv_obj_set_size.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t]
    lv_obj_set_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 434
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_width", "cdecl"):
        continue
    lv_obj_set_width = _lib.get("lv_obj_set_width", "cdecl")
    lv_obj_set_width.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_width.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 441
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_height", "cdecl"):
        continue
    lv_obj_set_height = _lib.get("lv_obj_set_height", "cdecl")
    lv_obj_set_height.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_height.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 448
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_width_fit", "cdecl"):
        continue
    lv_obj_set_width_fit = _lib.get("lv_obj_set_width_fit", "cdecl")
    lv_obj_set_width_fit.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_width_fit.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 455
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_height_fit", "cdecl"):
        continue
    lv_obj_set_height_fit = _lib.get("lv_obj_set_height_fit", "cdecl")
    lv_obj_set_height_fit.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_height_fit.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 463
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_width_margin", "cdecl"):
        continue
    lv_obj_set_width_margin = _lib.get("lv_obj_set_width_margin", "cdecl")
    lv_obj_set_width_margin.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_width_margin.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 471
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_height_margin", "cdecl"):
        continue
    lv_obj_set_height_margin = _lib.get("lv_obj_set_height_margin", "cdecl")
    lv_obj_set_height_margin.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_obj_set_height_margin.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 481
for _lib in _libs.values():
    if not _lib.has("lv_obj_align", "cdecl"):
        continue
    lv_obj_align = _lib.get("lv_obj_align", "cdecl")
    lv_obj_align.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t, lv_coord_t]
    lv_obj_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 490
for _lib in _libs.values():
    if not _lib.has("lv_obj_align_x", "cdecl"):
        continue
    lv_obj_align_x = _lib.get("lv_obj_align_x", "cdecl")
    lv_obj_align_x.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t]
    lv_obj_align_x.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 499
for _lib in _libs.values():
    if not _lib.has("lv_obj_align_y", "cdecl"):
        continue
    lv_obj_align_y = _lib.get("lv_obj_align_y", "cdecl")
    lv_obj_align_y.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t]
    lv_obj_align_y.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 509
for _lib in _libs.values():
    if not _lib.has("lv_obj_align_mid", "cdecl"):
        continue
    lv_obj_align_mid = _lib.get("lv_obj_align_mid", "cdecl")
    lv_obj_align_mid.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t, lv_coord_t]
    lv_obj_align_mid.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 518
for _lib in _libs.values():
    if not _lib.has("lv_obj_align_mid_x", "cdecl"):
        continue
    lv_obj_align_mid_x = _lib.get("lv_obj_align_mid_x", "cdecl")
    lv_obj_align_mid_x.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t]
    lv_obj_align_mid_x.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 527
for _lib in _libs.values():
    if not _lib.has("lv_obj_align_mid_y", "cdecl"):
        continue
    lv_obj_align_mid_y = _lib.get("lv_obj_align_mid_y", "cdecl")
    lv_obj_align_mid_y.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_align_t, lv_coord_t]
    lv_obj_align_mid_y.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 533
for _lib in _libs.values():
    if not _lib.has("lv_obj_realign", "cdecl"):
        continue
    lv_obj_realign = _lib.get("lv_obj_realign", "cdecl")
    lv_obj_realign.argtypes = [POINTER(lv_obj_t)]
    lv_obj_realign.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 541
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_auto_realign", "cdecl"):
        continue
    lv_obj_set_auto_realign = _lib.get("lv_obj_set_auto_realign", "cdecl")
    lv_obj_set_auto_realign.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_auto_realign.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 551
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_ext_click_area", "cdecl"):
        continue
    lv_obj_set_ext_click_area = _lib.get("lv_obj_set_ext_click_area", "cdecl")
    lv_obj_set_ext_click_area.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t]
    lv_obj_set_ext_click_area.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 564
for _lib in _libs.values():
    if not _lib.has("lv_obj_add_style", "cdecl"):
        continue
    lv_obj_add_style = _lib.get("lv_obj_add_style", "cdecl")
    lv_obj_add_style.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_style_t)]
    lv_obj_add_style.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 573
for _lib in _libs.values():
    if not _lib.has("lv_obj_remove_style", "cdecl"):
        continue
    lv_obj_remove_style = _lib.get("lv_obj_remove_style", "cdecl")
    lv_obj_remove_style.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_style_t)]
    lv_obj_remove_style.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 583
for _lib in _libs.values():
    if not _lib.has("lv_obj_clean_style_list", "cdecl"):
        continue
    lv_obj_clean_style_list = _lib.get("lv_obj_clean_style_list", "cdecl")
    lv_obj_clean_style_list.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_clean_style_list.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 593
for _lib in _libs.values():
    if not _lib.has("lv_obj_reset_style_list", "cdecl"):
        continue
    lv_obj_reset_style_list = _lib.get("lv_obj_reset_style_list", "cdecl")
    lv_obj_reset_style_list.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_reset_style_list.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 600
for _lib in _libs.values():
    if not _lib.has("lv_obj_refresh_style", "cdecl"):
        continue
    lv_obj_refresh_style = _lib.get("lv_obj_refresh_style", "cdecl")
    lv_obj_refresh_style.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    lv_obj_refresh_style.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 607
for _lib in _libs.values():
    if not _lib.has("lv_obj_report_style_mod", "cdecl"):
        continue
    lv_obj_report_style_mod = _lib.get("lv_obj_report_style_mod", "cdecl")
    lv_obj_report_style_mod.argtypes = [POINTER(lv_style_t)]
    lv_obj_report_style_mod.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 621
for _lib in _libs.values():
    if not _lib.has("_lv_obj_set_style_local_color", "cdecl"):
        continue
    _lv_obj_set_style_local_color = _lib.get("_lv_obj_set_style_local_color", "cdecl")
    _lv_obj_set_style_local_color.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t, lv_color_t]
    _lv_obj_set_style_local_color.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 635
for _lib in _libs.values():
    if not _lib.has("_lv_obj_set_style_local_int", "cdecl"):
        continue
    _lv_obj_set_style_local_int = _lib.get("_lv_obj_set_style_local_int", "cdecl")
    _lv_obj_set_style_local_int.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t, lv_style_int_t]
    _lv_obj_set_style_local_int.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 649
for _lib in _libs.values():
    if not _lib.has("_lv_obj_set_style_local_opa", "cdecl"):
        continue
    _lv_obj_set_style_local_opa = _lib.get("_lv_obj_set_style_local_opa", "cdecl")
    _lv_obj_set_style_local_opa.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t, lv_opa_t]
    _lv_obj_set_style_local_opa.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 663
for _lib in _libs.values():
    if not _lib.has("_lv_obj_set_style_local_ptr", "cdecl"):
        continue
    _lv_obj_set_style_local_ptr = _lib.get("_lv_obj_set_style_local_ptr", "cdecl")
    _lv_obj_set_style_local_ptr.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t, POINTER(None)]
    _lv_obj_set_style_local_ptr.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 676
for _lib in _libs.values():
    if not _lib.has("lv_obj_remove_style_local_prop", "cdecl"):
        continue
    lv_obj_remove_style_local_prop = _lib.get("lv_obj_remove_style_local_prop", "cdecl")
    lv_obj_remove_style_local_prop.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    lv_obj_remove_style_local_prop.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 683
for _lib in _libs.values():
    if not _lib.has("_lv_obj_disable_style_caching", "cdecl"):
        continue
    _lv_obj_disable_style_caching = _lib.get("_lv_obj_disable_style_caching", "cdecl")
    _lv_obj_disable_style_caching.argtypes = [POINTER(lv_obj_t), c_bool]
    _lv_obj_disable_style_caching.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 694
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_hidden", "cdecl"):
        continue
    lv_obj_set_hidden = _lib.get("lv_obj_set_hidden", "cdecl")
    lv_obj_set_hidden.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_hidden.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 701
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_adv_hittest", "cdecl"):
        continue
    lv_obj_set_adv_hittest = _lib.get("lv_obj_set_adv_hittest", "cdecl")
    lv_obj_set_adv_hittest.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_adv_hittest.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 708
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_click", "cdecl"):
        continue
    lv_obj_set_click = _lib.get("lv_obj_set_click", "cdecl")
    lv_obj_set_click.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_click.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 716
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_top", "cdecl"):
        continue
    lv_obj_set_top = _lib.get("lv_obj_set_top", "cdecl")
    lv_obj_set_top.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_top.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 723
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_drag", "cdecl"):
        continue
    lv_obj_set_drag = _lib.get("lv_obj_set_drag", "cdecl")
    lv_obj_set_drag.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_drag.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 730
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_drag_dir", "cdecl"):
        continue
    lv_obj_set_drag_dir = _lib.get("lv_obj_set_drag_dir", "cdecl")
    lv_obj_set_drag_dir.argtypes = [POINTER(lv_obj_t), lv_drag_dir_t]
    lv_obj_set_drag_dir.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 737
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_drag_throw", "cdecl"):
        continue
    lv_obj_set_drag_throw = _lib.get("lv_obj_set_drag_throw", "cdecl")
    lv_obj_set_drag_throw.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_drag_throw.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 745
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_drag_parent", "cdecl"):
        continue
    lv_obj_set_drag_parent = _lib.get("lv_obj_set_drag_parent", "cdecl")
    lv_obj_set_drag_parent.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_drag_parent.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 753
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_focus_parent", "cdecl"):
        continue
    lv_obj_set_focus_parent = _lib.get("lv_obj_set_focus_parent", "cdecl")
    lv_obj_set_focus_parent.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_focus_parent.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 761
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_gesture_parent", "cdecl"):
        continue
    lv_obj_set_gesture_parent = _lib.get("lv_obj_set_gesture_parent", "cdecl")
    lv_obj_set_gesture_parent.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_gesture_parent.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 768
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_parent_event", "cdecl"):
        continue
    lv_obj_set_parent_event = _lib.get("lv_obj_set_parent_event", "cdecl")
    lv_obj_set_parent_event.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_obj_set_parent_event.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 776
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_base_dir", "cdecl"):
        continue
    lv_obj_set_base_dir = _lib.get("lv_obj_set_base_dir", "cdecl")
    lv_obj_set_base_dir.argtypes = [POINTER(lv_obj_t), lv_bidi_dir_t]
    lv_obj_set_base_dir.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 783
for _lib in _libs.values():
    if not _lib.has("lv_obj_add_protect", "cdecl"):
        continue
    lv_obj_add_protect = _lib.get("lv_obj_add_protect", "cdecl")
    lv_obj_add_protect.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_add_protect.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 790
for _lib in _libs.values():
    if not _lib.has("lv_obj_clear_protect", "cdecl"):
        continue
    lv_obj_clear_protect = _lib.get("lv_obj_clear_protect", "cdecl")
    lv_obj_clear_protect.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_clear_protect.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 799
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_state", "cdecl"):
        continue
    lv_obj_set_state = _lib.get("lv_obj_set_state", "cdecl")
    lv_obj_set_state.argtypes = [POINTER(lv_obj_t), lv_state_t]
    lv_obj_set_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 808
for _lib in _libs.values():
    if not _lib.has("lv_obj_add_state", "cdecl"):
        continue
    lv_obj_add_state = _lib.get("lv_obj_add_state", "cdecl")
    lv_obj_add_state.argtypes = [POINTER(lv_obj_t), lv_state_t]
    lv_obj_add_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 817
for _lib in _libs.values():
    if not _lib.has("lv_obj_clear_state", "cdecl"):
        continue
    lv_obj_clear_state = _lib.get("lv_obj_clear_state", "cdecl")
    lv_obj_clear_state.argtypes = [POINTER(lv_obj_t), lv_state_t]
    lv_obj_clear_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 825
for _lib in _libs.values():
    if not _lib.has("lv_obj_finish_transitions", "cdecl"):
        continue
    lv_obj_finish_transitions = _lib.get("lv_obj_finish_transitions", "cdecl")
    lv_obj_finish_transitions.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_finish_transitions.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 834
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_event_cb", "cdecl"):
        continue
    lv_obj_set_event_cb = _lib.get("lv_obj_set_event_cb", "cdecl")
    lv_obj_set_event_cb.argtypes = [POINTER(lv_obj_t), lv_event_cb_t]
    lv_obj_set_event_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 843
for _lib in _libs.values():
    if not _lib.has("lv_event_send", "cdecl"):
        continue
    lv_event_send = _lib.get("lv_event_send", "cdecl")
    lv_event_send.argtypes = [POINTER(lv_obj_t), lv_event_t, POINTER(None)]
    lv_event_send.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 850
for _lib in _libs.values():
    if not _lib.has("lv_event_send_refresh", "cdecl"):
        continue
    lv_event_send_refresh = _lib.get("lv_event_send_refresh", "cdecl")
    lv_event_send_refresh.argtypes = [POINTER(lv_obj_t)]
    lv_event_send_refresh.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 856
for _lib in _libs.values():
    if not _lib.has("lv_event_send_refresh_recursive", "cdecl"):
        continue
    lv_event_send_refresh_recursive = _lib.get("lv_event_send_refresh_recursive", "cdecl")
    lv_event_send_refresh_recursive.argtypes = [POINTER(lv_obj_t)]
    lv_event_send_refresh_recursive.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 868
for _lib in _libs.values():
    if not _lib.has("lv_event_send_func", "cdecl"):
        continue
    lv_event_send_func = _lib.get("lv_event_send_func", "cdecl")
    lv_event_send_func.argtypes = [lv_event_cb_t, POINTER(lv_obj_t), lv_event_t, POINTER(None)]
    lv_event_send_func.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 874
for _lib in _libs.values():
    if not _lib.has("lv_event_get_data", "cdecl"):
        continue
    lv_event_get_data = _lib.get("lv_event_get_data", "cdecl")
    lv_event_get_data.argtypes = []
    lv_event_get_data.restype = POINTER(c_ubyte)
    lv_event_get_data.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 882
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_signal_cb", "cdecl"):
        continue
    lv_obj_set_signal_cb = _lib.get("lv_obj_set_signal_cb", "cdecl")
    lv_obj_set_signal_cb.argtypes = [POINTER(lv_obj_t), lv_signal_cb_t]
    lv_obj_set_signal_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 890
for _lib in _libs.values():
    if not _lib.has("lv_signal_send", "cdecl"):
        continue
    lv_signal_send = _lib.get("lv_signal_send", "cdecl")
    lv_signal_send.argtypes = [POINTER(lv_obj_t), lv_signal_t, POINTER(None)]
    lv_signal_send.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 897
for _lib in _libs.values():
    if not _lib.has("lv_obj_set_design_cb", "cdecl"):
        continue
    lv_obj_set_design_cb = _lib.get("lv_obj_set_design_cb", "cdecl")
    lv_obj_set_design_cb.argtypes = [POINTER(lv_obj_t), lv_design_cb_t]
    lv_obj_set_design_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 909
for _lib in _libs.values():
    if not _lib.has("lv_obj_allocate_ext_attr", "cdecl"):
        continue
    lv_obj_allocate_ext_attr = _lib.get("lv_obj_allocate_ext_attr", "cdecl")
    lv_obj_allocate_ext_attr.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_obj_allocate_ext_attr.restype = POINTER(c_ubyte)
    lv_obj_allocate_ext_attr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 916
for _lib in _libs.values():
    if not _lib.has("lv_obj_refresh_ext_draw_pad", "cdecl"):
        continue
    lv_obj_refresh_ext_draw_pad = _lib.get("lv_obj_refresh_ext_draw_pad", "cdecl")
    lv_obj_refresh_ext_draw_pad.argtypes = [POINTER(lv_obj_t)]
    lv_obj_refresh_ext_draw_pad.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 927
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_screen", "cdecl"):
        continue
    lv_obj_get_screen = _lib.get("lv_obj_get_screen", "cdecl")
    lv_obj_get_screen.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_screen.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 933
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_disp", "cdecl"):
        continue
    lv_obj_get_disp = _lib.get("lv_obj_get_disp", "cdecl")
    lv_obj_get_disp.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_disp.restype = POINTER(lv_disp_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 944
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_parent", "cdecl"):
        continue
    lv_obj_get_parent = _lib.get("lv_obj_get_parent", "cdecl")
    lv_obj_get_parent.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_parent.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 953
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_child", "cdecl"):
        continue
    lv_obj_get_child = _lib.get("lv_obj_get_child", "cdecl")
    lv_obj_get_child.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_obj_get_child.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 962
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_child_back", "cdecl"):
        continue
    lv_obj_get_child_back = _lib.get("lv_obj_get_child_back", "cdecl")
    lv_obj_get_child_back.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_obj_get_child_back.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 969
for _lib in _libs.values():
    if not _lib.has("lv_obj_count_children", "cdecl"):
        continue
    lv_obj_count_children = _lib.get("lv_obj_count_children", "cdecl")
    lv_obj_count_children.argtypes = [POINTER(lv_obj_t)]
    lv_obj_count_children.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 975
for _lib in _libs.values():
    if not _lib.has("lv_obj_count_children_recursive", "cdecl"):
        continue
    lv_obj_count_children_recursive = _lib.get("lv_obj_count_children_recursive", "cdecl")
    lv_obj_count_children_recursive.argtypes = [POINTER(lv_obj_t)]
    lv_obj_count_children_recursive.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 986
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_coords", "cdecl"):
        continue
    lv_obj_get_coords = _lib.get("lv_obj_get_coords", "cdecl")
    lv_obj_get_coords.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t)]
    lv_obj_get_coords.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 993
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_inner_coords", "cdecl"):
        continue
    lv_obj_get_inner_coords = _lib.get("lv_obj_get_inner_coords", "cdecl")
    lv_obj_get_inner_coords.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t)]
    lv_obj_get_inner_coords.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1000
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_x", "cdecl"):
        continue
    lv_obj_get_x = _lib.get("lv_obj_get_x", "cdecl")
    lv_obj_get_x.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_x.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1007
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_y", "cdecl"):
        continue
    lv_obj_get_y = _lib.get("lv_obj_get_y", "cdecl")
    lv_obj_get_y.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_y.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1014
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_width", "cdecl"):
        continue
    lv_obj_get_width = _lib.get("lv_obj_get_width", "cdecl")
    lv_obj_get_width.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_width.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1021
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_height", "cdecl"):
        continue
    lv_obj_get_height = _lib.get("lv_obj_get_height", "cdecl")
    lv_obj_get_height.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_height.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1028
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_width_fit", "cdecl"):
        continue
    lv_obj_get_width_fit = _lib.get("lv_obj_get_width_fit", "cdecl")
    lv_obj_get_width_fit.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_width_fit.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1035
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_height_fit", "cdecl"):
        continue
    lv_obj_get_height_fit = _lib.get("lv_obj_get_height_fit", "cdecl")
    lv_obj_get_height_fit.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_height_fit.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1043
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_height_margin", "cdecl"):
        continue
    lv_obj_get_height_margin = _lib.get("lv_obj_get_height_margin", "cdecl")
    lv_obj_get_height_margin.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_height_margin.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1051
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_width_margin", "cdecl"):
        continue
    lv_obj_get_width_margin = _lib.get("lv_obj_get_width_margin", "cdecl")
    lv_obj_get_width_margin.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_width_margin.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1064
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_width_grid", "cdecl"):
        continue
    lv_obj_get_width_grid = _lib.get("lv_obj_get_width_grid", "cdecl")
    lv_obj_get_width_grid.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_obj_get_width_grid.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1077
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_height_grid", "cdecl"):
        continue
    lv_obj_get_height_grid = _lib.get("lv_obj_get_height_grid", "cdecl")
    lv_obj_get_height_grid.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_obj_get_height_grid.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1084
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_auto_realign", "cdecl"):
        continue
    lv_obj_get_auto_realign = _lib.get("lv_obj_get_auto_realign", "cdecl")
    lv_obj_get_auto_realign.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_auto_realign.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1091
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_click_pad_left", "cdecl"):
        continue
    lv_obj_get_ext_click_pad_left = _lib.get("lv_obj_get_ext_click_pad_left", "cdecl")
    lv_obj_get_ext_click_pad_left.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_click_pad_left.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1098
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_click_pad_right", "cdecl"):
        continue
    lv_obj_get_ext_click_pad_right = _lib.get("lv_obj_get_ext_click_pad_right", "cdecl")
    lv_obj_get_ext_click_pad_right.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_click_pad_right.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1105
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_click_pad_top", "cdecl"):
        continue
    lv_obj_get_ext_click_pad_top = _lib.get("lv_obj_get_ext_click_pad_top", "cdecl")
    lv_obj_get_ext_click_pad_top.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_click_pad_top.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1112
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_click_pad_bottom", "cdecl"):
        continue
    lv_obj_get_ext_click_pad_bottom = _lib.get("lv_obj_get_ext_click_pad_bottom", "cdecl")
    lv_obj_get_ext_click_pad_bottom.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_click_pad_bottom.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1119
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_draw_pad", "cdecl"):
        continue
    lv_obj_get_ext_draw_pad = _lib.get("lv_obj_get_ext_draw_pad", "cdecl")
    lv_obj_get_ext_draw_pad.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_draw_pad.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1132
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_style_list", "cdecl"):
        continue
    lv_obj_get_style_list = _lib.get("lv_obj_get_style_list", "cdecl")
    lv_obj_get_style_list.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_get_style_list.restype = POINTER(lv_style_list_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1148
for _lib in _libs.values():
    if not _lib.has("_lv_obj_get_style_int", "cdecl"):
        continue
    _lv_obj_get_style_int = _lib.get("_lv_obj_get_style_int", "cdecl")
    _lv_obj_get_style_int.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    _lv_obj_get_style_int.restype = lv_style_int_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1164
for _lib in _libs.values():
    if not _lib.has("_lv_obj_get_style_color", "cdecl"):
        continue
    _lv_obj_get_style_color = _lib.get("_lv_obj_get_style_color", "cdecl")
    _lv_obj_get_style_color.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    _lv_obj_get_style_color.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1180
for _lib in _libs.values():
    if not _lib.has("_lv_obj_get_style_opa", "cdecl"):
        continue
    _lv_obj_get_style_opa = _lib.get("_lv_obj_get_style_opa", "cdecl")
    _lv_obj_get_style_opa.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    _lv_obj_get_style_opa.restype = lv_opa_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1196
for _lib in _libs.values():
    if not _lib.has("_lv_obj_get_style_ptr", "cdecl"):
        continue
    _lv_obj_get_style_ptr = _lib.get("_lv_obj_get_style_ptr", "cdecl")
    _lv_obj_get_style_ptr.argtypes = [POINTER(lv_obj_t), c_uint8, lv_style_property_t]
    _lv_obj_get_style_ptr.restype = POINTER(c_ubyte)
    _lv_obj_get_style_ptr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1205
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_local_style", "cdecl"):
        continue
    lv_obj_get_local_style = _lib.get("lv_obj_get_local_style", "cdecl")
    lv_obj_get_local_style.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_get_local_style.restype = POINTER(lv_style_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1218
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_hidden", "cdecl"):
        continue
    lv_obj_get_hidden = _lib.get("lv_obj_get_hidden", "cdecl")
    lv_obj_get_hidden.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_hidden.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1225
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_adv_hittest", "cdecl"):
        continue
    lv_obj_get_adv_hittest = _lib.get("lv_obj_get_adv_hittest", "cdecl")
    lv_obj_get_adv_hittest.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_adv_hittest.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1232
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_click", "cdecl"):
        continue
    lv_obj_get_click = _lib.get("lv_obj_get_click", "cdecl")
    lv_obj_get_click.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_click.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1239
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_top", "cdecl"):
        continue
    lv_obj_get_top = _lib.get("lv_obj_get_top", "cdecl")
    lv_obj_get_top.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_top.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1246
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_drag", "cdecl"):
        continue
    lv_obj_get_drag = _lib.get("lv_obj_get_drag", "cdecl")
    lv_obj_get_drag.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_drag.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1253
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_drag_dir", "cdecl"):
        continue
    lv_obj_get_drag_dir = _lib.get("lv_obj_get_drag_dir", "cdecl")
    lv_obj_get_drag_dir.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_drag_dir.restype = lv_drag_dir_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1260
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_drag_throw", "cdecl"):
        continue
    lv_obj_get_drag_throw = _lib.get("lv_obj_get_drag_throw", "cdecl")
    lv_obj_get_drag_throw.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_drag_throw.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1267
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_drag_parent", "cdecl"):
        continue
    lv_obj_get_drag_parent = _lib.get("lv_obj_get_drag_parent", "cdecl")
    lv_obj_get_drag_parent.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_drag_parent.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1274
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_focus_parent", "cdecl"):
        continue
    lv_obj_get_focus_parent = _lib.get("lv_obj_get_focus_parent", "cdecl")
    lv_obj_get_focus_parent.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_focus_parent.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1281
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_parent_event", "cdecl"):
        continue
    lv_obj_get_parent_event = _lib.get("lv_obj_get_parent_event", "cdecl")
    lv_obj_get_parent_event.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_parent_event.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1288
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_gesture_parent", "cdecl"):
        continue
    lv_obj_get_gesture_parent = _lib.get("lv_obj_get_gesture_parent", "cdecl")
    lv_obj_get_gesture_parent.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_gesture_parent.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1290
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_base_dir", "cdecl"):
        continue
    lv_obj_get_base_dir = _lib.get("lv_obj_get_base_dir", "cdecl")
    lv_obj_get_base_dir.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_base_dir.restype = lv_bidi_dir_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1297
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_protect", "cdecl"):
        continue
    lv_obj_get_protect = _lib.get("lv_obj_get_protect", "cdecl")
    lv_obj_get_protect.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_protect.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1305
for _lib in _libs.values():
    if not _lib.has("lv_obj_is_protected", "cdecl"):
        continue
    lv_obj_is_protected = _lib.get("lv_obj_is_protected", "cdecl")
    lv_obj_is_protected.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_is_protected.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1307
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_state", "cdecl"):
        continue
    lv_obj_get_state = _lib.get("lv_obj_get_state", "cdecl")
    lv_obj_get_state.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_get_state.restype = lv_state_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1314
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_signal_cb", "cdecl"):
        continue
    lv_obj_get_signal_cb = _lib.get("lv_obj_get_signal_cb", "cdecl")
    lv_obj_get_signal_cb.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_signal_cb.restype = lv_signal_cb_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1321
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_design_cb", "cdecl"):
        continue
    lv_obj_get_design_cb = _lib.get("lv_obj_get_design_cb", "cdecl")
    lv_obj_get_design_cb.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_design_cb.restype = lv_design_cb_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1328
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_event_cb", "cdecl"):
        continue
    lv_obj_get_event_cb = _lib.get("lv_obj_get_event_cb", "cdecl")
    lv_obj_get_event_cb.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_event_cb.restype = lv_event_cb_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1342
for _lib in _libs.values():
    if not _lib.has("lv_obj_is_point_on_coords", "cdecl"):
        continue
    lv_obj_is_point_on_coords = _lib.get("lv_obj_is_point_on_coords", "cdecl")
    lv_obj_is_point_on_coords.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_obj_is_point_on_coords.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1350
for _lib in _libs.values():
    if not _lib.has("lv_obj_hittest", "cdecl"):
        continue
    lv_obj_hittest = _lib.get("lv_obj_hittest", "cdecl")
    lv_obj_hittest.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_obj_hittest.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1358
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_ext_attr", "cdecl"):
        continue
    lv_obj_get_ext_attr = _lib.get("lv_obj_get_ext_attr", "cdecl")
    lv_obj_get_ext_attr.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_ext_attr.restype = POINTER(c_ubyte)
    lv_obj_get_ext_attr.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1366
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_type", "cdecl"):
        continue
    lv_obj_get_type = _lib.get("lv_obj_get_type", "cdecl")
    lv_obj_get_type.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_type_t)]
    lv_obj_get_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1397
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_group", "cdecl"):
        continue
    lv_obj_get_group = _lib.get("lv_obj_get_group", "cdecl")
    lv_obj_get_group.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_group.restype = POINTER(c_ubyte)
    lv_obj_get_group.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1404
for _lib in _libs.values():
    if not _lib.has("lv_obj_is_focused", "cdecl"):
        continue
    lv_obj_is_focused = _lib.get("lv_obj_is_focused", "cdecl")
    lv_obj_is_focused.argtypes = [POINTER(lv_obj_t)]
    lv_obj_is_focused.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1411
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_focused_obj", "cdecl"):
        continue
    lv_obj_get_focused_obj = _lib.get("lv_obj_get_focused_obj", "cdecl")
    lv_obj_get_focused_obj.argtypes = [POINTER(lv_obj_t)]
    lv_obj_get_focused_obj.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1423
for _lib in _libs.values():
    if not _lib.has("lv_obj_handle_get_type_signal", "cdecl"):
        continue
    lv_obj_handle_get_type_signal = _lib.get("lv_obj_handle_get_type_signal", "cdecl")
    lv_obj_handle_get_type_signal.argtypes = [POINTER(lv_obj_type_t), String]
    lv_obj_handle_get_type_signal.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1433
for _lib in _libs.values():
    if not _lib.has("lv_obj_init_draw_rect_dsc", "cdecl"):
        continue
    lv_obj_init_draw_rect_dsc = _lib.get("lv_obj_init_draw_rect_dsc", "cdecl")
    lv_obj_init_draw_rect_dsc.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_draw_rect_dsc_t)]
    lv_obj_init_draw_rect_dsc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1435
for _lib in _libs.values():
    if not _lib.has("lv_obj_init_draw_label_dsc", "cdecl"):
        continue
    lv_obj_init_draw_label_dsc = _lib.get("lv_obj_init_draw_label_dsc", "cdecl")
    lv_obj_init_draw_label_dsc.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_draw_label_dsc_t)]
    lv_obj_init_draw_label_dsc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1437
for _lib in _libs.values():
    if not _lib.has("lv_obj_init_draw_img_dsc", "cdecl"):
        continue
    lv_obj_init_draw_img_dsc = _lib.get("lv_obj_init_draw_img_dsc", "cdecl")
    lv_obj_init_draw_img_dsc.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_draw_img_dsc_t)]
    lv_obj_init_draw_img_dsc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1439
for _lib in _libs.values():
    if not _lib.has("lv_obj_init_draw_line_dsc", "cdecl"):
        continue
    lv_obj_init_draw_line_dsc = _lib.get("lv_obj_init_draw_line_dsc", "cdecl")
    lv_obj_init_draw_line_dsc.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_draw_line_dsc_t)]
    lv_obj_init_draw_line_dsc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1446
for _lib in _libs.values():
    if not _lib.has("lv_obj_get_draw_rect_ext_pad_size", "cdecl"):
        continue
    lv_obj_get_draw_rect_ext_pad_size = _lib.get("lv_obj_get_draw_rect_ext_pad_size", "cdecl")
    lv_obj_get_draw_rect_ext_pad_size.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_obj_get_draw_rect_ext_pad_size.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1454
for _lib in _libs.values():
    if not _lib.has("lv_obj_fade_in", "cdecl"):
        continue
    lv_obj_fade_in = _lib.get("lv_obj_fade_in", "cdecl")
    lv_obj_fade_in.argtypes = [POINTER(lv_obj_t), c_uint32, c_uint32]
    lv_obj_fade_in.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1462
for _lib in _libs.values():
    if not _lib.has("lv_obj_fade_out", "cdecl"):
        continue
    lv_obj_fade_out = _lib.get("lv_obj_fade_out", "cdecl")
    lv_obj_fade_out.argtypes = [POINTER(lv_obj_t), c_uint32, c_uint32]
    lv_obj_fade_out.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1470
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_obj_type", "cdecl"):
        continue
    lv_debug_check_obj_type = _lib.get("lv_debug_check_obj_type", "cdecl")
    lv_debug_check_obj_type.argtypes = [POINTER(lv_obj_t), String]
    lv_debug_check_obj_type.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1478
for _lib in _libs.values():
    if not _lib.has("lv_debug_check_obj_valid", "cdecl"):
        continue
    lv_debug_check_obj_valid = _lib.get("lv_debug_check_obj_valid", "cdecl")
    lv_debug_check_obj_valid.argtypes = [POINTER(lv_obj_t)]
    lv_debug_check_obj_valid.restype = c_bool
    break

enum_anon_89 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_UP = 17# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_DOWN = 18# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_RIGHT = 19# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_LEFT = 20# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_ESC = 27# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_DEL = 127# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_BACKSPACE = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_ENTER = 10# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_NEXT = 9# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_PREV = 11# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_HOME = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

LV_KEY_END = 3# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 25

lv_key_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 39

lv_group_style_mod_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_group_t), POINTER(lv_style_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 47

lv_group_focus_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_group_t))# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 48

struct__lv_group_t.__slots__ = [
    'obj_ll',
    'obj_focus',
    'focus_cb',
    'frozen',
    'editing',
    'click_focus',
    'refocus_policy',
    'wrap',
]
struct__lv_group_t._fields_ = [
    ('obj_ll', lv_ll_t),
    ('obj_focus', POINTER(POINTER(lv_obj_t))),
    ('focus_cb', lv_group_focus_cb_t),
    ('frozen', c_uint8, 1),
    ('editing', c_uint8, 1),
    ('click_focus', c_uint8, 1),
    ('refocus_policy', c_uint8, 1),
    ('wrap', c_uint8, 1),
]

lv_group_t = struct__lv_group_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 71

enum_anon_90 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 73

LV_GROUP_REFOCUS_POLICY_NEXT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 73

LV_GROUP_REFOCUS_POLICY_PREV = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 73

lv_group_refocus_policy_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 74

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 84
for _lib in _libs.values():
    if not _lib.has("_lv_group_init", "cdecl"):
        continue
    _lv_group_init = _lib.get("_lv_group_init", "cdecl")
    _lv_group_init.argtypes = []
    _lv_group_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 90
for _lib in _libs.values():
    if not _lib.has("lv_group_create", "cdecl"):
        continue
    lv_group_create = _lib.get("lv_group_create", "cdecl")
    lv_group_create.argtypes = []
    lv_group_create.restype = POINTER(lv_group_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 96
for _lib in _libs.values():
    if not _lib.has("lv_group_del", "cdecl"):
        continue
    lv_group_del = _lib.get("lv_group_del", "cdecl")
    lv_group_del.argtypes = [POINTER(lv_group_t)]
    lv_group_del.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 103
for _lib in _libs.values():
    if not _lib.has("lv_group_add_obj", "cdecl"):
        continue
    lv_group_add_obj = _lib.get("lv_group_add_obj", "cdecl")
    lv_group_add_obj.argtypes = [POINTER(lv_group_t), POINTER(lv_obj_t)]
    lv_group_add_obj.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_group_remove_obj", "cdecl"):
        continue
    lv_group_remove_obj = _lib.get("lv_group_remove_obj", "cdecl")
    lv_group_remove_obj.argtypes = [POINTER(lv_obj_t)]
    lv_group_remove_obj.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 115
for _lib in _libs.values():
    if not _lib.has("lv_group_remove_all_objs", "cdecl"):
        continue
    lv_group_remove_all_objs = _lib.get("lv_group_remove_all_objs", "cdecl")
    lv_group_remove_all_objs.argtypes = [POINTER(lv_group_t)]
    lv_group_remove_all_objs.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 121
for _lib in _libs.values():
    if not _lib.has("lv_group_focus_obj", "cdecl"):
        continue
    lv_group_focus_obj = _lib.get("lv_group_focus_obj", "cdecl")
    lv_group_focus_obj.argtypes = [POINTER(lv_obj_t)]
    lv_group_focus_obj.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_group_focus_next", "cdecl"):
        continue
    lv_group_focus_next = _lib.get("lv_group_focus_next", "cdecl")
    lv_group_focus_next.argtypes = [POINTER(lv_group_t)]
    lv_group_focus_next.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 133
for _lib in _libs.values():
    if not _lib.has("lv_group_focus_prev", "cdecl"):
        continue
    lv_group_focus_prev = _lib.get("lv_group_focus_prev", "cdecl")
    lv_group_focus_prev.argtypes = [POINTER(lv_group_t)]
    lv_group_focus_prev.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 140
for _lib in _libs.values():
    if not _lib.has("lv_group_focus_freeze", "cdecl"):
        continue
    lv_group_focus_freeze = _lib.get("lv_group_focus_freeze", "cdecl")
    lv_group_focus_freeze.argtypes = [POINTER(lv_group_t), c_bool]
    lv_group_focus_freeze.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 148
for _lib in _libs.values():
    if not _lib.has("lv_group_send_data", "cdecl"):
        continue
    lv_group_send_data = _lib.get("lv_group_send_data", "cdecl")
    lv_group_send_data.argtypes = [POINTER(lv_group_t), c_uint32]
    lv_group_send_data.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 155
for _lib in _libs.values():
    if not _lib.has("lv_group_set_focus_cb", "cdecl"):
        continue
    lv_group_set_focus_cb = _lib.get("lv_group_set_focus_cb", "cdecl")
    lv_group_set_focus_cb.argtypes = [POINTER(lv_group_t), lv_group_focus_cb_t]
    lv_group_set_focus_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 163
for _lib in _libs.values():
    if not _lib.has("lv_group_set_refocus_policy", "cdecl"):
        continue
    lv_group_set_refocus_policy = _lib.get("lv_group_set_refocus_policy", "cdecl")
    lv_group_set_refocus_policy.argtypes = [POINTER(lv_group_t), lv_group_refocus_policy_t]
    lv_group_set_refocus_policy.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 170
for _lib in _libs.values():
    if not _lib.has("lv_group_set_editing", "cdecl"):
        continue
    lv_group_set_editing = _lib.get("lv_group_set_editing", "cdecl")
    lv_group_set_editing.argtypes = [POINTER(lv_group_t), c_bool]
    lv_group_set_editing.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 177
for _lib in _libs.values():
    if not _lib.has("lv_group_set_click_focus", "cdecl"):
        continue
    lv_group_set_click_focus = _lib.get("lv_group_set_click_focus", "cdecl")
    lv_group_set_click_focus.argtypes = [POINTER(lv_group_t), c_bool]
    lv_group_set_click_focus.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 184
for _lib in _libs.values():
    if not _lib.has("lv_group_set_wrap", "cdecl"):
        continue
    lv_group_set_wrap = _lib.get("lv_group_set_wrap", "cdecl")
    lv_group_set_wrap.argtypes = [POINTER(lv_group_t), c_bool]
    lv_group_set_wrap.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 191
for _lib in _libs.values():
    if not _lib.has("lv_group_get_focused", "cdecl"):
        continue
    lv_group_get_focused = _lib.get("lv_group_get_focused", "cdecl")
    lv_group_get_focused.argtypes = [POINTER(lv_group_t)]
    lv_group_get_focused.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 208
for _lib in _libs.values():
    if not _lib.has("lv_group_get_focus_cb", "cdecl"):
        continue
    lv_group_get_focus_cb = _lib.get("lv_group_get_focus_cb", "cdecl")
    lv_group_get_focus_cb.argtypes = [POINTER(lv_group_t)]
    lv_group_get_focus_cb.restype = lv_group_focus_cb_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 215
for _lib in _libs.values():
    if not _lib.has("lv_group_get_editing", "cdecl"):
        continue
    lv_group_get_editing = _lib.get("lv_group_get_editing", "cdecl")
    lv_group_get_editing.argtypes = [POINTER(lv_group_t)]
    lv_group_get_editing.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 222
for _lib in _libs.values():
    if not _lib.has("lv_group_get_click_focus", "cdecl"):
        continue
    lv_group_get_click_focus = _lib.get("lv_group_get_click_focus", "cdecl")
    lv_group_get_click_focus.argtypes = [POINTER(lv_group_t)]
    lv_group_get_click_focus.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_group_get_wrap", "cdecl"):
        continue
    lv_group_get_wrap = _lib.get("lv_group_get_wrap", "cdecl")
    lv_group_get_wrap.argtypes = [POINTER(lv_group_t)]
    lv_group_get_wrap.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 35
for _lib in _libs.values():
    if not _lib.has("_lv_indev_init", "cdecl"):
        continue
    _lv_indev_init = _lib.get("_lv_indev_init", "cdecl")
    _lv_indev_init.argtypes = []
    _lv_indev_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 41
for _lib in _libs.values():
    if not _lib.has("_lv_indev_read_task", "cdecl"):
        continue
    _lv_indev_read_task = _lib.get("_lv_indev_read_task", "cdecl")
    _lv_indev_read_task.argtypes = [POINTER(lv_task_t)]
    _lv_indev_read_task.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 48
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_act", "cdecl"):
        continue
    lv_indev_get_act = _lib.get("lv_indev_get_act", "cdecl")
    lv_indev_get_act.argtypes = []
    lv_indev_get_act.restype = POINTER(lv_indev_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 55
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_type", "cdecl"):
        continue
    lv_indev_get_type = _lib.get("lv_indev_get_type", "cdecl")
    lv_indev_get_type.argtypes = [POINTER(lv_indev_t)]
    lv_indev_get_type.restype = lv_indev_type_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 62
for _lib in _libs.values():
    if not _lib.has("lv_indev_reset", "cdecl"):
        continue
    lv_indev_reset = _lib.get("lv_indev_reset", "cdecl")
    lv_indev_reset.argtypes = [POINTER(lv_indev_t), POINTER(lv_obj_t)]
    lv_indev_reset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 68
for _lib in _libs.values():
    if not _lib.has("lv_indev_reset_long_press", "cdecl"):
        continue
    lv_indev_reset_long_press = _lib.get("lv_indev_reset_long_press", "cdecl")
    lv_indev_reset_long_press.argtypes = [POINTER(lv_indev_t)]
    lv_indev_reset_long_press.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_indev_enable", "cdecl"):
        continue
    lv_indev_enable = _lib.get("lv_indev_enable", "cdecl")
    lv_indev_enable.argtypes = [POINTER(lv_indev_t), c_bool]
    lv_indev_enable.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_indev_set_cursor", "cdecl"):
        continue
    lv_indev_set_cursor = _lib.get("lv_indev_set_cursor", "cdecl")
    lv_indev_set_cursor.argtypes = [POINTER(lv_indev_t), POINTER(lv_obj_t)]
    lv_indev_set_cursor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 90
for _lib in _libs.values():
    if not _lib.has("lv_indev_set_group", "cdecl"):
        continue
    lv_indev_set_group = _lib.get("lv_indev_set_group", "cdecl")
    lv_indev_set_group.argtypes = [POINTER(lv_indev_t), POINTER(lv_group_t)]
    lv_indev_set_group.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 99
for _lib in _libs.values():
    if not _lib.has("lv_indev_set_button_points", "cdecl"):
        continue
    lv_indev_set_button_points = _lib.get("lv_indev_set_button_points", "cdecl")
    lv_indev_set_button_points.argtypes = [POINTER(lv_indev_t), POINTER(lv_point_t)]
    lv_indev_set_button_points.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_point", "cdecl"):
        continue
    lv_indev_get_point = _lib.get("lv_indev_get_point", "cdecl")
    lv_indev_get_point.argtypes = [POINTER(lv_indev_t), POINTER(lv_point_t)]
    lv_indev_get_point.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_gesture_dir", "cdecl"):
        continue
    lv_indev_get_gesture_dir = _lib.get("lv_indev_get_gesture_dir", "cdecl")
    lv_indev_get_gesture_dir.argtypes = [POINTER(lv_indev_t)]
    lv_indev_get_gesture_dir.restype = lv_gesture_dir_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_key", "cdecl"):
        continue
    lv_indev_get_key = _lib.get("lv_indev_get_key", "cdecl")
    lv_indev_get_key.argtypes = [POINTER(lv_indev_t)]
    lv_indev_get_key.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 128
for _lib in _libs.values():
    if not _lib.has("lv_indev_is_dragging", "cdecl"):
        continue
    lv_indev_is_dragging = _lib.get("lv_indev_is_dragging", "cdecl")
    lv_indev_is_dragging.argtypes = [POINTER(lv_indev_t)]
    lv_indev_is_dragging.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 136
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_vect", "cdecl"):
        continue
    lv_indev_get_vect = _lib.get("lv_indev_get_vect", "cdecl")
    lv_indev_get_vect.argtypes = [POINTER(lv_indev_t), POINTER(lv_point_t)]
    lv_indev_get_vect.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 144
for _lib in _libs.values():
    if not _lib.has("lv_indev_finish_drag", "cdecl"):
        continue
    lv_indev_finish_drag = _lib.get("lv_indev_finish_drag", "cdecl")
    lv_indev_finish_drag.argtypes = [POINTER(lv_indev_t)]
    lv_indev_finish_drag.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_indev_wait_release", "cdecl"):
        continue
    lv_indev_wait_release = _lib.get("lv_indev_wait_release", "cdecl")
    lv_indev_wait_release.argtypes = [POINTER(lv_indev_t)]
    lv_indev_wait_release.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 157
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_obj_act", "cdecl"):
        continue
    lv_indev_get_obj_act = _lib.get("lv_indev_get_obj_act", "cdecl")
    lv_indev_get_obj_act.argtypes = []
    lv_indev_get_obj_act.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 165
for _lib in _libs.values():
    if not _lib.has("lv_indev_search_obj", "cdecl"):
        continue
    lv_indev_search_obj = _lib.get("lv_indev_search_obj", "cdecl")
    lv_indev_search_obj.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_indev_search_obj.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_indev.h: 173
for _lib in _libs.values():
    if not _lib.has("lv_indev_get_read_task", "cdecl"):
        continue
    lv_indev_get_read_task = _lib.get("lv_indev_get_read_task", "cdecl")
    lv_indev_get_read_task.argtypes = [POINTER(lv_disp_t)]
    lv_indev_get_read_task.restype = POINTER(lv_task_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 48
for _lib in _libs.values():
    if not _lib.has("_lv_refr_init", "cdecl"):
        continue
    _lv_refr_init = _lib.get("_lv_refr_init", "cdecl")
    _lv_refr_init.argtypes = []
    _lv_refr_init.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 57
for _lib in _libs.values():
    if not _lib.has("lv_refr_now", "cdecl"):
        continue
    lv_refr_now = _lib.get("lv_refr_now", "cdecl")
    lv_refr_now.argtypes = [POINTER(lv_disp_t)]
    lv_refr_now.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 65
for _lib in _libs.values():
    if not _lib.has("_lv_inv_area", "cdecl"):
        continue
    _lv_inv_area = _lib.get("_lv_inv_area", "cdecl")
    _lv_inv_area.argtypes = [POINTER(lv_disp_t), POINTER(lv_area_t)]
    _lv_inv_area.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 71
for _lib in _libs.values():
    if not _lib.has("_lv_refr_get_disp_refreshing", "cdecl"):
        continue
    _lv_refr_get_disp_refreshing = _lib.get("_lv_refr_get_disp_refreshing", "cdecl")
    _lv_refr_get_disp_refreshing.argtypes = []
    _lv_refr_get_disp_refreshing.restype = POINTER(lv_disp_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 79
for _lib in _libs.values():
    if not _lib.has("_lv_refr_set_disp_refreshing", "cdecl"):
        continue
    _lv_refr_set_disp_refreshing = _lib.get("_lv_refr_set_disp_refreshing", "cdecl")
    _lv_refr_set_disp_refreshing.argtypes = [POINTER(lv_disp_t)]
    _lv_refr_set_disp_refreshing.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 93
for _lib in _libs.values():
    if not _lib.has("_lv_disp_refr_task", "cdecl"):
        continue
    _lv_disp_refr_task = _lib.get("_lv_disp_refr_task", "cdecl")
    _lv_disp_refr_task.argtypes = [POINTER(lv_task_t)]
    _lv_disp_refr_task.restype = None
    break

enum_anon_91 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_OVER_LEFT = (LV_SCR_LOAD_ANIM_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_OVER_RIGHT = (LV_SCR_LOAD_ANIM_OVER_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_OVER_TOP = (LV_SCR_LOAD_ANIM_OVER_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_OVER_BOTTOM = (LV_SCR_LOAD_ANIM_OVER_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_MOVE_LEFT = (LV_SCR_LOAD_ANIM_OVER_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_MOVE_RIGHT = (LV_SCR_LOAD_ANIM_MOVE_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_MOVE_TOP = (LV_SCR_LOAD_ANIM_MOVE_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_MOVE_BOTTOM = (LV_SCR_LOAD_ANIM_MOVE_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

LV_SCR_LOAD_ANIM_FADE_ON = (LV_SCR_LOAD_ANIM_MOVE_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

lv_scr_load_anim_t = enum_anon_91# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 38

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 50
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_scr_act", "cdecl"):
        continue
    lv_disp_get_scr_act = _lib.get("lv_disp_get_scr_act", "cdecl")
    lv_disp_get_scr_act.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_scr_act.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 58
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_scr_prev", "cdecl"):
        continue
    lv_disp_get_scr_prev = _lib.get("lv_disp_get_scr_prev", "cdecl")
    lv_disp_get_scr_prev.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_scr_prev.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 64
for _lib in _libs.values():
    if not _lib.has("lv_disp_load_scr", "cdecl"):
        continue
    lv_disp_load_scr = _lib.get("lv_disp_load_scr", "cdecl")
    lv_disp_load_scr.argtypes = [POINTER(lv_obj_t)]
    lv_disp_load_scr.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 71
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_layer_top", "cdecl"):
        continue
    lv_disp_get_layer_top = _lib.get("lv_disp_get_layer_top", "cdecl")
    lv_disp_get_layer_top.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_layer_top.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 79
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_layer_sys", "cdecl"):
        continue
    lv_disp_get_layer_sys = _lib.get("lv_disp_get_layer_sys", "cdecl")
    lv_disp_get_layer_sys.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_layer_sys.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 86
for _lib in _libs.values():
    if not _lib.has("lv_disp_assign_screen", "cdecl"):
        continue
    lv_disp_assign_screen = _lib.get("lv_disp_assign_screen", "cdecl")
    lv_disp_assign_screen.argtypes = [POINTER(lv_disp_t), POINTER(lv_obj_t)]
    lv_disp_assign_screen.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 93
for _lib in _libs.values():
    if not _lib.has("lv_disp_set_bg_color", "cdecl"):
        continue
    lv_disp_set_bg_color = _lib.get("lv_disp_set_bg_color", "cdecl")
    lv_disp_set_bg_color.argtypes = [POINTER(lv_disp_t), lv_color_t]
    lv_disp_set_bg_color.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 100
for _lib in _libs.values():
    if not _lib.has("lv_disp_set_bg_image", "cdecl"):
        continue
    lv_disp_set_bg_image = _lib.get("lv_disp_set_bg_image", "cdecl")
    lv_disp_set_bg_image.argtypes = [POINTER(lv_disp_t), POINTER(None)]
    lv_disp_set_bg_image.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 107
for _lib in _libs.values():
    if not _lib.has("lv_disp_set_bg_opa", "cdecl"):
        continue
    lv_disp_set_bg_opa = _lib.get("lv_disp_set_bg_opa", "cdecl")
    lv_disp_set_bg_opa.argtypes = [POINTER(lv_disp_t), lv_opa_t]
    lv_disp_set_bg_opa.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 119
for _lib in _libs.values():
    if not _lib.has("lv_scr_load_anim", "cdecl"):
        continue
    lv_scr_load_anim = _lib.get("lv_scr_load_anim", "cdecl")
    lv_scr_load_anim.argtypes = [POINTER(lv_obj_t), lv_scr_load_anim_t, c_uint32, c_uint32, c_bool]
    lv_scr_load_anim.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_disp_get_inactive_time", "cdecl"):
        continue
    lv_disp_get_inactive_time = _lib.get("lv_disp_get_inactive_time", "cdecl")
    lv_disp_get_inactive_time.argtypes = [POINTER(lv_disp_t)]
    lv_disp_get_inactive_time.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 133
for _lib in _libs.values():
    if not _lib.has("lv_disp_trig_activity", "cdecl"):
        continue
    lv_disp_trig_activity = _lib.get("lv_disp_trig_activity", "cdecl")
    lv_disp_trig_activity.argtypes = [POINTER(lv_disp_t)]
    lv_disp_trig_activity.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 139
for _lib in _libs.values():
    if not _lib.has("lv_disp_clean_dcache", "cdecl"):
        continue
    lv_disp_clean_dcache = _lib.get("lv_disp_clean_dcache", "cdecl")
    lv_disp_clean_dcache.argtypes = [POINTER(lv_disp_t)]
    lv_disp_clean_dcache.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 147
for _lib in _libs.values():
    if not _lib.has("_lv_disp_get_refr_task", "cdecl"):
        continue
    _lv_disp_get_refr_task = _lib.get("_lv_disp_get_refr_task", "cdecl")
    _lv_disp_get_refr_task.argtypes = [POINTER(lv_disp_t)]
    _lv_disp_get_refr_task.restype = POINTER(lv_task_t)
    break

enum_anon_92 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SCR = (LV_THEME_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_OBJ = (LV_THEME_SCR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_ARC = (LV_THEME_OBJ + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_BAR = (LV_THEME_ARC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_BTN = (LV_THEME_BAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_BTNMATRIX = (LV_THEME_BTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CALENDAR = (LV_THEME_BTNMATRIX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CANVAS = (LV_THEME_CALENDAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CHECKBOX = (LV_THEME_CANVAS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CHART = (LV_THEME_CHECKBOX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CONT = (LV_THEME_CHART + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CPICKER = (LV_THEME_CONT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_DROPDOWN = (LV_THEME_CPICKER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_GAUGE = (LV_THEME_DROPDOWN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_IMAGE = (LV_THEME_GAUGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_IMGBTN = (LV_THEME_IMAGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_KEYBOARD = (LV_THEME_IMGBTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LABEL = (LV_THEME_KEYBOARD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LED = (LV_THEME_LABEL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LINE = (LV_THEME_LED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LIST = (LV_THEME_LINE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LIST_BTN = (LV_THEME_LIST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_LINEMETER = (LV_THEME_LIST_BTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_MSGBOX = (LV_THEME_LINEMETER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_MSGBOX_BTNS = (LV_THEME_MSGBOX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_OBJMASK = (LV_THEME_MSGBOX_BTNS + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_PAGE = (LV_THEME_OBJMASK + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_ROLLER = (LV_THEME_PAGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SLIDER = (LV_THEME_ROLLER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SPINBOX = (LV_THEME_SLIDER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SPINBOX_BTN = (LV_THEME_SPINBOX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SPINNER = (LV_THEME_SPINBOX_BTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_SWITCH = (LV_THEME_SPINNER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_TABLE = (LV_THEME_SWITCH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_TABVIEW = (LV_THEME_TABLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_TABVIEW_PAGE = (LV_THEME_TABVIEW + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_TEXTAREA = (LV_THEME_TABVIEW_PAGE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_TILEVIEW = (LV_THEME_TEXTAREA + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_WIN = (LV_THEME_TILEVIEW + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_WIN_BTN = (LV_THEME_WIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

_LV_THEME_BUILTIN_LAST = (LV_THEME_WIN_BTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

LV_THEME_CUSTOM_START = _LV_THEME_BUILTIN_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

_LV_THEME_CUSTOM_LAST = 65535# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

lv_theme_style_t = enum_anon_92# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 147

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 154
class struct__lv_theme_t(Structure):
    pass

lv_theme_apply_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(struct__lv_theme_t), POINTER(lv_obj_t), lv_theme_style_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 151

lv_theme_apply_xcb_t = CFUNCTYPE(UNCHECKED(None), POINTER(lv_obj_t), lv_theme_style_t)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 152

struct__lv_theme_t.__slots__ = [
    'apply_cb',
    'apply_xcb',
    'base',
    'color_primary',
    'color_secondary',
    'font_small',
    'font_normal',
    'font_subtitle',
    'font_title',
    'flags',
    'user_data',
]
struct__lv_theme_t._fields_ = [
    ('apply_cb', lv_theme_apply_cb_t),
    ('apply_xcb', lv_theme_apply_xcb_t),
    ('base', POINTER(struct__lv_theme_t)),
    ('color_primary', lv_color_t),
    ('color_secondary', lv_color_t),
    ('font_small', POINTER(lv_font_t)),
    ('font_normal', POINTER(lv_font_t)),
    ('font_subtitle', POINTER(lv_font_t)),
    ('font_title', POINTER(lv_font_t)),
    ('flags', c_uint32),
    ('user_data', POINTER(None)),
]

lv_theme_t = struct__lv_theme_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 166

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 177
for _lib in _libs.values():
    if not _lib.has("lv_theme_set_act", "cdecl"):
        continue
    lv_theme_set_act = _lib.get("lv_theme_set_act", "cdecl")
    lv_theme_set_act.argtypes = [POINTER(lv_theme_t)]
    lv_theme_set_act.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 183
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_act", "cdecl"):
        continue
    lv_theme_get_act = _lib.get("lv_theme_get_act", "cdecl")
    lv_theme_get_act.argtypes = []
    lv_theme_get_act.restype = POINTER(lv_theme_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 190
for _lib in _libs.values():
    if not _lib.has("lv_theme_apply", "cdecl"):
        continue
    lv_theme_apply = _lib.get("lv_theme_apply", "cdecl")
    lv_theme_apply.argtypes = [POINTER(lv_obj_t), lv_theme_style_t]
    lv_theme_apply.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 198
for _lib in _libs.values():
    if not _lib.has("lv_theme_copy", "cdecl"):
        continue
    lv_theme_copy = _lib.get("lv_theme_copy", "cdecl")
    lv_theme_copy.argtypes = [POINTER(lv_theme_t), POINTER(lv_theme_t)]
    lv_theme_copy.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 207
for _lib in _libs.values():
    if not _lib.has("lv_theme_set_base", "cdecl"):
        continue
    lv_theme_set_base = _lib.get("lv_theme_set_base", "cdecl")
    lv_theme_set_base.argtypes = [POINTER(lv_theme_t), POINTER(lv_theme_t)]
    lv_theme_set_base.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 215
for _lib in _libs.values():
    if not _lib.has("lv_theme_set_apply_cb", "cdecl"):
        continue
    lv_theme_set_apply_cb = _lib.get("lv_theme_set_apply_cb", "cdecl")
    lv_theme_set_apply_cb.argtypes = [POINTER(lv_theme_t), lv_theme_apply_cb_t]
    lv_theme_set_apply_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 221
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_font_small", "cdecl"):
        continue
    lv_theme_get_font_small = _lib.get("lv_theme_get_font_small", "cdecl")
    lv_theme_get_font_small.argtypes = []
    lv_theme_get_font_small.restype = POINTER(lv_font_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 227
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_font_normal", "cdecl"):
        continue
    lv_theme_get_font_normal = _lib.get("lv_theme_get_font_normal", "cdecl")
    lv_theme_get_font_normal.argtypes = []
    lv_theme_get_font_normal.restype = POINTER(lv_font_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 233
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_font_subtitle", "cdecl"):
        continue
    lv_theme_get_font_subtitle = _lib.get("lv_theme_get_font_subtitle", "cdecl")
    lv_theme_get_font_subtitle.argtypes = []
    lv_theme_get_font_subtitle.restype = POINTER(lv_font_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 239
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_font_title", "cdecl"):
        continue
    lv_theme_get_font_title = _lib.get("lv_theme_get_font_title", "cdecl")
    lv_theme_get_font_title.argtypes = []
    lv_theme_get_font_title.restype = POINTER(lv_font_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 245
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_color_primary", "cdecl"):
        continue
    lv_theme_get_color_primary = _lib.get("lv_theme_get_color_primary", "cdecl")
    lv_theme_get_color_primary.argtypes = []
    lv_theme_get_color_primary.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 251
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_color_secondary", "cdecl"):
        continue
    lv_theme_get_color_secondary = _lib.get("lv_theme_get_color_secondary", "cdecl")
    lv_theme_get_color_secondary.argtypes = []
    lv_theme_get_color_secondary.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 257
for _lib in _libs.values():
    if not _lib.has("lv_theme_get_flags", "cdecl"):
        continue
    lv_theme_get_flags = _lib.get("lv_theme_get_flags", "cdecl")
    lv_theme_get_flags.argtypes = []
    lv_theme_get_flags.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_empty.h: 43
for _lib in _libs.values():
    if not _lib.has("lv_theme_empty_init", "cdecl"):
        continue
    lv_theme_empty_init = _lib.get("lv_theme_empty_init", "cdecl")
    lv_theme_empty_init.argtypes = [lv_color_t, lv_color_t, c_uint32, POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t)]
    lv_theme_empty_init.restype = POINTER(lv_theme_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_template.h: 43
for _lib in _libs.values():
    if not _lib.has("lv_theme_template_init", "cdecl"):
        continue
    lv_theme_template_init = _lib.get("lv_theme_template_init", "cdecl")
    lv_theme_template_init.argtypes = [lv_color_t, lv_color_t, c_uint32, POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t)]
    lv_theme_template_init.restype = POINTER(lv_theme_t)
    break

enum_anon_93 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

LV_THEME_MATERIAL_FLAG_DARK = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

LV_THEME_MATERIAL_FLAG_LIGHT = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

LV_THEME_MATERIAL_FLAG_NO_TRANSITION = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

LV_THEME_MATERIAL_FLAG_NO_FOCUS = 32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

lv_theme_material_flag_t = enum_anon_93# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 28

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_material.h: 49
for _lib in _libs.values():
    if not _lib.has("lv_theme_material_init", "cdecl"):
        continue
    lv_theme_material_init = _lib.get("lv_theme_material_init", "cdecl")
    lv_theme_material_init.argtypes = [lv_color_t, lv_color_t, c_uint32, POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t)]
    lv_theme_material_init.restype = POINTER(lv_theme_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme_mono.h: 43
for _lib in _libs.values():
    if not _lib.has("lv_theme_mono_init", "cdecl"):
        continue
    lv_theme_mono_init = _lib.get("lv_theme_mono_init", "cdecl")
    lv_theme_mono_init.argtypes = [lv_color_t, lv_color_t, c_uint32, POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t), POINTER(lv_font_t)]
    lv_theme_mono_init.restype = POINTER(lv_theme_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_loader.h: 31
for _lib in _libs.values():
    if not _lib.has("lv_font_load", "cdecl"):
        continue
    lv_font_load = _lib.get("lv_font_load", "cdecl")
    lv_font_load.argtypes = [String]
    lv_font_load.restype = POINTER(lv_font_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_loader.h: 32
for _lib in _libs.values():
    if not _lib.has("lv_font_free", "cdecl"):
        continue
    lv_font_free = _lib.get("lv_font_free", "cdecl")
    lv_font_free.argtypes = [POINTER(lv_font_t)]
    lv_font_free.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 46
class struct_anon_94(Structure):
    pass

struct_anon_94.__slots__ = [
    'bitmap_index',
    'adv_w',
    'box_w',
    'box_h',
    'ofs_x',
    'ofs_y',
]
struct_anon_94._fields_ = [
    ('bitmap_index', c_uint32, 20),
    ('adv_w', c_uint32, 12),
    ('box_w', c_uint8),
    ('box_h', c_uint8),
    ('ofs_x', c_int8),
    ('ofs_y', c_int8),
]

lv_font_fmt_txt_glyph_dsc_t = struct_anon_94# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 46

enum_anon_95 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 49

LV_FONT_FMT_TXT_CMAP_FORMAT0_TINY = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 49

LV_FONT_FMT_TXT_CMAP_FORMAT0_FULL = (LV_FONT_FMT_TXT_CMAP_FORMAT0_TINY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 49

LV_FONT_FMT_TXT_CMAP_SPARSE_TINY = (LV_FONT_FMT_TXT_CMAP_FORMAT0_FULL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 49

LV_FONT_FMT_TXT_CMAP_SPARSE_FULL = (LV_FONT_FMT_TXT_CMAP_SPARSE_TINY + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 49

lv_font_fmt_txt_cmap_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 56

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 112
class struct_anon_96(Structure):
    pass

struct_anon_96.__slots__ = [
    'range_start',
    'range_length',
    'glyph_id_start',
    'unicode_list',
    'glyph_id_ofs_list',
    'list_length',
    'type',
]
struct_anon_96._fields_ = [
    ('range_start', c_uint32),
    ('range_length', c_uint16),
    ('glyph_id_start', c_uint16),
    ('unicode_list', POINTER(c_uint16)),
    ('glyph_id_ofs_list', POINTER(None)),
    ('list_length', c_uint16),
    ('type', lv_font_fmt_txt_cmap_type_t),
]

lv_font_fmt_txt_cmap_t = struct_anon_96# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 112

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 127
class struct_anon_97(Structure):
    pass

struct_anon_97.__slots__ = [
    'glyph_ids',
    'values',
    'pair_cnt',
    'glyph_ids_size',
]
struct_anon_97._fields_ = [
    ('glyph_ids', POINTER(None)),
    ('values', POINTER(c_int8)),
    ('pair_cnt', c_uint32, 24),
    ('glyph_ids_size', c_uint32, 2),
]

lv_font_fmt_txt_kern_pair_t = struct_anon_97# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 127

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 144
class struct_anon_98(Structure):
    pass

struct_anon_98.__slots__ = [
    'class_pair_values',
    'left_class_mapping',
    'right_class_mapping',
    'left_class_cnt',
    'right_class_cnt',
]
struct_anon_98._fields_ = [
    ('class_pair_values', POINTER(c_int8)),
    ('left_class_mapping', POINTER(c_uint8)),
    ('right_class_mapping', POINTER(c_uint8)),
    ('left_class_cnt', c_uint8),
    ('right_class_cnt', c_uint8),
]

lv_font_fmt_txt_kern_classes_t = struct_anon_98# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 144

enum_anon_99 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 151

LV_FONT_FMT_TXT_PLAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 151

LV_FONT_FMT_TXT_COMPRESSED = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 151

LV_FONT_FMT_TXT_COMPRESSED_NO_PREFILTER = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 151

lv_font_fmt_txt_bitmap_format_t = enum_anon_99# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 151

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 193
class struct_anon_100(Structure):
    pass

struct_anon_100.__slots__ = [
    'glyph_bitmap',
    'glyph_dsc',
    'cmaps',
    'kern_dsc',
    'kern_scale',
    'cmap_num',
    'bpp',
    'kern_classes',
    'bitmap_format',
    'last_letter',
    'last_glyph_id',
]
struct_anon_100._fields_ = [
    ('glyph_bitmap', POINTER(c_uint8)),
    ('glyph_dsc', POINTER(lv_font_fmt_txt_glyph_dsc_t)),
    ('cmaps', POINTER(lv_font_fmt_txt_cmap_t)),
    ('kern_dsc', POINTER(None)),
    ('kern_scale', c_uint16),
    ('cmap_num', c_uint16, 10),
    ('bpp', c_uint16, 4),
    ('kern_classes', c_uint16, 1),
    ('bitmap_format', c_uint16, 2),
    ('last_letter', c_uint32),
    ('last_glyph_id', c_uint32),
]

lv_font_fmt_txt_dsc_t = struct_anon_100# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 193

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 205
for _lib in _libs.values():
    if not _lib.has("lv_font_get_bitmap_fmt_txt", "cdecl"):
        continue
    lv_font_get_bitmap_fmt_txt = _lib.get("lv_font_get_bitmap_fmt_txt", "cdecl")
    lv_font_get_bitmap_fmt_txt.argtypes = [POINTER(lv_font_t), c_uint32]
    lv_font_get_bitmap_fmt_txt.restype = POINTER(c_uint8)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 215
for _lib in _libs.values():
    if not _lib.has("lv_font_get_glyph_dsc_fmt_txt", "cdecl"):
        continue
    lv_font_get_glyph_dsc_fmt_txt = _lib.get("lv_font_get_glyph_dsc_fmt_txt", "cdecl")
    lv_font_get_glyph_dsc_fmt_txt.argtypes = [POINTER(lv_font_t), POINTER(lv_font_glyph_dsc_t), c_uint32, c_uint32]
    lv_font_get_glyph_dsc_fmt_txt.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_font/lv_font_fmt_txt.h: 221
for _lib in _libs.values():
    if not _lib.has("_lv_font_clean_up_fmt_txt", "cdecl"):
        continue
    _lv_font_clean_up_fmt_txt = _lib.get("_lv_font_clean_up_fmt_txt", "cdecl")
    _lv_font_clean_up_fmt_txt.argtypes = []
    _lv_font_clean_up_fmt_txt.restype = None
    break

enum_anon_101 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_OFF = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_CENTER = (LV_LAYOUT_OFF + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_COLUMN_LEFT = (LV_LAYOUT_CENTER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_COLUMN_MID = (LV_LAYOUT_COLUMN_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_COLUMN_RIGHT = (LV_LAYOUT_COLUMN_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_ROW_TOP = (LV_LAYOUT_COLUMN_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_ROW_MID = (LV_LAYOUT_ROW_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_ROW_BOTTOM = (LV_LAYOUT_ROW_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_PRETTY_TOP = (LV_LAYOUT_ROW_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_PRETTY_MID = (LV_LAYOUT_PRETTY_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_PRETTY_BOTTOM = (LV_LAYOUT_PRETTY_MID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

LV_LAYOUT_GRID = (LV_LAYOUT_PRETTY_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

_LV_LAYOUT_LAST = (LV_LAYOUT_GRID + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 31

lv_layout_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 84

enum_anon_102 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

LV_FIT_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

LV_FIT_TIGHT = (LV_FIT_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

LV_FIT_PARENT = (LV_FIT_TIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

LV_FIT_MAX = (LV_FIT_PARENT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

_LV_FIT_LAST = (LV_FIT_MAX + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 89

lv_fit_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 97

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 107
class struct_anon_103(Structure):
    pass

struct_anon_103.__slots__ = [
    'layout',
    'fit_left',
    'fit_right',
    'fit_top',
    'fit_bottom',
]
struct_anon_103._fields_ = [
    ('layout', lv_layout_t, 4),
    ('fit_left', lv_fit_t, 2),
    ('fit_right', lv_fit_t, 2),
    ('fit_top', lv_fit_t, 2),
    ('fit_bottom', lv_fit_t, 2),
]

lv_cont_ext_t = struct_anon_103# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 107

enum_anon_104 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 110

LV_CONT_PART_MAIN = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 110

_LV_CONT_PART_VIRTUAL_LAST = _LV_OBJ_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 110

_LV_CONT_PART_REAL_LAST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 110

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 126
for _lib in _libs.values():
    if not _lib.has("lv_cont_create", "cdecl"):
        continue
    lv_cont_create = _lib.get("lv_cont_create", "cdecl")
    lv_cont_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_cont_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 137
for _lib in _libs.values():
    if not _lib.has("lv_cont_set_layout", "cdecl"):
        continue
    lv_cont_set_layout = _lib.get("lv_cont_set_layout", "cdecl")
    lv_cont_set_layout.argtypes = [POINTER(lv_obj_t), lv_layout_t]
    lv_cont_set_layout.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 148
for _lib in _libs.values():
    if not _lib.has("lv_cont_set_fit4", "cdecl"):
        continue
    lv_cont_set_fit4 = _lib.get("lv_cont_set_fit4", "cdecl")
    lv_cont_set_fit4.argtypes = [POINTER(lv_obj_t), lv_fit_t, lv_fit_t, lv_fit_t, lv_fit_t]
    lv_cont_set_fit4.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 182
for _lib in _libs.values():
    if not _lib.has("lv_cont_get_layout", "cdecl"):
        continue
    lv_cont_get_layout = _lib.get("lv_cont_get_layout", "cdecl")
    lv_cont_get_layout.argtypes = [POINTER(lv_obj_t)]
    lv_cont_get_layout.restype = lv_layout_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 189
for _lib in _libs.values():
    if not _lib.has("lv_cont_get_fit_left", "cdecl"):
        continue
    lv_cont_get_fit_left = _lib.get("lv_cont_get_fit_left", "cdecl")
    lv_cont_get_fit_left.argtypes = [POINTER(lv_obj_t)]
    lv_cont_get_fit_left.restype = lv_fit_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 196
for _lib in _libs.values():
    if not _lib.has("lv_cont_get_fit_right", "cdecl"):
        continue
    lv_cont_get_fit_right = _lib.get("lv_cont_get_fit_right", "cdecl")
    lv_cont_get_fit_right.argtypes = [POINTER(lv_obj_t)]
    lv_cont_get_fit_right.restype = lv_fit_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 203
for _lib in _libs.values():
    if not _lib.has("lv_cont_get_fit_top", "cdecl"):
        continue
    lv_cont_get_fit_top = _lib.get("lv_cont_get_fit_top", "cdecl")
    lv_cont_get_fit_top.argtypes = [POINTER(lv_obj_t)]
    lv_cont_get_fit_top.restype = lv_fit_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cont.h: 210
for _lib in _libs.values():
    if not _lib.has("lv_cont_get_fit_bottom", "cdecl"):
        continue
    lv_cont_get_fit_bottom = _lib.get("lv_cont_get_fit_bottom", "cdecl")
    lv_cont_get_fit_bottom.argtypes = [POINTER(lv_obj_t)]
    lv_cont_get_fit_bottom.restype = lv_fit_t
    break

enum_anon_105 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_RELEASED = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_PRESSED = (LV_BTN_STATE_RELEASED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_DISABLED = (LV_BTN_STATE_PRESSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_CHECKED_RELEASED = (LV_BTN_STATE_DISABLED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_CHECKED_PRESSED = (LV_BTN_STATE_CHECKED_RELEASED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

LV_BTN_STATE_CHECKED_DISABLED = (LV_BTN_STATE_CHECKED_PRESSED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

_LV_BTN_STATE_LAST = (LV_BTN_STATE_CHECKED_DISABLED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 38

lv_btn_state_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 47

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 56
class struct_anon_106(Structure):
    pass

struct_anon_106.__slots__ = [
    'cont',
    'checkable',
]
struct_anon_106._fields_ = [
    ('cont', lv_cont_ext_t),
    ('checkable', c_uint8, 1),
]

lv_btn_ext_t = struct_anon_106# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 56

enum_anon_107 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 59

LV_BTN_PART_MAIN = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 59

_LV_BTN_PART_VIRTUAL_LAST = (LV_BTN_PART_MAIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 59

_LV_BTN_PART_REAL_LAST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 59

lv_btn_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 64

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 76
for _lib in _libs.values():
    if not _lib.has("lv_btn_create", "cdecl"):
        continue
    lv_btn_create = _lib.get("lv_btn_create", "cdecl")
    lv_btn_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_btn_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 87
for _lib in _libs.values():
    if not _lib.has("lv_btn_set_checkable", "cdecl"):
        continue
    lv_btn_set_checkable = _lib.get("lv_btn_set_checkable", "cdecl")
    lv_btn_set_checkable.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_btn_set_checkable.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 94
for _lib in _libs.values():
    if not _lib.has("lv_btn_set_state", "cdecl"):
        continue
    lv_btn_set_state = _lib.get("lv_btn_set_state", "cdecl")
    lv_btn_set_state.argtypes = [POINTER(lv_obj_t), lv_btn_state_t]
    lv_btn_set_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 100
for _lib in _libs.values():
    if not _lib.has("lv_btn_toggle", "cdecl"):
        continue
    lv_btn_toggle = _lib.get("lv_btn_toggle", "cdecl")
    lv_btn_toggle.argtypes = [POINTER(lv_obj_t)]
    lv_btn_toggle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 159
for _lib in _libs.values():
    if not _lib.has("lv_btn_get_state", "cdecl"):
        continue
    lv_btn_get_state = _lib.get("lv_btn_get_state", "cdecl")
    lv_btn_get_state.argtypes = [POINTER(lv_obj_t)]
    lv_btn_get_state.restype = lv_btn_state_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btn.h: 166
for _lib in _libs.values():
    if not _lib.has("lv_btn_get_checkable", "cdecl"):
        continue
    lv_btn_get_checkable = _lib.get("lv_btn_get_checkable", "cdecl")
    lv_btn_get_checkable.argtypes = [POINTER(lv_obj_t)]
    lv_btn_get_checkable.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 47
class struct_anon_108(Structure):
    pass

struct_anon_108.__slots__ = [
    'btn',
    'img_src_mid',
    'act_cf',
    'tiled',
]
struct_anon_108._fields_ = [
    ('btn', lv_btn_ext_t),
    ('img_src_mid', POINTER(None) * int(_LV_BTN_STATE_LAST)),
    ('act_cf', lv_img_cf_t),
    ('tiled', c_uint8, 1),
]

lv_imgbtn_ext_t = struct_anon_108# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 47

enum_anon_109 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 50

LV_IMGBTN_PART_MAIN = LV_BTN_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 50

lv_imgbtn_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 53

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 66
for _lib in _libs.values():
    if not _lib.has("lv_imgbtn_create", "cdecl"):
        continue
    lv_imgbtn_create = _lib.get("lv_imgbtn_create", "cdecl")
    lv_imgbtn_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_imgbtn_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_imgbtn_set_src", "cdecl"):
        continue
    lv_imgbtn_set_src = _lib.get("lv_imgbtn_set_src", "cdecl")
    lv_imgbtn_set_src.argtypes = [POINTER(lv_obj_t), lv_btn_state_t, POINTER(None)]
    lv_imgbtn_set_src.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_imgbtn_set_state", "cdecl"):
        continue
    lv_imgbtn_set_state = _lib.get("lv_imgbtn_set_state", "cdecl")
    lv_imgbtn_set_state.argtypes = [POINTER(lv_obj_t), lv_btn_state_t]
    lv_imgbtn_set_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 112
for _lib in _libs.values():
    if not _lib.has("lv_imgbtn_toggle", "cdecl"):
        continue
    lv_imgbtn_toggle = _lib.get("lv_imgbtn_toggle", "cdecl")
    lv_imgbtn_toggle.argtypes = [POINTER(lv_obj_t)]
    lv_imgbtn_toggle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_imgbtn.h: 135
for _lib in _libs.values():
    if not _lib.has("lv_imgbtn_get_src", "cdecl"):
        continue
    lv_imgbtn_get_src = _lib.get("lv_imgbtn_get_src", "cdecl")
    lv_imgbtn_get_src.argtypes = [POINTER(lv_obj_t), lv_btn_state_t]
    lv_imgbtn_get_src.restype = POINTER(c_ubyte)
    lv_imgbtn_get_src.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/../lv_draw/lv_draw_triangle.h: 36
for _lib in _libs.values():
    if not _lib.has("lv_draw_triangle", "cdecl"):
        continue
    lv_draw_triangle = _lib.get("lv_draw_triangle", "cdecl")
    lv_draw_triangle.argtypes = [POINTER(lv_point_t), POINTER(lv_area_t), POINTER(lv_draw_rect_dsc_t)]
    lv_draw_triangle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/../lv_draw/lv_draw_triangle.h: 45
for _lib in _libs.values():
    if not _lib.has("lv_draw_polygon", "cdecl"):
        continue
    lv_draw_polygon = _lib.get("lv_draw_polygon", "cdecl")
    lv_draw_polygon.argtypes = [POINTER(lv_point_t), c_uint16, POINTER(lv_area_t), POINTER(lv_draw_rect_dsc_t)]
    lv_draw_polygon.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/../lv_draw/lv_draw_arc.h: 41
for _lib in _libs.values():
    if not _lib.has("lv_draw_arc", "cdecl"):
        continue
    lv_draw_arc = _lib.get("lv_draw_arc", "cdecl")
    lv_draw_arc.argtypes = [lv_coord_t, lv_coord_t, c_uint16, c_uint16, c_uint16, POINTER(lv_area_t), POINTER(lv_draw_line_dsc_t)]
    lv_draw_arc.restype = None
    break

enum_anon_110 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_EXPAND = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_BREAK = (LV_LABEL_LONG_EXPAND + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_DOT = (LV_LABEL_LONG_BREAK + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_SROLL = (LV_LABEL_LONG_DOT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_SROLL_CIRC = (LV_LABEL_LONG_SROLL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

LV_LABEL_LONG_CROP = (LV_LABEL_LONG_SROLL_CIRC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 43

lv_label_long_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 52

enum_anon_111 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 55

LV_LABEL_ALIGN_LEFT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 55

LV_LABEL_ALIGN_CENTER = (LV_LABEL_ALIGN_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 55

LV_LABEL_ALIGN_RIGHT = (LV_LABEL_ALIGN_CENTER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 55

LV_LABEL_ALIGN_AUTO = (LV_LABEL_ALIGN_RIGHT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 55

lv_label_align_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 61

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 69
class union_anon_112(Union):
    pass

union_anon_112.__slots__ = [
    'tmp_ptr',
    'tmp',
]
union_anon_112._fields_ = [
    ('tmp_ptr', String),
    ('tmp', c_char * int((3 + 1))),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 99
class struct_anon_113(Structure):
    pass

struct_anon_113.__slots__ = [
    'text',
    'dot',
    'dot_end',
    'anim_speed',
    'offset',
    'long_mode',
    'static_txt',
    'align',
    'recolor',
    'expand',
    'dot_tmp_alloc',
]
struct_anon_113._fields_ = [
    ('text', String),
    ('dot', union_anon_112),
    ('dot_end', c_uint32),
    ('anim_speed', c_uint16),
    ('offset', lv_point_t),
    ('long_mode', lv_label_long_mode_t, 3),
    ('static_txt', c_uint8, 1),
    ('align', c_uint8, 2),
    ('recolor', c_uint8, 1),
    ('expand', c_uint8, 1),
    ('dot_tmp_alloc', c_uint8, 1),
]

lv_label_ext_t = struct_anon_113# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 99

enum_anon_114 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 102

LV_LABEL_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 102

lv_label_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 106

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 118
for _lib in _libs.values():
    if not _lib.has("lv_label_create", "cdecl"):
        continue
    lv_label_create = _lib.get("lv_label_create", "cdecl")
    lv_label_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_label_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_label_set_text", "cdecl"):
        continue
    lv_label_set_text = _lib.get("lv_label_set_text", "cdecl")
    lv_label_set_text.argtypes = [POINTER(lv_obj_t), String]
    lv_label_set_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 136
for _lib in _libs.values():
    if _lib.has("lv_label_set_text_fmt", "cdecl"):
        _func = _lib.get("lv_label_set_text_fmt", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(lv_obj_t), String]
        lv_label_set_text_fmt = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 144
for _lib in _libs.values():
    if not _lib.has("lv_label_set_text_static", "cdecl"):
        continue
    lv_label_set_text_static = _lib.get("lv_label_set_text_static", "cdecl")
    lv_label_set_text_static.argtypes = [POINTER(lv_obj_t), String]
    lv_label_set_text_static.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 153
for _lib in _libs.values():
    if not _lib.has("lv_label_set_long_mode", "cdecl"):
        continue
    lv_label_set_long_mode = _lib.get("lv_label_set_long_mode", "cdecl")
    lv_label_set_long_mode.argtypes = [POINTER(lv_obj_t), lv_label_long_mode_t]
    lv_label_set_long_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 160
for _lib in _libs.values():
    if not _lib.has("lv_label_set_align", "cdecl"):
        continue
    lv_label_set_align = _lib.get("lv_label_set_align", "cdecl")
    lv_label_set_align.argtypes = [POINTER(lv_obj_t), lv_label_align_t]
    lv_label_set_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 167
for _lib in _libs.values():
    if not _lib.has("lv_label_set_recolor", "cdecl"):
        continue
    lv_label_set_recolor = _lib.get("lv_label_set_recolor", "cdecl")
    lv_label_set_recolor.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_label_set_recolor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 174
for _lib in _libs.values():
    if not _lib.has("lv_label_set_anim_speed", "cdecl"):
        continue
    lv_label_set_anim_speed = _lib.get("lv_label_set_anim_speed", "cdecl")
    lv_label_set_anim_speed.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_label_set_anim_speed.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 181
for _lib in _libs.values():
    if not _lib.has("lv_label_set_text_sel_start", "cdecl"):
        continue
    lv_label_set_text_sel_start = _lib.get("lv_label_set_text_sel_start", "cdecl")
    lv_label_set_text_sel_start.argtypes = [POINTER(lv_obj_t), c_uint32]
    lv_label_set_text_sel_start.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 188
for _lib in _libs.values():
    if not _lib.has("lv_label_set_text_sel_end", "cdecl"):
        continue
    lv_label_set_text_sel_end = _lib.get("lv_label_set_text_sel_end", "cdecl")
    lv_label_set_text_sel_end.argtypes = [POINTER(lv_obj_t), c_uint32]
    lv_label_set_text_sel_end.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 198
for _lib in _libs.values():
    if not _lib.has("lv_label_get_text", "cdecl"):
        continue
    lv_label_get_text = _lib.get("lv_label_get_text", "cdecl")
    lv_label_get_text.argtypes = [POINTER(lv_obj_t)]
    if sizeof(c_int) == sizeof(c_void_p):
        lv_label_get_text.restype = ReturnString
    else:
        lv_label_get_text.restype = String
        lv_label_get_text.errcheck = ReturnString
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 205
for _lib in _libs.values():
    if not _lib.has("lv_label_get_long_mode", "cdecl"):
        continue
    lv_label_get_long_mode = _lib.get("lv_label_get_long_mode", "cdecl")
    lv_label_get_long_mode.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_long_mode.restype = lv_label_long_mode_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 212
for _lib in _libs.values():
    if not _lib.has("lv_label_get_align", "cdecl"):
        continue
    lv_label_get_align = _lib.get("lv_label_get_align", "cdecl")
    lv_label_get_align.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_align.restype = lv_label_align_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 219
for _lib in _libs.values():
    if not _lib.has("lv_label_get_recolor", "cdecl"):
        continue
    lv_label_get_recolor = _lib.get("lv_label_get_recolor", "cdecl")
    lv_label_get_recolor.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_recolor.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 226
for _lib in _libs.values():
    if not _lib.has("lv_label_get_anim_speed", "cdecl"):
        continue
    lv_label_get_anim_speed = _lib.get("lv_label_get_anim_speed", "cdecl")
    lv_label_get_anim_speed.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_anim_speed.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 235
for _lib in _libs.values():
    if not _lib.has("lv_label_get_letter_pos", "cdecl"):
        continue
    lv_label_get_letter_pos = _lib.get("lv_label_get_letter_pos", "cdecl")
    lv_label_get_letter_pos.argtypes = [POINTER(lv_obj_t), c_uint32, POINTER(lv_point_t)]
    lv_label_get_letter_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 244
for _lib in _libs.values():
    if not _lib.has("lv_label_get_letter_on", "cdecl"):
        continue
    lv_label_get_letter_on = _lib.get("lv_label_get_letter_on", "cdecl")
    lv_label_get_letter_on.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_label_get_letter_on.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 252
for _lib in _libs.values():
    if not _lib.has("lv_label_is_char_under_pos", "cdecl"):
        continue
    lv_label_is_char_under_pos = _lib.get("lv_label_is_char_under_pos", "cdecl")
    lv_label_is_char_under_pos.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_label_is_char_under_pos.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 259
for _lib in _libs.values():
    if not _lib.has("lv_label_get_text_sel_start", "cdecl"):
        continue
    lv_label_get_text_sel_start = _lib.get("lv_label_get_text_sel_start", "cdecl")
    lv_label_get_text_sel_start.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_text_sel_start.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 266
for _lib in _libs.values():
    if not _lib.has("lv_label_get_text_sel_end", "cdecl"):
        continue
    lv_label_get_text_sel_end = _lib.get("lv_label_get_text_sel_end", "cdecl")
    lv_label_get_text_sel_end.argtypes = [POINTER(lv_obj_t)]
    lv_label_get_text_sel_end.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 268
for _lib in _libs.values():
    if not _lib.has("lv_label_get_style", "cdecl"):
        continue
    lv_label_get_style = _lib.get("lv_label_get_style", "cdecl")
    lv_label_get_style.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_label_get_style.restype = POINTER(lv_style_list_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 281
for _lib in _libs.values():
    if not _lib.has("lv_label_ins_text", "cdecl"):
        continue
    lv_label_ins_text = _lib.get("lv_label_ins_text", "cdecl")
    lv_label_ins_text.argtypes = [POINTER(lv_obj_t), c_uint32, String]
    lv_label_ins_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 290
for _lib in _libs.values():
    if not _lib.has("lv_label_cut_text", "cdecl"):
        continue
    lv_label_cut_text = _lib.get("lv_label_cut_text", "cdecl")
    lv_label_cut_text.argtypes = [POINTER(lv_obj_t), c_uint32, c_uint32]
    lv_label_cut_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 296
for _lib in _libs.values():
    if not _lib.has("lv_label_refr_text", "cdecl"):
        continue
    lv_label_refr_text = _lib.get("lv_label_refr_text", "cdecl")
    lv_label_refr_text.argtypes = [POINTER(lv_obj_t)]
    lv_label_refr_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 47
class struct_anon_115(Structure):
    pass

struct_anon_115.__slots__ = [
    'src',
    'offset',
    'w',
    'h',
    'angle',
    'pivot',
    'zoom',
    'src_type',
    'auto_size',
    'cf',
    'antialias',
]
struct_anon_115._fields_ = [
    ('src', POINTER(None)),
    ('offset', lv_point_t),
    ('w', lv_coord_t),
    ('h', lv_coord_t),
    ('angle', c_uint16),
    ('pivot', lv_point_t),
    ('zoom', c_uint16),
    ('src_type', c_uint8, 2),
    ('auto_size', c_uint8, 1),
    ('cf', c_uint8, 5),
    ('antialias', c_uint8, 1),
]

lv_img_ext_t = struct_anon_115# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 47

enum_anon_116 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 50

LV_IMG_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 50

lv_img_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 53

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 65
for _lib in _libs.values():
    if not _lib.has("lv_img_create", "cdecl"):
        continue
    lv_img_create = _lib.get("lv_img_create", "cdecl")
    lv_img_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_img_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 76
for _lib in _libs.values():
    if not _lib.has("lv_img_set_src", "cdecl"):
        continue
    lv_img_set_src = _lib.get("lv_img_set_src", "cdecl")
    lv_img_set_src.argtypes = [POINTER(lv_obj_t), POINTER(None)]
    lv_img_set_src.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 84
for _lib in _libs.values():
    if not _lib.has("lv_img_set_auto_size", "cdecl"):
        continue
    lv_img_set_auto_size = _lib.get("lv_img_set_auto_size", "cdecl")
    lv_img_set_auto_size.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_img_set_auto_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 92
for _lib in _libs.values():
    if not _lib.has("lv_img_set_offset_x", "cdecl"):
        continue
    lv_img_set_offset_x = _lib.get("lv_img_set_offset_x", "cdecl")
    lv_img_set_offset_x.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_img_set_offset_x.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 100
for _lib in _libs.values():
    if not _lib.has("lv_img_set_offset_y", "cdecl"):
        continue
    lv_img_set_offset_y = _lib.get("lv_img_set_offset_y", "cdecl")
    lv_img_set_offset_y.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_img_set_offset_y.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_img_set_pivot", "cdecl"):
        continue
    lv_img_set_pivot = _lib.get("lv_img_set_pivot", "cdecl")
    lv_img_set_pivot.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t]
    lv_img_set_pivot.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 117
for _lib in _libs.values():
    if not _lib.has("lv_img_set_angle", "cdecl"):
        continue
    lv_img_set_angle = _lib.get("lv_img_set_angle", "cdecl")
    lv_img_set_angle.argtypes = [POINTER(lv_obj_t), c_int16]
    lv_img_set_angle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_img_set_zoom", "cdecl"):
        continue
    lv_img_set_zoom = _lib.get("lv_img_set_zoom", "cdecl")
    lv_img_set_zoom.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_img_set_zoom.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 136
for _lib in _libs.values():
    if not _lib.has("lv_img_set_antialias", "cdecl"):
        continue
    lv_img_set_antialias = _lib.get("lv_img_set_antialias", "cdecl")
    lv_img_set_antialias.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_img_set_antialias.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 147
for _lib in _libs.values():
    if not _lib.has("lv_img_get_src", "cdecl"):
        continue
    lv_img_get_src = _lib.get("lv_img_get_src", "cdecl")
    lv_img_get_src.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_src.restype = POINTER(c_ubyte)
    lv_img_get_src.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 154
for _lib in _libs.values():
    if not _lib.has("lv_img_get_file_name", "cdecl"):
        continue
    lv_img_get_file_name = _lib.get("lv_img_get_file_name", "cdecl")
    lv_img_get_file_name.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_file_name.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_img_get_auto_size", "cdecl"):
        continue
    lv_img_get_auto_size = _lib.get("lv_img_get_auto_size", "cdecl")
    lv_img_get_auto_size.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_auto_size.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 168
for _lib in _libs.values():
    if not _lib.has("lv_img_get_offset_x", "cdecl"):
        continue
    lv_img_get_offset_x = _lib.get("lv_img_get_offset_x", "cdecl")
    lv_img_get_offset_x.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_offset_x.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 175
for _lib in _libs.values():
    if not _lib.has("lv_img_get_offset_y", "cdecl"):
        continue
    lv_img_get_offset_y = _lib.get("lv_img_get_offset_y", "cdecl")
    lv_img_get_offset_y.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_offset_y.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 182
for _lib in _libs.values():
    if not _lib.has("lv_img_get_angle", "cdecl"):
        continue
    lv_img_get_angle = _lib.get("lv_img_get_angle", "cdecl")
    lv_img_get_angle.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_angle.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 189
for _lib in _libs.values():
    if not _lib.has("lv_img_get_pivot", "cdecl"):
        continue
    lv_img_get_pivot = _lib.get("lv_img_get_pivot", "cdecl")
    lv_img_get_pivot.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t)]
    lv_img_get_pivot.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 196
for _lib in _libs.values():
    if not _lib.has("lv_img_get_zoom", "cdecl"):
        continue
    lv_img_get_zoom = _lib.get("lv_img_get_zoom", "cdecl")
    lv_img_get_zoom.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_zoom.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_img.h: 203
for _lib in _libs.values():
    if not _lib.has("lv_img_get_antialias", "cdecl"):
        continue
    lv_img_get_antialias = _lib.get("lv_img_get_antialias", "cdecl")
    lv_img_get_antialias.argtypes = [POINTER(lv_obj_t)]
    lv_img_get_antialias.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 37
class struct_anon_117(Structure):
    pass

struct_anon_117.__slots__ = [
    'point_array',
    'point_num',
    'auto_size',
    'y_inv',
]
struct_anon_117._fields_ = [
    ('point_array', POINTER(lv_point_t)),
    ('point_num', c_uint16),
    ('auto_size', c_uint8, 1),
    ('y_inv', c_uint8, 1),
]

lv_line_ext_t = struct_anon_117# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 37

enum_anon_118 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 40

LV_LINE_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 40

lv_line_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 43

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 54
for _lib in _libs.values():
    if not _lib.has("lv_line_create", "cdecl"):
        continue
    lv_line_create = _lib.get("lv_line_create", "cdecl")
    lv_line_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_line_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 67
for _lib in _libs.values():
    if not _lib.has("lv_line_set_points", "cdecl"):
        continue
    lv_line_set_points = _lib.get("lv_line_set_points", "cdecl")
    lv_line_set_points.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t), c_uint16]
    lv_line_set_points.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_line_set_auto_size", "cdecl"):
        continue
    lv_line_set_auto_size = _lib.get("lv_line_set_auto_size", "cdecl")
    lv_line_set_auto_size.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_line_set_auto_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 84
for _lib in _libs.values():
    if not _lib.has("lv_line_set_y_invert", "cdecl"):
        continue
    lv_line_set_y_invert = _lib.get("lv_line_set_y_invert", "cdecl")
    lv_line_set_y_invert.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_line_set_y_invert.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 99
for _lib in _libs.values():
    if not _lib.has("lv_line_get_auto_size", "cdecl"):
        continue
    lv_line_get_auto_size = _lib.get("lv_line_get_auto_size", "cdecl")
    lv_line_get_auto_size.argtypes = [POINTER(lv_obj_t)]
    lv_line_get_auto_size.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_line_get_y_invert", "cdecl"):
        continue
    lv_line_get_y_invert = _lib.get("lv_line_get_y_invert", "cdecl")
    lv_line_get_y_invert.argtypes = [POINTER(lv_obj_t)]
    lv_line_get_y_invert.restype = c_bool
    break

enum_anon_119 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_OFF = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_ON = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_DRAG = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_AUTO = 3# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_HIDE = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

LV_SCROLLBAR_MODE_UNHIDE = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 38

lv_scrollbar_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 46

enum_anon_120 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 49

LV_PAGE_EDGE_LEFT = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 49

LV_PAGE_EDGE_TOP = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 49

LV_PAGE_EDGE_RIGHT = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 49

LV_PAGE_EDGE_BOTTOM = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 49

lv_page_edge_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 50

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 57
class struct_anon_121(Structure):
    pass

struct_anon_121.__slots__ = [
    'style',
    'hor_area',
    'ver_area',
    'hor_draw',
    'ver_draw',
    'mode',
]
struct_anon_121._fields_ = [
    ('style', lv_style_list_t),
    ('hor_area', lv_area_t),
    ('ver_area', lv_area_t),
    ('hor_draw', c_uint8, 1),
    ('ver_draw', c_uint8, 1),
    ('mode', lv_scrollbar_mode_t, 3),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 66
class struct_anon_122(Structure):
    pass

struct_anon_122.__slots__ = [
    'state',
    'style',
    'enabled',
    'top_ip',
    'bottom_ip',
    'right_ip',
    'left_ip',
]
struct_anon_122._fields_ = [
    ('state', lv_anim_value_t),
    ('style', lv_style_list_t),
    ('enabled', c_uint8, 1),
    ('top_ip', c_uint8, 1),
    ('bottom_ip', c_uint8, 1),
    ('right_ip', c_uint8, 1),
    ('left_ip', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 84
class struct_anon_123(Structure):
    pass

struct_anon_123.__slots__ = [
    'bg',
    'scrl',
    'scrlbar',
    'edge_flash',
    'anim_time',
    'scroll_prop_obj',
    'scroll_prop',
]
struct_anon_123._fields_ = [
    ('bg', lv_cont_ext_t),
    ('scrl', POINTER(lv_obj_t)),
    ('scrlbar', struct_anon_121),
    ('edge_flash', struct_anon_122),
    ('anim_time', c_uint16),
    ('scroll_prop_obj', POINTER(lv_obj_t)),
    ('scroll_prop', c_uint8, 1),
]

lv_page_ext_t = struct_anon_123# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 84

enum_anon_124 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

LV_PAGE_PART_BG = LV_CONT_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

LV_PAGE_PART_SCROLLBAR = _LV_OBJ_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

LV_PAGE_PART_EDGE_FLASH = (LV_PAGE_PART_SCROLLBAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

_LV_PAGE_PART_VIRTUAL_LAST = (LV_PAGE_PART_EDGE_FLASH + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

LV_PAGE_PART_SCROLLABLE = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

_LV_PAGE_PART_REAL_LAST = (LV_PAGE_PART_SCROLLABLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 86

lv_part_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 95

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 107
for _lib in _libs.values():
    if not _lib.has("lv_page_create", "cdecl"):
        continue
    lv_page_create = _lib.get("lv_page_create", "cdecl")
    lv_page_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_page_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_page_clean", "cdecl"):
        continue
    lv_page_clean = _lib.get("lv_page_clean", "cdecl")
    lv_page_clean.argtypes = [POINTER(lv_obj_t)]
    lv_page_clean.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_page_get_scrollable", "cdecl"):
        continue
    lv_page_get_scrollable = _lib.get("lv_page_get_scrollable", "cdecl")
    lv_page_get_scrollable.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_scrollable.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_page_get_anim_time", "cdecl"):
        continue
    lv_page_get_anim_time = _lib.get("lv_page_get_anim_time", "cdecl")
    lv_page_get_anim_time.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_anim_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 138
for _lib in _libs.values():
    if not _lib.has("lv_page_set_scrollbar_mode", "cdecl"):
        continue
    lv_page_set_scrollbar_mode = _lib.get("lv_page_set_scrollbar_mode", "cdecl")
    lv_page_set_scrollbar_mode.argtypes = [POINTER(lv_obj_t), lv_scrollbar_mode_t]
    lv_page_set_scrollbar_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 145
for _lib in _libs.values():
    if not _lib.has("lv_page_set_anim_time", "cdecl"):
        continue
    lv_page_set_anim_time = _lib.get("lv_page_set_anim_time", "cdecl")
    lv_page_set_anim_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_page_set_anim_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 155
for _lib in _libs.values():
    if not _lib.has("lv_page_set_scroll_propagation", "cdecl"):
        continue
    lv_page_set_scroll_propagation = _lib.get("lv_page_set_scroll_propagation", "cdecl")
    lv_page_set_scroll_propagation.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_page_set_scroll_propagation.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 162
for _lib in _libs.values():
    if not _lib.has("lv_page_set_edge_flash", "cdecl"):
        continue
    lv_page_set_edge_flash = _lib.get("lv_page_set_edge_flash", "cdecl")
    lv_page_set_edge_flash.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_page_set_edge_flash.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 241
for _lib in _libs.values():
    if not _lib.has("lv_page_get_scrollbar_mode", "cdecl"):
        continue
    lv_page_get_scrollbar_mode = _lib.get("lv_page_get_scrollbar_mode", "cdecl")
    lv_page_get_scrollbar_mode.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_scrollbar_mode.restype = lv_scrollbar_mode_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 248
for _lib in _libs.values():
    if not _lib.has("lv_page_get_scroll_propagation", "cdecl"):
        continue
    lv_page_get_scroll_propagation = _lib.get("lv_page_get_scroll_propagation", "cdecl")
    lv_page_get_scroll_propagation.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_scroll_propagation.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 255
for _lib in _libs.values():
    if not _lib.has("lv_page_get_edge_flash", "cdecl"):
        continue
    lv_page_get_edge_flash = _lib.get("lv_page_get_edge_flash", "cdecl")
    lv_page_get_edge_flash.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_edge_flash.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 262
for _lib in _libs.values():
    if not _lib.has("lv_page_get_width_fit", "cdecl"):
        continue
    lv_page_get_width_fit = _lib.get("lv_page_get_width_fit", "cdecl")
    lv_page_get_width_fit.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_width_fit.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 269
for _lib in _libs.values():
    if not _lib.has("lv_page_get_height_fit", "cdecl"):
        continue
    lv_page_get_height_fit = _lib.get("lv_page_get_height_fit", "cdecl")
    lv_page_get_height_fit.argtypes = [POINTER(lv_obj_t)]
    lv_page_get_height_fit.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 282
for _lib in _libs.values():
    if not _lib.has("lv_page_get_width_grid", "cdecl"):
        continue
    lv_page_get_width_grid = _lib.get("lv_page_get_width_grid", "cdecl")
    lv_page_get_width_grid.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_page_get_width_grid.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 295
for _lib in _libs.values():
    if not _lib.has("lv_page_get_height_grid", "cdecl"):
        continue
    lv_page_get_height_grid = _lib.get("lv_page_get_height_grid", "cdecl")
    lv_page_get_height_grid.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_page_get_height_grid.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 377
for _lib in _libs.values():
    if not _lib.has("lv_page_on_edge", "cdecl"):
        continue
    lv_page_on_edge = _lib.get("lv_page_on_edge", "cdecl")
    lv_page_on_edge.argtypes = [POINTER(lv_obj_t), lv_page_edge_t]
    lv_page_on_edge.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 384
for _lib in _libs.values():
    if not _lib.has("lv_page_glue_obj", "cdecl"):
        continue
    lv_page_glue_obj = _lib.get("lv_page_glue_obj", "cdecl")
    lv_page_glue_obj.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_page_glue_obj.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 392
for _lib in _libs.values():
    if not _lib.has("lv_page_focus", "cdecl"):
        continue
    lv_page_focus = _lib.get("lv_page_focus", "cdecl")
    lv_page_focus.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_anim_enable_t]
    lv_page_focus.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 399
for _lib in _libs.values():
    if not _lib.has("lv_page_scroll_hor", "cdecl"):
        continue
    lv_page_scroll_hor = _lib.get("lv_page_scroll_hor", "cdecl")
    lv_page_scroll_hor.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_page_scroll_hor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 406
for _lib in _libs.values():
    if not _lib.has("lv_page_scroll_ver", "cdecl"):
        continue
    lv_page_scroll_ver = _lib.get("lv_page_scroll_ver", "cdecl")
    lv_page_scroll_ver.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_page_scroll_ver.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_page.h: 414
for _lib in _libs.values():
    if not _lib.has("lv_page_start_edge_flash", "cdecl"):
        continue
    lv_page_start_edge_flash = _lib.get("lv_page_start_edge_flash", "cdecl")
    lv_page_start_edge_flash.argtypes = [POINTER(lv_obj_t), lv_page_edge_t]
    lv_page_start_edge_flash.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 55
class struct_anon_125(Structure):
    pass

struct_anon_125.__slots__ = [
    'page',
    'last_sel_btn',
    'act_sel_btn',
]
struct_anon_125._fields_ = [
    ('page', lv_page_ext_t),
    ('last_sel_btn', POINTER(lv_obj_t)),
    ('act_sel_btn', POINTER(lv_obj_t)),
]

lv_list_ext_t = struct_anon_125# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 55

enum_anon_126 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

LV_LIST_PART_BG = LV_PAGE_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

LV_LIST_PART_SCROLLBAR = LV_PAGE_PART_SCROLLBAR# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

LV_LIST_PART_EDGE_FLASH = LV_PAGE_PART_EDGE_FLASH# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

_LV_LIST_PART_VIRTUAL_LAST = _LV_PAGE_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

LV_LIST_PART_SCROLLABLE = LV_PAGE_PART_SCROLLABLE# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

_LV_LIST_PART_REAL_LAST = _LV_PAGE_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 58

lv_list_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 66

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 78
for _lib in _libs.values():
    if not _lib.has("lv_list_create", "cdecl"):
        continue
    lv_list_create = _lib.get("lv_list_create", "cdecl")
    lv_list_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_list_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 84
for _lib in _libs.values():
    if not _lib.has("lv_list_clean", "cdecl"):
        continue
    lv_list_clean = _lib.get("lv_list_clean", "cdecl")
    lv_list_clean.argtypes = [POINTER(lv_obj_t)]
    lv_list_clean.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 97
for _lib in _libs.values():
    if not _lib.has("lv_list_add_btn", "cdecl"):
        continue
    lv_list_add_btn = _lib.get("lv_list_add_btn", "cdecl")
    lv_list_add_btn.argtypes = [POINTER(lv_obj_t), POINTER(None), String]
    lv_list_add_btn.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_list_remove", "cdecl"):
        continue
    lv_list_remove = _lib.get("lv_list_remove", "cdecl")
    lv_list_remove.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_list_remove.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 118
for _lib in _libs.values():
    if not _lib.has("lv_list_focus_btn", "cdecl"):
        continue
    lv_list_focus_btn = _lib.get("lv_list_focus_btn", "cdecl")
    lv_list_focus_btn.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_list_focus_btn.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 166
for _lib in _libs.values():
    if not _lib.has("lv_list_set_layout", "cdecl"):
        continue
    lv_list_set_layout = _lib.get("lv_list_set_layout", "cdecl")
    lv_list_set_layout.argtypes = [POINTER(lv_obj_t), lv_layout_t]
    lv_list_set_layout.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 177
for _lib in _libs.values():
    if not _lib.has("lv_list_get_btn_text", "cdecl"):
        continue
    lv_list_get_btn_text = _lib.get("lv_list_get_btn_text", "cdecl")
    lv_list_get_btn_text.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_btn_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 183
for _lib in _libs.values():
    if not _lib.has("lv_list_get_btn_label", "cdecl"):
        continue
    lv_list_get_btn_label = _lib.get("lv_list_get_btn_label", "cdecl")
    lv_list_get_btn_label.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_btn_label.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 190
for _lib in _libs.values():
    if not _lib.has("lv_list_get_btn_img", "cdecl"):
        continue
    lv_list_get_btn_img = _lib.get("lv_list_get_btn_img", "cdecl")
    lv_list_get_btn_img.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_btn_img.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 198
for _lib in _libs.values():
    if not _lib.has("lv_list_get_prev_btn", "cdecl"):
        continue
    lv_list_get_prev_btn = _lib.get("lv_list_get_prev_btn", "cdecl")
    lv_list_get_prev_btn.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_list_get_prev_btn.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 206
for _lib in _libs.values():
    if not _lib.has("lv_list_get_next_btn", "cdecl"):
        continue
    lv_list_get_next_btn = _lib.get("lv_list_get_next_btn", "cdecl")
    lv_list_get_next_btn.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_list_get_next_btn.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 214
for _lib in _libs.values():
    if not _lib.has("lv_list_get_btn_index", "cdecl"):
        continue
    lv_list_get_btn_index = _lib.get("lv_list_get_btn_index", "cdecl")
    lv_list_get_btn_index.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_list_get_btn_index.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 221
for _lib in _libs.values():
    if not _lib.has("lv_list_get_size", "cdecl"):
        continue
    lv_list_get_size = _lib.get("lv_list_get_size", "cdecl")
    lv_list_get_size.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_size.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_list_get_btn_selected", "cdecl"):
        continue
    lv_list_get_btn_selected = _lib.get("lv_list_get_btn_selected", "cdecl")
    lv_list_get_btn_selected.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_btn_selected.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 237
for _lib in _libs.values():
    if not _lib.has("lv_list_get_layout", "cdecl"):
        continue
    lv_list_get_layout = _lib.get("lv_list_get_layout", "cdecl")
    lv_list_get_layout.argtypes = [POINTER(lv_obj_t)]
    lv_list_get_layout.restype = lv_layout_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 287
for _lib in _libs.values():
    if not _lib.has("lv_list_up", "cdecl"):
        continue
    lv_list_up = _lib.get("lv_list_up", "cdecl")
    lv_list_up.argtypes = [POINTER(lv_obj_t)]
    lv_list_up.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 292
for _lib in _libs.values():
    if not _lib.has("lv_list_down", "cdecl"):
        continue
    lv_list_down = _lib.get("lv_list_down", "cdecl")
    lv_list_down.argtypes = [POINTER(lv_obj_t)]
    lv_list_down.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_list.h: 299
for _lib in _libs.values():
    if not _lib.has("lv_list_focus", "cdecl"):
        continue
    lv_list_focus = _lib.get("lv_list_focus", "cdecl")
    lv_list_focus.argtypes = [POINTER(lv_obj_t), lv_anim_enable_t]
    lv_list_focus.restype = None
    break

enum_anon_127 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 41

LV_CHART_TYPE_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 41

LV_CHART_TYPE_LINE = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 41

LV_CHART_TYPE_COLUMN = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 41

lv_chart_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 46

enum_anon_128 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 49

LV_CHART_UPDATE_MODE_SHIFT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 49

LV_CHART_UPDATE_MODE_CIRCULAR = (LV_CHART_UPDATE_MODE_SHIFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 49

lv_chart_update_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 53

enum_anon_129 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 55

LV_CHART_AXIS_PRIMARY_Y = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 55

LV_CHART_AXIS_SECONDARY_Y = (LV_CHART_AXIS_PRIMARY_Y + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 55

_LV_CHART_AXIS_LAST = (LV_CHART_AXIS_SECONDARY_Y + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 55

lv_chart_axis_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 60

enum_anon_130 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

LV_CHART_CURSOR_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

LV_CHART_CURSOR_RIGHT = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

LV_CHART_CURSOR_UP = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

LV_CHART_CURSOR_LEFT = 4# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

LV_CHART_CURSOR_DOWN = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 62

lv_cursor_direction_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 69

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 78
class struct_anon_131(Structure):
    pass

struct_anon_131.__slots__ = [
    'points',
    'color',
    'start_point',
    'ext_buf_assigned',
    'hidden',
    'y_axis',
]
struct_anon_131._fields_ = [
    ('points', POINTER(lv_coord_t)),
    ('color', lv_color_t),
    ('start_point', c_uint16),
    ('ext_buf_assigned', c_uint8, 1),
    ('hidden', c_uint8, 1),
    ('y_axis', lv_chart_axis_t, 1),
]

lv_chart_series_t = struct_anon_131# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 78

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 84
class struct_anon_132(Structure):
    pass

struct_anon_132.__slots__ = [
    'point',
    'color',
    'axes',
]
struct_anon_132._fields_ = [
    ('point', lv_point_t),
    ('color', lv_color_t),
    ('axes', lv_cursor_direction_t, 4),
]

lv_chart_cursor_t = struct_anon_132# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 84

enum_anon_133 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 87

LV_CHART_AXIS_SKIP_LAST_TICK = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 87

LV_CHART_AXIS_DRAW_LAST_TICK = 1# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 87

LV_CHART_AXIS_INVERSE_LABELS_ORDER = 2# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 87

lv_chart_axis_options_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 92

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 100
class struct_anon_134(Structure):
    pass

struct_anon_134.__slots__ = [
    'list_of_values',
    'options',
    'num_tick_marks',
    'major_tick_len',
    'minor_tick_len',
]
struct_anon_134._fields_ = [
    ('list_of_values', String),
    ('options', lv_chart_axis_options_t),
    ('num_tick_marks', c_uint8),
    ('major_tick_len', c_uint8),
    ('minor_tick_len', c_uint8),
]

lv_chart_axis_cfg_t = struct_anon_134# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 100

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 121
class struct_anon_135(Structure):
    pass

struct_anon_135.__slots__ = [
    'series_ll',
    'cursors_ll',
    'ymin',
    'ymax',
    'hdiv_cnt',
    'vdiv_cnt',
    'point_cnt',
    'style_series_bg',
    'style_series',
    'style_cursors',
    'type',
    'y_axis',
    'x_axis',
    'secondary_y_axis',
    'update_mode',
]
struct_anon_135._fields_ = [
    ('series_ll', lv_ll_t),
    ('cursors_ll', lv_ll_t),
    ('ymin', lv_coord_t * int(_LV_CHART_AXIS_LAST)),
    ('ymax', lv_coord_t * int(_LV_CHART_AXIS_LAST)),
    ('hdiv_cnt', c_uint8),
    ('vdiv_cnt', c_uint8),
    ('point_cnt', c_uint16),
    ('style_series_bg', lv_style_list_t),
    ('style_series', lv_style_list_t),
    ('style_cursors', lv_style_list_t),
    ('type', lv_chart_type_t),
    ('y_axis', lv_chart_axis_cfg_t),
    ('x_axis', lv_chart_axis_cfg_t),
    ('secondary_y_axis', lv_chart_axis_cfg_t),
    ('update_mode', c_uint8, 1),
]

lv_chart_ext_t = struct_anon_135# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 121

enum_anon_136 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 124

LV_CHART_PART_BG = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 124

LV_CHART_PART_SERIES_BG = _LV_OBJ_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 124

LV_CHART_PART_SERIES = (LV_CHART_PART_SERIES_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 124

LV_CHART_PART_CURSOR = (LV_CHART_PART_SERIES + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 124

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 142
for _lib in _libs.values():
    if not _lib.has("lv_chart_create", "cdecl"):
        continue
    lv_chart_create = _lib.get("lv_chart_create", "cdecl")
    lv_chart_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_chart_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 154
for _lib in _libs.values():
    if not _lib.has("lv_chart_add_series", "cdecl"):
        continue
    lv_chart_add_series = _lib.get("lv_chart_add_series", "cdecl")
    lv_chart_add_series.argtypes = [POINTER(lv_obj_t), lv_color_t]
    lv_chart_add_series.restype = POINTER(lv_chart_series_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_chart_remove_series", "cdecl"):
        continue
    lv_chart_remove_series = _lib.get("lv_chart_remove_series", "cdecl")
    lv_chart_remove_series.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t)]
    lv_chart_remove_series.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 170
for _lib in _libs.values():
    if not _lib.has("lv_chart_add_cursor", "cdecl"):
        continue
    lv_chart_add_cursor = _lib.get("lv_chart_add_cursor", "cdecl")
    lv_chart_add_cursor.argtypes = [POINTER(lv_obj_t), lv_color_t, lv_cursor_direction_t]
    lv_chart_add_cursor.restype = POINTER(lv_chart_cursor_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 177
for _lib in _libs.values():
    if not _lib.has("lv_chart_clear_series", "cdecl"):
        continue
    lv_chart_clear_series = _lib.get("lv_chart_clear_series", "cdecl")
    lv_chart_clear_series.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t)]
    lv_chart_clear_series.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 185
for _lib in _libs.values():
    if not _lib.has("lv_chart_hide_series", "cdecl"):
        continue
    lv_chart_hide_series = _lib.get("lv_chart_hide_series", "cdecl")
    lv_chart_hide_series.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), c_bool]
    lv_chart_hide_series.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 197
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_div_line_count", "cdecl"):
        continue
    lv_chart_set_div_line_count = _lib.get("lv_chart_set_div_line_count", "cdecl")
    lv_chart_set_div_line_count.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_chart_set_div_line_count.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 206
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_y_range", "cdecl"):
        continue
    lv_chart_set_y_range = _lib.get("lv_chart_set_y_range", "cdecl")
    lv_chart_set_y_range.argtypes = [POINTER(lv_obj_t), lv_chart_axis_t, lv_coord_t, lv_coord_t]
    lv_chart_set_y_range.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 213
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_type", "cdecl"):
        continue
    lv_chart_set_type = _lib.get("lv_chart_set_type", "cdecl")
    lv_chart_set_type.argtypes = [POINTER(lv_obj_t), lv_chart_type_t]
    lv_chart_set_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 220
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_point_count", "cdecl"):
        continue
    lv_chart_set_point_count = _lib.get("lv_chart_set_point_count", "cdecl")
    lv_chart_set_point_count.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_chart_set_point_count.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 228
for _lib in _libs.values():
    if not _lib.has("lv_chart_init_points", "cdecl"):
        continue
    lv_chart_init_points = _lib.get("lv_chart_init_points", "cdecl")
    lv_chart_init_points.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), lv_coord_t]
    lv_chart_init_points.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 236
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_points", "cdecl"):
        continue
    lv_chart_set_points = _lib.get("lv_chart_set_points", "cdecl")
    lv_chart_set_points.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), POINTER(lv_coord_t)]
    lv_chart_set_points.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 244
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_next", "cdecl"):
        continue
    lv_chart_set_next = _lib.get("lv_chart_set_next", "cdecl")
    lv_chart_set_next.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), lv_coord_t]
    lv_chart_set_next.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 251
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_update_mode", "cdecl"):
        continue
    lv_chart_set_update_mode = _lib.get("lv_chart_set_update_mode", "cdecl")
    lv_chart_set_update_mode.argtypes = [POINTER(lv_obj_t), lv_chart_update_mode_t]
    lv_chart_set_update_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 261
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_x_tick_length", "cdecl"):
        continue
    lv_chart_set_x_tick_length = _lib.get("lv_chart_set_x_tick_length", "cdecl")
    lv_chart_set_x_tick_length.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_chart_set_x_tick_length.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 271
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_y_tick_length", "cdecl"):
        continue
    lv_chart_set_y_tick_length = _lib.get("lv_chart_set_y_tick_length", "cdecl")
    lv_chart_set_y_tick_length.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_chart_set_y_tick_length.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 281
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_secondary_y_tick_length", "cdecl"):
        continue
    lv_chart_set_secondary_y_tick_length = _lib.get("lv_chart_set_secondary_y_tick_length", "cdecl")
    lv_chart_set_secondary_y_tick_length.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_chart_set_secondary_y_tick_length.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 291
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_x_tick_texts", "cdecl"):
        continue
    lv_chart_set_x_tick_texts = _lib.get("lv_chart_set_x_tick_texts", "cdecl")
    lv_chart_set_x_tick_texts.argtypes = [POINTER(lv_obj_t), String, c_uint8, lv_chart_axis_options_t]
    lv_chart_set_x_tick_texts.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 302
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_secondary_y_tick_texts", "cdecl"):
        continue
    lv_chart_set_secondary_y_tick_texts = _lib.get("lv_chart_set_secondary_y_tick_texts", "cdecl")
    lv_chart_set_secondary_y_tick_texts.argtypes = [POINTER(lv_obj_t), String, c_uint8, lv_chart_axis_options_t]
    lv_chart_set_secondary_y_tick_texts.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 313
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_y_tick_texts", "cdecl"):
        continue
    lv_chart_set_y_tick_texts = _lib.get("lv_chart_set_y_tick_texts", "cdecl")
    lv_chart_set_y_tick_texts.argtypes = [POINTER(lv_obj_t), String, c_uint8, lv_chart_axis_options_t]
    lv_chart_set_y_tick_texts.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 322
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_x_start_point", "cdecl"):
        continue
    lv_chart_set_x_start_point = _lib.get("lv_chart_set_x_start_point", "cdecl")
    lv_chart_set_x_start_point.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), c_uint16]
    lv_chart_set_x_start_point.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 331
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_ext_array", "cdecl"):
        continue
    lv_chart_set_ext_array = _lib.get("lv_chart_set_ext_array", "cdecl")
    lv_chart_set_ext_array.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), POINTER(lv_coord_t), c_uint16]
    lv_chart_set_ext_array.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 340
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_point_id", "cdecl"):
        continue
    lv_chart_set_point_id = _lib.get("lv_chart_set_point_id", "cdecl")
    lv_chart_set_point_id.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), lv_coord_t, c_uint16]
    lv_chart_set_point_id.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 348
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_series_axis", "cdecl"):
        continue
    lv_chart_set_series_axis = _lib.get("lv_chart_set_series_axis", "cdecl")
    lv_chart_set_series_axis.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), lv_chart_axis_t]
    lv_chart_set_series_axis.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 357
for _lib in _libs.values():
    if not _lib.has("lv_chart_set_cursor_point", "cdecl"):
        continue
    lv_chart_set_cursor_point = _lib.get("lv_chart_set_cursor_point", "cdecl")
    lv_chart_set_cursor_point.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_cursor_t), POINTER(lv_point_t)]
    lv_chart_set_cursor_point.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 368
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_type", "cdecl"):
        continue
    lv_chart_get_type = _lib.get("lv_chart_get_type", "cdecl")
    lv_chart_get_type.argtypes = [POINTER(lv_obj_t)]
    lv_chart_get_type.restype = lv_chart_type_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 375
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_point_count", "cdecl"):
        continue
    lv_chart_get_point_count = _lib.get("lv_chart_get_point_count", "cdecl")
    lv_chart_get_point_count.argtypes = [POINTER(lv_obj_t)]
    lv_chart_get_point_count.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 382
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_x_start_point", "cdecl"):
        continue
    lv_chart_get_x_start_point = _lib.get("lv_chart_get_x_start_point", "cdecl")
    lv_chart_get_x_start_point.argtypes = [POINTER(lv_chart_series_t)]
    lv_chart_get_x_start_point.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 391
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_point_id", "cdecl"):
        continue
    lv_chart_get_point_id = _lib.get("lv_chart_get_point_id", "cdecl")
    lv_chart_get_point_id.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), c_uint16]
    lv_chart_get_point_id.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 399
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_series_axis", "cdecl"):
        continue
    lv_chart_get_series_axis = _lib.get("lv_chart_get_series_axis", "cdecl")
    lv_chart_get_series_axis.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t)]
    lv_chart_get_series_axis.restype = lv_chart_axis_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 406
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_series_area", "cdecl"):
        continue
    lv_chart_get_series_area = _lib.get("lv_chart_get_series_area", "cdecl")
    lv_chart_get_series_area.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t)]
    lv_chart_get_series_area.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 415
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_cursor_point", "cdecl"):
        continue
    lv_chart_get_cursor_point = _lib.get("lv_chart_get_cursor_point", "cdecl")
    lv_chart_get_cursor_point.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_cursor_t)]
    lv_chart_get_cursor_point.restype = lv_point_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 423
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_nearest_index_from_coord", "cdecl"):
        continue
    lv_chart_get_nearest_index_from_coord = _lib.get("lv_chart_get_nearest_index_from_coord", "cdecl")
    lv_chart_get_nearest_index_from_coord.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_chart_get_nearest_index_from_coord.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 433
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_x_from_index", "cdecl"):
        continue
    lv_chart_get_x_from_index = _lib.get("lv_chart_get_x_from_index", "cdecl")
    lv_chart_get_x_from_index.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), c_uint16]
    lv_chart_get_x_from_index.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 443
for _lib in _libs.values():
    if not _lib.has("lv_chart_get_y_from_index", "cdecl"):
        continue
    lv_chart_get_y_from_index = _lib.get("lv_chart_get_y_from_index", "cdecl")
    lv_chart_get_y_from_index.argtypes = [POINTER(lv_obj_t), POINTER(lv_chart_series_t), c_uint16]
    lv_chart_get_y_from_index.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 453
for _lib in _libs.values():
    if not _lib.has("lv_chart_refresh", "cdecl"):
        continue
    lv_chart_refresh = _lib.get("lv_chart_refresh", "cdecl")
    lv_chart_refresh.argtypes = [POINTER(lv_obj_t)]
    lv_chart_refresh.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 56
class struct_anon_137(Structure):
    pass

struct_anon_137.__slots__ = [
    'align',
    'right_merge',
    'type',
    'crop',
]
struct_anon_137._fields_ = [
    ('align', c_uint8, 2),
    ('right_merge', c_uint8, 1),
    ('type', c_uint8, 4),
    ('crop', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 63
class union_anon_138(Union):
    pass

union_anon_138.__slots__ = [
    's',
    'format_byte',
]
union_anon_138._fields_ = [
    ('s', struct_anon_137),
    ('format_byte', c_uint8),
]

lv_table_cell_format_t = union_anon_138# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 63

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 76
class struct_anon_139(Structure):
    pass

struct_anon_139.__slots__ = [
    'col_cnt',
    'row_cnt',
    'cell_data',
    'row_h',
    'cell_style',
    'col_w',
    'cell_types',
]
struct_anon_139._fields_ = [
    ('col_cnt', c_uint16),
    ('row_cnt', c_uint16),
    ('cell_data', POINTER(POINTER(c_char))),
    ('row_h', POINTER(lv_coord_t)),
    ('cell_style', lv_style_list_t * int(4)),
    ('col_w', lv_coord_t * int(12)),
    ('cell_types', c_uint16, 4),
]

lv_table_ext_t = struct_anon_139# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 76

enum_anon_140 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

LV_TABLE_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

LV_TABLE_PART_CELL1 = (LV_TABLE_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

LV_TABLE_PART_CELL2 = (LV_TABLE_PART_CELL1 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

LV_TABLE_PART_CELL3 = (LV_TABLE_PART_CELL2 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

LV_TABLE_PART_CELL4 = (LV_TABLE_PART_CELL3 + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 79

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 98
for _lib in _libs.values():
    if not _lib.has("lv_table_create", "cdecl"):
        continue
    lv_table_create = _lib.get("lv_table_create", "cdecl")
    lv_table_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_table_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 112
for _lib in _libs.values():
    if not _lib.has("lv_table_set_cell_value", "cdecl"):
        continue
    lv_table_set_cell_value = _lib.get("lv_table_set_cell_value", "cdecl")
    lv_table_set_cell_value.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, String]
    lv_table_set_cell_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 121
for _lib in _libs.values():
    if _lib.has("lv_table_set_cell_value_fmt", "cdecl"):
        _func = _lib.get("lv_table_set_cell_value_fmt", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, String]
        lv_table_set_cell_value_fmt = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 128
for _lib in _libs.values():
    if not _lib.has("lv_table_set_row_cnt", "cdecl"):
        continue
    lv_table_set_row_cnt = _lib.get("lv_table_set_row_cnt", "cdecl")
    lv_table_set_row_cnt.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_table_set_row_cnt.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 135
for _lib in _libs.values():
    if not _lib.has("lv_table_set_col_cnt", "cdecl"):
        continue
    lv_table_set_col_cnt = _lib.get("lv_table_set_col_cnt", "cdecl")
    lv_table_set_col_cnt.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_table_set_col_cnt.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 143
for _lib in _libs.values():
    if not _lib.has("lv_table_set_col_width", "cdecl"):
        continue
    lv_table_set_col_width = _lib.get("lv_table_set_col_width", "cdecl")
    lv_table_set_col_width.argtypes = [POINTER(lv_obj_t), c_uint16, lv_coord_t]
    lv_table_set_col_width.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 152
for _lib in _libs.values():
    if not _lib.has("lv_table_set_cell_align", "cdecl"):
        continue
    lv_table_set_cell_align = _lib.get("lv_table_set_cell_align", "cdecl")
    lv_table_set_cell_align.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, lv_label_align_t]
    lv_table_set_cell_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_table_set_cell_type", "cdecl"):
        continue
    lv_table_set_cell_type = _lib.get("lv_table_set_cell_type", "cdecl")
    lv_table_set_cell_type.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, c_uint8]
    lv_table_set_cell_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 170
for _lib in _libs.values():
    if not _lib.has("lv_table_set_cell_crop", "cdecl"):
        continue
    lv_table_set_cell_crop = _lib.get("lv_table_set_cell_crop", "cdecl")
    lv_table_set_cell_crop.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, c_bool]
    lv_table_set_cell_crop.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 179
for _lib in _libs.values():
    if not _lib.has("lv_table_set_cell_merge_right", "cdecl"):
        continue
    lv_table_set_cell_merge_right = _lib.get("lv_table_set_cell_merge_right", "cdecl")
    lv_table_set_cell_merge_right.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16, c_bool]
    lv_table_set_cell_merge_right.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 192
for _lib in _libs.values():
    if not _lib.has("lv_table_get_cell_value", "cdecl"):
        continue
    lv_table_get_cell_value = _lib.get("lv_table_get_cell_value", "cdecl")
    lv_table_get_cell_value.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_table_get_cell_value.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 199
for _lib in _libs.values():
    if not _lib.has("lv_table_get_row_cnt", "cdecl"):
        continue
    lv_table_get_row_cnt = _lib.get("lv_table_get_row_cnt", "cdecl")
    lv_table_get_row_cnt.argtypes = [POINTER(lv_obj_t)]
    lv_table_get_row_cnt.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 206
for _lib in _libs.values():
    if not _lib.has("lv_table_get_col_cnt", "cdecl"):
        continue
    lv_table_get_col_cnt = _lib.get("lv_table_get_col_cnt", "cdecl")
    lv_table_get_col_cnt.argtypes = [POINTER(lv_obj_t)]
    lv_table_get_col_cnt.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 214
for _lib in _libs.values():
    if not _lib.has("lv_table_get_col_width", "cdecl"):
        continue
    lv_table_get_col_width = _lib.get("lv_table_get_col_width", "cdecl")
    lv_table_get_col_width.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_table_get_col_width.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 224
for _lib in _libs.values():
    if not _lib.has("lv_table_get_cell_align", "cdecl"):
        continue
    lv_table_get_cell_align = _lib.get("lv_table_get_cell_align", "cdecl")
    lv_table_get_cell_align.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_table_get_cell_align.restype = lv_label_align_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 233
for _lib in _libs.values():
    if not _lib.has("lv_table_get_cell_type", "cdecl"):
        continue
    lv_table_get_cell_type = _lib.get("lv_table_get_cell_type", "cdecl")
    lv_table_get_cell_type.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_table_get_cell_type.restype = lv_label_align_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 242
for _lib in _libs.values():
    if not _lib.has("lv_table_get_cell_crop", "cdecl"):
        continue
    lv_table_get_cell_crop = _lib.get("lv_table_get_cell_crop", "cdecl")
    lv_table_get_cell_crop.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_table_get_cell_crop.restype = lv_label_align_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 251
for _lib in _libs.values():
    if not _lib.has("lv_table_get_cell_merge_right", "cdecl"):
        continue
    lv_table_get_cell_merge_right = _lib.get("lv_table_get_cell_merge_right", "cdecl")
    lv_table_get_cell_merge_right.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_table_get_cell_merge_right.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_table.h: 260
for _lib in _libs.values():
    if not _lib.has("lv_table_get_pressed_cell", "cdecl"):
        continue
    lv_table_get_pressed_cell = _lib.get("lv_table_get_pressed_cell", "cdecl")
    lv_table_get_pressed_cell.argtypes = [POINTER(lv_obj_t), POINTER(c_uint16), POINTER(c_uint16)]
    lv_table_get_pressed_cell.restype = lv_res_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 47
class struct_anon_141(Structure):
    pass

struct_anon_141.__slots__ = [
    'bg_btn',
    'bullet',
    'label',
]
struct_anon_141._fields_ = [
    ('bg_btn', lv_btn_ext_t),
    ('bullet', POINTER(lv_obj_t)),
    ('label', POINTER(lv_obj_t)),
]

lv_checkbox_ext_t = struct_anon_141# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 47

enum_anon_142 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 50

LV_CHECKBOX_PART_BG = LV_BTN_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 50

_LV_CHECKBOX_PART_VIRTUAL_LAST = (LV_CHECKBOX_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 50

LV_CHECKBOX_PART_BULLET = _LV_BTN_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 50

_LV_CHECKBOX_PART_REAL_LAST = (LV_CHECKBOX_PART_BULLET + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 50

lv_checkbox_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 56

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 68
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_create", "cdecl"):
        continue
    lv_checkbox_create = _lib.get("lv_checkbox_create", "cdecl")
    lv_checkbox_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_checkbox_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 80
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_set_text", "cdecl"):
        continue
    lv_checkbox_set_text = _lib.get("lv_checkbox_set_text", "cdecl")
    lv_checkbox_set_text.argtypes = [POINTER(lv_obj_t), String]
    lv_checkbox_set_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_set_text_static", "cdecl"):
        continue
    lv_checkbox_set_text_static = _lib.get("lv_checkbox_set_text_static", "cdecl")
    lv_checkbox_set_text_static.argtypes = [POINTER(lv_obj_t), String]
    lv_checkbox_set_text_static.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_set_checked", "cdecl"):
        continue
    lv_checkbox_set_checked = _lib.get("lv_checkbox_set_checked", "cdecl")
    lv_checkbox_set_checked.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_checkbox_set_checked.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 101
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_set_disabled", "cdecl"):
        continue
    lv_checkbox_set_disabled = _lib.get("lv_checkbox_set_disabled", "cdecl")
    lv_checkbox_set_disabled.argtypes = [POINTER(lv_obj_t)]
    lv_checkbox_set_disabled.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 108
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_set_state", "cdecl"):
        continue
    lv_checkbox_set_state = _lib.get("lv_checkbox_set_state", "cdecl")
    lv_checkbox_set_state.argtypes = [POINTER(lv_obj_t), lv_btn_state_t]
    lv_checkbox_set_state.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_checkbox.h: 118
for _lib in _libs.values():
    if not _lib.has("lv_checkbox_get_text", "cdecl"):
        continue
    lv_checkbox_get_text = _lib.get("lv_checkbox_get_text", "cdecl")
    lv_checkbox_get_text.argtypes = [POINTER(lv_obj_t)]
    lv_checkbox_get_text.restype = c_char_p
    break

enum_anon_143 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 30

LV_CPICKER_TYPE_RECT = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 30

LV_CPICKER_TYPE_DISC = (LV_CPICKER_TYPE_RECT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 30

lv_cpicker_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 34

enum_anon_144 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 36

LV_CPICKER_COLOR_MODE_HUE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 36

LV_CPICKER_COLOR_MODE_SATURATION = (LV_CPICKER_COLOR_MODE_HUE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 36

LV_CPICKER_COLOR_MODE_VALUE = (LV_CPICKER_COLOR_MODE_SATURATION + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 36

lv_cpicker_color_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 41

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 46
class struct_anon_145(Structure):
    pass

struct_anon_145.__slots__ = [
    'style_list',
    'pos',
    'colored',
]
struct_anon_145._fields_ = [
    ('style_list', lv_style_list_t),
    ('pos', lv_point_t),
    ('colored', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 58
class struct_anon_146(Structure):
    pass

struct_anon_146.__slots__ = [
    'hsv',
    'knob',
    'last_click_time',
    'last_change_time',
    'last_press_point',
    'color_mode',
    'color_mode_fixed',
    'type',
]
struct_anon_146._fields_ = [
    ('hsv', lv_color_hsv_t),
    ('knob', struct_anon_145),
    ('last_click_time', c_uint32),
    ('last_change_time', c_uint32),
    ('last_press_point', lv_point_t),
    ('color_mode', lv_cpicker_color_mode_t, 2),
    ('color_mode_fixed', c_uint8, 1),
    ('type', lv_cpicker_type_t, 1),
]

lv_cpicker_ext_t = struct_anon_146# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 58

enum_anon_147 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 61

LV_CPICKER_PART_MAIN = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 61

LV_CPICKER_PART_KNOB = _LV_OBJ_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 61

_LV_CPICKER_PART_VIRTUAL_LAST = (LV_CPICKER_PART_KNOB + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 61

_LV_CPICKER_PART_REAL_LAST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 61

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 78
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_create", "cdecl"):
        continue
    lv_cpicker_create = _lib.get("lv_cpicker_create", "cdecl")
    lv_cpicker_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_cpicker_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_type", "cdecl"):
        continue
    lv_cpicker_set_type = _lib.get("lv_cpicker_set_type", "cdecl")
    lv_cpicker_set_type.argtypes = [POINTER(lv_obj_t), lv_cpicker_type_t]
    lv_cpicker_set_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 97
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_hue", "cdecl"):
        continue
    lv_cpicker_set_hue = _lib.get("lv_cpicker_set_hue", "cdecl")
    lv_cpicker_set_hue.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_cpicker_set_hue.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 105
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_saturation", "cdecl"):
        continue
    lv_cpicker_set_saturation = _lib.get("lv_cpicker_set_saturation", "cdecl")
    lv_cpicker_set_saturation.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_cpicker_set_saturation.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_value", "cdecl"):
        continue
    lv_cpicker_set_value = _lib.get("lv_cpicker_set_value", "cdecl")
    lv_cpicker_set_value.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_cpicker_set_value.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 121
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_hsv", "cdecl"):
        continue
    lv_cpicker_set_hsv = _lib.get("lv_cpicker_set_hsv", "cdecl")
    lv_cpicker_set_hsv.argtypes = [POINTER(lv_obj_t), lv_color_hsv_t]
    lv_cpicker_set_hsv.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_color", "cdecl"):
        continue
    lv_cpicker_set_color = _lib.get("lv_cpicker_set_color", "cdecl")
    lv_cpicker_set_color.argtypes = [POINTER(lv_obj_t), lv_color_t]
    lv_cpicker_set_color.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 136
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_color_mode", "cdecl"):
        continue
    lv_cpicker_set_color_mode = _lib.get("lv_cpicker_set_color_mode", "cdecl")
    lv_cpicker_set_color_mode.argtypes = [POINTER(lv_obj_t), lv_cpicker_color_mode_t]
    lv_cpicker_set_color_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 143
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_color_mode_fixed", "cdecl"):
        continue
    lv_cpicker_set_color_mode_fixed = _lib.get("lv_cpicker_set_color_mode_fixed", "cdecl")
    lv_cpicker_set_color_mode_fixed.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_cpicker_set_color_mode_fixed.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_set_knob_colored", "cdecl"):
        continue
    lv_cpicker_set_knob_colored = _lib.get("lv_cpicker_set_knob_colored", "cdecl")
    lv_cpicker_set_knob_colored.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_cpicker_set_knob_colored.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_color_mode", "cdecl"):
        continue
    lv_cpicker_get_color_mode = _lib.get("lv_cpicker_get_color_mode", "cdecl")
    lv_cpicker_get_color_mode.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_color_mode.restype = lv_cpicker_color_mode_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 168
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_color_mode_fixed", "cdecl"):
        continue
    lv_cpicker_get_color_mode_fixed = _lib.get("lv_cpicker_get_color_mode_fixed", "cdecl")
    lv_cpicker_get_color_mode_fixed.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_color_mode_fixed.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 175
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_hue", "cdecl"):
        continue
    lv_cpicker_get_hue = _lib.get("lv_cpicker_get_hue", "cdecl")
    lv_cpicker_get_hue.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_hue.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 182
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_saturation", "cdecl"):
        continue
    lv_cpicker_get_saturation = _lib.get("lv_cpicker_get_saturation", "cdecl")
    lv_cpicker_get_saturation.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_saturation.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 189
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_value", "cdecl"):
        continue
    lv_cpicker_get_value = _lib.get("lv_cpicker_get_value", "cdecl")
    lv_cpicker_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_value.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 196
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_hsv", "cdecl"):
        continue
    lv_cpicker_get_hsv = _lib.get("lv_cpicker_get_hsv", "cdecl")
    lv_cpicker_get_hsv.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_hsv.restype = lv_color_hsv_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 203
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_color", "cdecl"):
        continue
    lv_cpicker_get_color = _lib.get("lv_cpicker_get_color", "cdecl")
    lv_cpicker_get_color.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_color.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_cpicker.h: 210
for _lib in _libs.values():
    if not _lib.has("lv_cpicker_get_knob_colored", "cdecl"):
        continue
    lv_cpicker_get_knob_colored = _lib.get("lv_cpicker_get_knob_colored", "cdecl")
    lv_cpicker_get_knob_colored.argtypes = [POINTER(lv_obj_t)]
    lv_cpicker_get_knob_colored.restype = c_bool
    break

enum_anon_148 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 46

LV_BAR_TYPE_NORMAL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 46

LV_BAR_TYPE_SYMMETRICAL = (LV_BAR_TYPE_NORMAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 46

LV_BAR_TYPE_CUSTOM = (LV_BAR_TYPE_SYMMETRICAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 46

lv_bar_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 51

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 59
class struct_anon_149(Structure):
    pass

struct_anon_149.__slots__ = [
    'bar',
    'anim_start',
    'anim_end',
    'anim_state',
]
struct_anon_149._fields_ = [
    ('bar', POINTER(lv_obj_t)),
    ('anim_start', lv_anim_value_t),
    ('anim_end', lv_anim_value_t),
    ('anim_state', lv_anim_value_t),
]

lv_bar_anim_t = struct_anon_149# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 59

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 79
class struct_anon_150(Structure):
    pass

struct_anon_150.__slots__ = [
    'cur_value',
    'min_value',
    'max_value',
    'start_value',
    'indic_area',
    'anim_time',
    'cur_value_anim',
    'start_value_anim',
    'type',
    'style_indic',
]
struct_anon_150._fields_ = [
    ('cur_value', c_int16),
    ('min_value', c_int16),
    ('max_value', c_int16),
    ('start_value', c_int16),
    ('indic_area', lv_area_t),
    ('anim_time', lv_anim_value_t),
    ('cur_value_anim', lv_bar_anim_t),
    ('start_value_anim', lv_bar_anim_t),
    ('type', c_uint8, 2),
    ('style_indic', lv_style_list_t),
]

lv_bar_ext_t = struct_anon_150# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 79

enum_anon_151 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 82

LV_BAR_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 82

LV_BAR_PART_INDIC = (LV_BAR_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 82

_LV_BAR_PART_VIRTUAL_LAST = (LV_BAR_PART_INDIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 82

lv_bar_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 87

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 99
for _lib in _libs.values():
    if not _lib.has("lv_bar_create", "cdecl"):
        continue
    lv_bar_create = _lib.get("lv_bar_create", "cdecl")
    lv_bar_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_bar_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 111
for _lib in _libs.values():
    if not _lib.has("lv_bar_set_value", "cdecl"):
        continue
    lv_bar_set_value = _lib.get("lv_bar_set_value", "cdecl")
    lv_bar_set_value.argtypes = [POINTER(lv_obj_t), c_int16, lv_anim_enable_t]
    lv_bar_set_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 119
for _lib in _libs.values():
    if not _lib.has("lv_bar_set_start_value", "cdecl"):
        continue
    lv_bar_set_start_value = _lib.get("lv_bar_set_start_value", "cdecl")
    lv_bar_set_start_value.argtypes = [POINTER(lv_obj_t), c_int16, lv_anim_enable_t]
    lv_bar_set_start_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_bar_set_range", "cdecl"):
        continue
    lv_bar_set_range = _lib.get("lv_bar_set_range", "cdecl")
    lv_bar_set_range.argtypes = [POINTER(lv_obj_t), c_int16, c_int16]
    lv_bar_set_range.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_bar_set_type", "cdecl"):
        continue
    lv_bar_set_type = _lib.get("lv_bar_set_type", "cdecl")
    lv_bar_set_type.argtypes = [POINTER(lv_obj_t), lv_bar_type_t]
    lv_bar_set_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 141
for _lib in _libs.values():
    if not _lib.has("lv_bar_set_anim_time", "cdecl"):
        continue
    lv_bar_set_anim_time = _lib.get("lv_bar_set_anim_time", "cdecl")
    lv_bar_set_anim_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_bar_set_anim_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 152
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_value", "cdecl"):
        continue
    lv_bar_get_value = _lib.get("lv_bar_get_value", "cdecl")
    lv_bar_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 159
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_start_value", "cdecl"):
        continue
    lv_bar_get_start_value = _lib.get("lv_bar_get_start_value", "cdecl")
    lv_bar_get_start_value.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_start_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 166
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_min_value", "cdecl"):
        continue
    lv_bar_get_min_value = _lib.get("lv_bar_get_min_value", "cdecl")
    lv_bar_get_min_value.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_min_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 173
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_max_value", "cdecl"):
        continue
    lv_bar_get_max_value = _lib.get("lv_bar_get_max_value", "cdecl")
    lv_bar_get_max_value.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_max_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 180
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_type", "cdecl"):
        continue
    lv_bar_get_type = _lib.get("lv_bar_get_type", "cdecl")
    lv_bar_get_type.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_type.restype = lv_bar_type_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 187
for _lib in _libs.values():
    if not _lib.has("lv_bar_get_anim_time", "cdecl"):
        continue
    lv_bar_get_anim_time = _lib.get("lv_bar_get_anim_time", "cdecl")
    lv_bar_get_anim_time.argtypes = [POINTER(lv_obj_t)]
    lv_bar_get_anim_time.restype = c_uint16
    break

enum_anon_152 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 36

LV_SLIDER_TYPE_NORMAL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 36

LV_SLIDER_TYPE_SYMMETRICAL = (LV_SLIDER_TYPE_NORMAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 36

LV_SLIDER_TYPE_RANGE = (LV_SLIDER_TYPE_SYMMETRICAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 36

lv_slider_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 41

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 53
class struct_anon_153(Structure):
    pass

struct_anon_153.__slots__ = [
    'bar',
    'style_knob',
    'left_knob_area',
    'right_knob_area',
    'value_to_set',
    'dragging',
    'left_knob_focus',
]
struct_anon_153._fields_ = [
    ('bar', lv_bar_ext_t),
    ('style_knob', lv_style_list_t),
    ('left_knob_area', lv_area_t),
    ('right_knob_area', lv_area_t),
    ('value_to_set', POINTER(c_int16)),
    ('dragging', c_uint8, 1),
    ('left_knob_focus', c_uint8, 1),
]

lv_slider_ext_t = struct_anon_153# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 53

enum_anon_154 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 56

LV_SLIDER_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 56

LV_SLIDER_PART_INDIC = (LV_SLIDER_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 56

LV_SLIDER_PART_KNOB = (LV_SLIDER_PART_INDIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 56

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 72
for _lib in _libs.values():
    if not _lib.has("lv_slider_create", "cdecl"):
        continue
    lv_slider_create = _lib.get("lv_slider_create", "cdecl")
    lv_slider_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_slider_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 146
for _lib in _libs.values():
    if not _lib.has("lv_slider_get_value", "cdecl"):
        continue
    lv_slider_get_value = _lib.get("lv_slider_get_value", "cdecl")
    lv_slider_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_slider_get_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 183
for _lib in _libs.values():
    if not _lib.has("lv_slider_is_dragged", "cdecl"):
        continue
    lv_slider_is_dragged = _lib.get("lv_slider_is_dragged", "cdecl")
    lv_slider_is_dragged.argtypes = [POINTER(lv_obj_t)]
    lv_slider_is_dragged.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_slider.h: 202
for _lib in _libs.values():
    try:
        type = (lv_bar_type_t).in_dll(_lib, "type")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 35
class struct_anon_155(Structure):
    pass

struct_anon_155.__slots__ = [
    'bright',
]
struct_anon_155._fields_ = [
    ('bright', c_uint8),
]

lv_led_ext_t = struct_anon_155# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 35

enum_anon_156 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 38

LV_LED_PART_MAIN = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 38

lv_led_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 41

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 53
for _lib in _libs.values():
    if not _lib.has("lv_led_create", "cdecl"):
        continue
    lv_led_create = _lib.get("lv_led_create", "cdecl")
    lv_led_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_led_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 60
for _lib in _libs.values():
    if not _lib.has("lv_led_set_bright", "cdecl"):
        continue
    lv_led_set_bright = _lib.get("lv_led_set_bright", "cdecl")
    lv_led_set_bright.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_led_set_bright.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 66
for _lib in _libs.values():
    if not _lib.has("lv_led_on", "cdecl"):
        continue
    lv_led_on = _lib.get("lv_led_on", "cdecl")
    lv_led_on.argtypes = [POINTER(lv_obj_t)]
    lv_led_on.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 72
for _lib in _libs.values():
    if not _lib.has("lv_led_off", "cdecl"):
        continue
    lv_led_off = _lib.get("lv_led_off", "cdecl")
    lv_led_off.argtypes = [POINTER(lv_obj_t)]
    lv_led_off.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 78
for _lib in _libs.values():
    if not _lib.has("lv_led_toggle", "cdecl"):
        continue
    lv_led_toggle = _lib.get("lv_led_toggle", "cdecl")
    lv_led_toggle.argtypes = [POINTER(lv_obj_t)]
    lv_led_toggle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_led.h: 85
for _lib in _libs.values():
    if not _lib.has("lv_led_get_bright", "cdecl"):
        continue
    lv_led_get_bright = _lib.get("lv_led_get_bright", "cdecl")
    lv_led_get_bright.argtypes = [POINTER(lv_obj_t)]
    lv_led_get_bright.restype = c_uint8
    break

enum_anon_157 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_HIDDEN = 8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_NO_REPEAT = 16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_DISABLED = 32# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_CHECKABLE = 64# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_CHECK_STATE = 128# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

LV_BTNMATRIX_CTRL_CLICK_TRIG = 256# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 38

lv_btnmatrix_ctrl_t = c_uint16# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 46

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 63
class struct_anon_158(Structure):
    pass

struct_anon_158.__slots__ = [
    'map_p',
    'button_areas',
    'ctrl_bits',
    'style_btn',
    'btn_cnt',
    'btn_id_pr',
    'btn_id_focused',
    'btn_id_act',
    'recolor',
    'one_check',
    'align',
]
struct_anon_158._fields_ = [
    ('map_p', POINTER(POINTER(c_char))),
    ('button_areas', POINTER(lv_area_t)),
    ('ctrl_bits', POINTER(lv_btnmatrix_ctrl_t)),
    ('style_btn', lv_style_list_t),
    ('btn_cnt', c_uint16),
    ('btn_id_pr', c_uint16),
    ('btn_id_focused', c_uint16),
    ('btn_id_act', c_uint16),
    ('recolor', c_uint8, 1),
    ('one_check', c_uint8, 1),
    ('align', c_uint8, 2),
]

lv_btnmatrix_ext_t = struct_anon_158# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 63

enum_anon_159 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 65

LV_BTNMATRIX_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 65

LV_BTNMATRIX_PART_BTN = (LV_BTNMATRIX_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 65

lv_btnmatrix_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 69

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_create", "cdecl"):
        continue
    lv_btnmatrix_create = _lib.get("lv_btnmatrix_create", "cdecl")
    lv_btnmatrix_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_btnmatrix_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_map", "cdecl"):
        continue
    lv_btnmatrix_set_map = _lib.get("lv_btnmatrix_set_map", "cdecl")
    lv_btnmatrix_set_map.argtypes = [POINTER(lv_obj_t), POINTER(POINTER(c_char))]
    lv_btnmatrix_set_map.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_ctrl_map", "cdecl"):
        continue
    lv_btnmatrix_set_ctrl_map = _lib.get("lv_btnmatrix_set_ctrl_map", "cdecl")
    lv_btnmatrix_set_ctrl_map.argtypes = [POINTER(lv_obj_t), POINTER(lv_btnmatrix_ctrl_t)]
    lv_btnmatrix_set_ctrl_map.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 116
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_focused_btn", "cdecl"):
        continue
    lv_btnmatrix_set_focused_btn = _lib.get("lv_btnmatrix_set_focused_btn", "cdecl")
    lv_btnmatrix_set_focused_btn.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_btnmatrix_set_focused_btn.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 123
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_recolor", "cdecl"):
        continue
    lv_btnmatrix_set_recolor = _lib.get("lv_btnmatrix_set_recolor", "cdecl")
    lv_btnmatrix_set_recolor.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_btnmatrix_set_recolor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 130
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_btn_ctrl", "cdecl"):
        continue
    lv_btnmatrix_set_btn_ctrl = _lib.get("lv_btnmatrix_set_btn_ctrl", "cdecl")
    lv_btnmatrix_set_btn_ctrl.argtypes = [POINTER(lv_obj_t), c_uint16, lv_btnmatrix_ctrl_t]
    lv_btnmatrix_set_btn_ctrl.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 137
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_clear_btn_ctrl", "cdecl"):
        continue
    lv_btnmatrix_clear_btn_ctrl = _lib.get("lv_btnmatrix_clear_btn_ctrl", "cdecl")
    lv_btnmatrix_clear_btn_ctrl.argtypes = [POINTER(lv_obj_t), c_uint16, lv_btnmatrix_ctrl_t]
    lv_btnmatrix_clear_btn_ctrl.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 144
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_btn_ctrl_all", "cdecl"):
        continue
    lv_btnmatrix_set_btn_ctrl_all = _lib.get("lv_btnmatrix_set_btn_ctrl_all", "cdecl")
    lv_btnmatrix_set_btn_ctrl_all.argtypes = [POINTER(lv_obj_t), lv_btnmatrix_ctrl_t]
    lv_btnmatrix_set_btn_ctrl_all.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 152
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_clear_btn_ctrl_all", "cdecl"):
        continue
    lv_btnmatrix_clear_btn_ctrl_all = _lib.get("lv_btnmatrix_clear_btn_ctrl_all", "cdecl")
    lv_btnmatrix_clear_btn_ctrl_all.argtypes = [POINTER(lv_obj_t), lv_btnmatrix_ctrl_t]
    lv_btnmatrix_clear_btn_ctrl_all.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 163
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_btn_width", "cdecl"):
        continue
    lv_btnmatrix_set_btn_width = _lib.get("lv_btnmatrix_set_btn_width", "cdecl")
    lv_btnmatrix_set_btn_width.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint8]
    lv_btnmatrix_set_btn_width.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 172
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_one_check", "cdecl"):
        continue
    lv_btnmatrix_set_one_check = _lib.get("lv_btnmatrix_set_one_check", "cdecl")
    lv_btnmatrix_set_one_check.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_btnmatrix_set_one_check.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 179
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_set_align", "cdecl"):
        continue
    lv_btnmatrix_set_align = _lib.get("lv_btnmatrix_set_align", "cdecl")
    lv_btnmatrix_set_align.argtypes = [POINTER(lv_obj_t), lv_label_align_t]
    lv_btnmatrix_set_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 190
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_map_array", "cdecl"):
        continue
    lv_btnmatrix_get_map_array = _lib.get("lv_btnmatrix_get_map_array", "cdecl")
    lv_btnmatrix_get_map_array.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_map_array.restype = POINTER(POINTER(c_char))
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 197
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_recolor", "cdecl"):
        continue
    lv_btnmatrix_get_recolor = _lib.get("lv_btnmatrix_get_recolor", "cdecl")
    lv_btnmatrix_get_recolor.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_recolor.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 205
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_active_btn", "cdecl"):
        continue
    lv_btnmatrix_get_active_btn = _lib.get("lv_btnmatrix_get_active_btn", "cdecl")
    lv_btnmatrix_get_active_btn.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_active_btn.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 213
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_active_btn_text", "cdecl"):
        continue
    lv_btnmatrix_get_active_btn_text = _lib.get("lv_btnmatrix_get_active_btn_text", "cdecl")
    lv_btnmatrix_get_active_btn_text.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_active_btn_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 220
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_focused_btn", "cdecl"):
        continue
    lv_btnmatrix_get_focused_btn = _lib.get("lv_btnmatrix_get_focused_btn", "cdecl")
    lv_btnmatrix_get_focused_btn.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_focused_btn.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_btn_text", "cdecl"):
        continue
    lv_btnmatrix_get_btn_text = _lib.get("lv_btnmatrix_get_btn_text", "cdecl")
    lv_btnmatrix_get_btn_text.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_btnmatrix_get_btn_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 239
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_btn_ctrl", "cdecl"):
        continue
    lv_btnmatrix_get_btn_ctrl = _lib.get("lv_btnmatrix_get_btn_ctrl", "cdecl")
    lv_btnmatrix_get_btn_ctrl.argtypes = [POINTER(lv_obj_t), c_uint16, lv_btnmatrix_ctrl_t]
    lv_btnmatrix_get_btn_ctrl.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 246
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_one_check", "cdecl"):
        continue
    lv_btnmatrix_get_one_check = _lib.get("lv_btnmatrix_get_one_check", "cdecl")
    lv_btnmatrix_get_one_check.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_one_check.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 253
for _lib in _libs.values():
    if not _lib.has("lv_btnmatrix_get_align", "cdecl"):
        continue
    lv_btnmatrix_get_align = _lib.get("lv_btnmatrix_get_align", "cdecl")
    lv_btnmatrix_get_align.argtypes = [POINTER(lv_obj_t)]
    lv_btnmatrix_get_align.restype = lv_label_align_t
    break

enum_anon_160 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 42

LV_KEYBOARD_MODE_TEXT_LOWER = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 42

LV_KEYBOARD_MODE_TEXT_UPPER = (LV_KEYBOARD_MODE_TEXT_LOWER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 42

LV_KEYBOARD_MODE_SPECIAL = (LV_KEYBOARD_MODE_TEXT_UPPER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 42

LV_KEYBOARD_MODE_NUM = (LV_KEYBOARD_MODE_SPECIAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 42

lv_keyboard_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 48

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 57
class struct_anon_161(Structure):
    pass

struct_anon_161.__slots__ = [
    'btnm',
    'ta',
    'mode',
    'cursor_mng',
]
struct_anon_161._fields_ = [
    ('btnm', lv_btnmatrix_ext_t),
    ('ta', POINTER(lv_obj_t)),
    ('mode', lv_keyboard_mode_t),
    ('cursor_mng', c_uint8, 1),
]

lv_keyboard_ext_t = struct_anon_161# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 57

enum_anon_162 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 59

LV_KEYBOARD_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 59

LV_KEYBOARD_PART_BTN = (LV_KEYBOARD_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 59

lv_keyboard_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 63

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_create", "cdecl"):
        continue
    lv_keyboard_create = _lib.get("lv_keyboard_create", "cdecl")
    lv_keyboard_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_keyboard_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 86
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_set_textarea", "cdecl"):
        continue
    lv_keyboard_set_textarea = _lib.get("lv_keyboard_set_textarea", "cdecl")
    lv_keyboard_set_textarea.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_keyboard_set_textarea.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 93
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_set_mode", "cdecl"):
        continue
    lv_keyboard_set_mode = _lib.get("lv_keyboard_set_mode", "cdecl")
    lv_keyboard_set_mode.argtypes = [POINTER(lv_obj_t), lv_keyboard_mode_t]
    lv_keyboard_set_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 100
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_set_cursor_manage", "cdecl"):
        continue
    lv_keyboard_set_cursor_manage = _lib.get("lv_keyboard_set_cursor_manage", "cdecl")
    lv_keyboard_set_cursor_manage.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_keyboard_set_cursor_manage.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_set_map", "cdecl"):
        continue
    lv_keyboard_set_map = _lib.get("lv_keyboard_set_map", "cdecl")
    lv_keyboard_set_map.argtypes = [POINTER(lv_obj_t), lv_keyboard_mode_t, POINTER(POINTER(c_char))]
    lv_keyboard_set_map.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_set_ctrl_map", "cdecl"):
        continue
    lv_keyboard_set_ctrl_map = _lib.get("lv_keyboard_set_ctrl_map", "cdecl")
    lv_keyboard_set_ctrl_map.argtypes = [POINTER(lv_obj_t), lv_keyboard_mode_t, POINTER(lv_btnmatrix_ctrl_t)]
    lv_keyboard_set_ctrl_map.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 131
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_get_textarea", "cdecl"):
        continue
    lv_keyboard_get_textarea = _lib.get("lv_keyboard_get_textarea", "cdecl")
    lv_keyboard_get_textarea.argtypes = [POINTER(lv_obj_t)]
    lv_keyboard_get_textarea.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 138
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_get_mode", "cdecl"):
        continue
    lv_keyboard_get_mode = _lib.get("lv_keyboard_get_mode", "cdecl")
    lv_keyboard_get_mode.argtypes = [POINTER(lv_obj_t)]
    lv_keyboard_get_mode.restype = lv_keyboard_mode_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 145
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_get_cursor_manage", "cdecl"):
        continue
    lv_keyboard_get_cursor_manage = _lib.get("lv_keyboard_get_cursor_manage", "cdecl")
    lv_keyboard_get_cursor_manage.argtypes = [POINTER(lv_obj_t)]
    lv_keyboard_get_cursor_manage.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 168
for _lib in _libs.values():
    if not _lib.has("lv_keyboard_def_event_cb", "cdecl"):
        continue
    lv_keyboard_def_event_cb = _lib.get("lv_keyboard_def_event_cb", "cdecl")
    lv_keyboard_def_event_cb.argtypes = [POINTER(lv_obj_t), lv_event_t]
    lv_keyboard_def_event_cb.restype = None
    break

enum_anon_163 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 41

LV_DROPDOWN_DIR_DOWN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 41

LV_DROPDOWN_DIR_UP = (LV_DROPDOWN_DIR_DOWN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 41

LV_DROPDOWN_DIR_LEFT = (LV_DROPDOWN_DIR_UP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 41

LV_DROPDOWN_DIR_RIGHT = (LV_DROPDOWN_DIR_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 41

lv_dropdown_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 48

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 68
class struct_anon_164(Structure):
    pass

struct_anon_164.__slots__ = [
    'page',
    'text',
    'symbol',
    'options',
    'style_selected',
    'style_page',
    'style_scrlbar',
    'max_height',
    'option_cnt',
    'sel_opt_id',
    'sel_opt_id_orig',
    'pr_opt_id',
    'dir',
    'show_selected',
    'static_txt',
]
struct_anon_164._fields_ = [
    ('page', POINTER(lv_obj_t)),
    ('text', String),
    ('symbol', String),
    ('options', String),
    ('style_selected', lv_style_list_t),
    ('style_page', lv_style_list_t),
    ('style_scrlbar', lv_style_list_t),
    ('max_height', lv_coord_t),
    ('option_cnt', c_uint16),
    ('sel_opt_id', c_uint16),
    ('sel_opt_id_orig', c_uint16),
    ('pr_opt_id', c_uint16),
    ('dir', lv_dropdown_dir_t, 2),
    ('show_selected', c_uint8, 1),
    ('static_txt', c_uint8, 1),
]

lv_dropdown_ext_t = struct_anon_164# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 68

enum_anon_165 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 70

LV_DROPDOWN_PART_MAIN = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 70

LV_DROPDOWN_PART_LIST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 70

LV_DROPDOWN_PART_SCROLLBAR = (LV_DROPDOWN_PART_LIST + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 70

LV_DROPDOWN_PART_SELECTED = (LV_DROPDOWN_PART_SCROLLBAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 70

lv_dropdown_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 76

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_create", "cdecl"):
        continue
    lv_dropdown_create = _lib.get("lv_dropdown_create", "cdecl")
    lv_dropdown_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_dropdown_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 99
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_text", "cdecl"):
        continue
    lv_dropdown_set_text = _lib.get("lv_dropdown_set_text", "cdecl")
    lv_dropdown_set_text.argtypes = [POINTER(lv_obj_t), String]
    lv_dropdown_set_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 105
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_clear_options", "cdecl"):
        continue
    lv_dropdown_clear_options = _lib.get("lv_dropdown_clear_options", "cdecl")
    lv_dropdown_clear_options.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_clear_options.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_options", "cdecl"):
        continue
    lv_dropdown_set_options = _lib.get("lv_dropdown_set_options", "cdecl")
    lv_dropdown_set_options.argtypes = [POINTER(lv_obj_t), String]
    lv_dropdown_set_options.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_options_static", "cdecl"):
        continue
    lv_dropdown_set_options_static = _lib.get("lv_dropdown_set_options_static", "cdecl")
    lv_dropdown_set_options_static.argtypes = [POINTER(lv_obj_t), String]
    lv_dropdown_set_options_static.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 128
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_add_option", "cdecl"):
        continue
    lv_dropdown_add_option = _lib.get("lv_dropdown_add_option", "cdecl")
    lv_dropdown_add_option.argtypes = [POINTER(lv_obj_t), String, c_uint32]
    lv_dropdown_add_option.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 135
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_selected", "cdecl"):
        continue
    lv_dropdown_set_selected = _lib.get("lv_dropdown_set_selected", "cdecl")
    lv_dropdown_set_selected.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_dropdown_set_selected.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 142
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_dir", "cdecl"):
        continue
    lv_dropdown_set_dir = _lib.get("lv_dropdown_set_dir", "cdecl")
    lv_dropdown_set_dir.argtypes = [POINTER(lv_obj_t), lv_dropdown_dir_t]
    lv_dropdown_set_dir.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 149
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_max_height", "cdecl"):
        continue
    lv_dropdown_set_max_height = _lib.get("lv_dropdown_set_max_height", "cdecl")
    lv_dropdown_set_max_height.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_dropdown_set_max_height.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 156
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_symbol", "cdecl"):
        continue
    lv_dropdown_set_symbol = _lib.get("lv_dropdown_set_symbol", "cdecl")
    lv_dropdown_set_symbol.argtypes = [POINTER(lv_obj_t), String]
    lv_dropdown_set_symbol.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 163
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_set_show_selected", "cdecl"):
        continue
    lv_dropdown_set_show_selected = _lib.get("lv_dropdown_set_show_selected", "cdecl")
    lv_dropdown_set_show_selected.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_dropdown_set_show_selected.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 174
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_text", "cdecl"):
        continue
    lv_dropdown_get_text = _lib.get("lv_dropdown_get_text", "cdecl")
    lv_dropdown_get_text.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 181
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_options", "cdecl"):
        continue
    lv_dropdown_get_options = _lib.get("lv_dropdown_get_options", "cdecl")
    lv_dropdown_get_options.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_options.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 188
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_selected", "cdecl"):
        continue
    lv_dropdown_get_selected = _lib.get("lv_dropdown_get_selected", "cdecl")
    lv_dropdown_get_selected.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_selected.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 195
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_option_cnt", "cdecl"):
        continue
    lv_dropdown_get_option_cnt = _lib.get("lv_dropdown_get_option_cnt", "cdecl")
    lv_dropdown_get_option_cnt.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_option_cnt.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 203
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_selected_str", "cdecl"):
        continue
    lv_dropdown_get_selected_str = _lib.get("lv_dropdown_get_selected_str", "cdecl")
    lv_dropdown_get_selected_str.argtypes = [POINTER(lv_obj_t), String, c_uint32]
    lv_dropdown_get_selected_str.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 210
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_max_height", "cdecl"):
        continue
    lv_dropdown_get_max_height = _lib.get("lv_dropdown_get_max_height", "cdecl")
    lv_dropdown_get_max_height.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_max_height.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 217
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_symbol", "cdecl"):
        continue
    lv_dropdown_get_symbol = _lib.get("lv_dropdown_get_symbol", "cdecl")
    lv_dropdown_get_symbol.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_symbol.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 224
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_dir", "cdecl"):
        continue
    lv_dropdown_get_dir = _lib.get("lv_dropdown_get_dir", "cdecl")
    lv_dropdown_get_dir.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_dir.restype = lv_dropdown_dir_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 231
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_get_show_selected", "cdecl"):
        continue
    lv_dropdown_get_show_selected = _lib.get("lv_dropdown_get_show_selected", "cdecl")
    lv_dropdown_get_show_selected.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_get_show_selected.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 241
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_open", "cdecl"):
        continue
    lv_dropdown_open = _lib.get("lv_dropdown_open", "cdecl")
    lv_dropdown_open.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_open.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 248
for _lib in _libs.values():
    if not _lib.has("lv_dropdown_close", "cdecl"):
        continue
    lv_dropdown_close = _lib.get("lv_dropdown_close", "cdecl")
    lv_dropdown_close.argtypes = [POINTER(lv_obj_t)]
    lv_dropdown_close.restype = None
    break

enum_anon_166 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 38

LV_ROLLER_MODE_NORMAL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 38

LV_ROLLER_MODE_INFINITE = (LV_ROLLER_MODE_NORMAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 38

lv_roller_mode_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 43

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 56
class struct_anon_167(Structure):
    pass

struct_anon_167.__slots__ = [
    'page',
    'style_sel',
    'option_cnt',
    'sel_opt_id',
    'sel_opt_id_ori',
    'mode',
    'auto_fit',
]
struct_anon_167._fields_ = [
    ('page', lv_page_ext_t),
    ('style_sel', lv_style_list_t),
    ('option_cnt', c_uint16),
    ('sel_opt_id', c_uint16),
    ('sel_opt_id_ori', c_uint16),
    ('mode', lv_roller_mode_t, 1),
    ('auto_fit', c_uint8, 1),
]

lv_roller_ext_t = struct_anon_167# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 56

enum_anon_168 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 58

LV_ROLLER_PART_BG = LV_PAGE_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 58

LV_ROLLER_PART_SELECTED = _LV_PAGE_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 58

_LV_ROLLER_PART_VIRTUAL_LAST = (LV_ROLLER_PART_SELECTED + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 58

lv_roller_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 63

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_roller_create", "cdecl"):
        continue
    lv_roller_create = _lib.get("lv_roller_create", "cdecl")
    lv_roller_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_roller_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 87
for _lib in _libs.values():
    if not _lib.has("lv_roller_set_options", "cdecl"):
        continue
    lv_roller_set_options = _lib.get("lv_roller_set_options", "cdecl")
    lv_roller_set_options.argtypes = [POINTER(lv_obj_t), String, lv_roller_mode_t]
    lv_roller_set_options.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 94
for _lib in _libs.values():
    if not _lib.has("lv_roller_set_align", "cdecl"):
        continue
    lv_roller_set_align = _lib.get("lv_roller_set_align", "cdecl")
    lv_roller_set_align.argtypes = [POINTER(lv_obj_t), lv_label_align_t]
    lv_roller_set_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_roller_set_selected", "cdecl"):
        continue
    lv_roller_set_selected = _lib.get("lv_roller_set_selected", "cdecl")
    lv_roller_set_selected.argtypes = [POINTER(lv_obj_t), c_uint16, lv_anim_enable_t]
    lv_roller_set_selected.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_roller_set_visible_row_count", "cdecl"):
        continue
    lv_roller_set_visible_row_count = _lib.get("lv_roller_set_visible_row_count", "cdecl")
    lv_roller_set_visible_row_count.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_roller_set_visible_row_count.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 116
for _lib in _libs.values():
    if not _lib.has("lv_roller_set_auto_fit", "cdecl"):
        continue
    lv_roller_set_auto_fit = _lib.get("lv_roller_set_auto_fit", "cdecl")
    lv_roller_set_auto_fit.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_roller_set_auto_fit.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 136
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_selected", "cdecl"):
        continue
    lv_roller_get_selected = _lib.get("lv_roller_get_selected", "cdecl")
    lv_roller_get_selected.argtypes = [POINTER(lv_obj_t)]
    lv_roller_get_selected.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 143
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_option_cnt", "cdecl"):
        continue
    lv_roller_get_option_cnt = _lib.get("lv_roller_get_option_cnt", "cdecl")
    lv_roller_get_option_cnt.argtypes = [POINTER(lv_obj_t)]
    lv_roller_get_option_cnt.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 151
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_selected_str", "cdecl"):
        continue
    lv_roller_get_selected_str = _lib.get("lv_roller_get_selected_str", "cdecl")
    lv_roller_get_selected_str.argtypes = [POINTER(lv_obj_t), String, c_uint32]
    lv_roller_get_selected_str.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 158
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_align", "cdecl"):
        continue
    lv_roller_get_align = _lib.get("lv_roller_get_align", "cdecl")
    lv_roller_get_align.argtypes = [POINTER(lv_obj_t)]
    lv_roller_get_align.restype = lv_label_align_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 165
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_auto_fit", "cdecl"):
        continue
    lv_roller_get_auto_fit = _lib.get("lv_roller_get_auto_fit", "cdecl")
    lv_roller_get_auto_fit.argtypes = [POINTER(lv_obj_t)]
    lv_roller_get_auto_fit.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_roller.h: 172
for _lib in _libs.values():
    if not _lib.has("lv_roller_get_options", "cdecl"):
        continue
    lv_roller_get_options = _lib.get("lv_roller_get_options", "cdecl")
    lv_roller_get_options.argtypes = [POINTER(lv_obj_t)]
    lv_roller_get_options.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 55
class struct_anon_169(Structure):
    pass

struct_anon_169.__slots__ = [
    'style',
    'valid_x',
    'pos',
    'blink_time',
    'area',
    'txt_byte_pos',
    'state',
    'hidden',
    'click_pos',
]
struct_anon_169._fields_ = [
    ('style', lv_style_list_t),
    ('valid_x', lv_coord_t),
    ('pos', c_uint32),
    ('blink_time', c_uint16),
    ('area', lv_area_t),
    ('txt_byte_pos', c_uint32),
    ('state', c_uint8, 1),
    ('hidden', c_uint8, 1),
    ('click_pos', c_uint8, 1),
]

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 76
class struct_anon_170(Structure):
    pass

struct_anon_170.__slots__ = [
    'page',
    'label',
    'placeholder_txt',
    'style_placeholder',
    'pwd_tmp',
    'accepted_chars',
    'max_length',
    'pwd_show_time',
    'cursor',
    'pwd_mode',
    'one_line',
]
struct_anon_170._fields_ = [
    ('page', lv_page_ext_t),
    ('label', POINTER(lv_obj_t)),
    ('placeholder_txt', String),
    ('style_placeholder', lv_style_list_t),
    ('pwd_tmp', String),
    ('accepted_chars', String),
    ('max_length', c_uint32),
    ('pwd_show_time', c_uint16),
    ('cursor', struct_anon_169),
    ('pwd_mode', c_uint8, 1),
    ('one_line', c_uint8, 1),
]

lv_textarea_ext_t = struct_anon_170# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 76

enum_anon_171 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

LV_TEXTAREA_PART_BG = LV_PAGE_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

LV_TEXTAREA_PART_SCROLLBAR = LV_PAGE_PART_SCROLLBAR# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

LV_TEXTAREA_PART_EDGE_FLASH = LV_PAGE_PART_EDGE_FLASH# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

LV_TEXTAREA_PART_CURSOR = _LV_PAGE_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

LV_TEXTAREA_PART_PLACEHOLDER = (LV_TEXTAREA_PART_CURSOR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

_LV_TEXTAREA_PART_VIRTUAL_LAST = (LV_TEXTAREA_PART_PLACEHOLDER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

_LV_TEXTAREA_PART_REAL_LAST = _LV_PAGE_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 79

lv_textarea_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 89

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 101
for _lib in _libs.values():
    if not _lib.has("lv_textarea_create", "cdecl"):
        continue
    lv_textarea_create = _lib.get("lv_textarea_create", "cdecl")
    lv_textarea_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_textarea_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_textarea_add_char", "cdecl"):
        continue
    lv_textarea_add_char = _lib.get("lv_textarea_add_char", "cdecl")
    lv_textarea_add_char.argtypes = [POINTER(lv_obj_t), c_uint32]
    lv_textarea_add_char.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_textarea_add_text", "cdecl"):
        continue
    lv_textarea_add_text = _lib.get("lv_textarea_add_text", "cdecl")
    lv_textarea_add_text.argtypes = [POINTER(lv_obj_t), String]
    lv_textarea_add_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 126
for _lib in _libs.values():
    if not _lib.has("lv_textarea_del_char", "cdecl"):
        continue
    lv_textarea_del_char = _lib.get("lv_textarea_del_char", "cdecl")
    lv_textarea_del_char.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_del_char.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 132
for _lib in _libs.values():
    if not _lib.has("lv_textarea_del_char_forward", "cdecl"):
        continue
    lv_textarea_del_char_forward = _lib.get("lv_textarea_del_char_forward", "cdecl")
    lv_textarea_del_char_forward.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_del_char_forward.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 143
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_text", "cdecl"):
        continue
    lv_textarea_set_text = _lib.get("lv_textarea_set_text", "cdecl")
    lv_textarea_set_text.argtypes = [POINTER(lv_obj_t), String]
    lv_textarea_set_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_placeholder_text", "cdecl"):
        continue
    lv_textarea_set_placeholder_text = _lib.get("lv_textarea_set_placeholder_text", "cdecl")
    lv_textarea_set_placeholder_text.argtypes = [POINTER(lv_obj_t), String]
    lv_textarea_set_placeholder_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 159
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_cursor_pos", "cdecl"):
        continue
    lv_textarea_set_cursor_pos = _lib.get("lv_textarea_set_cursor_pos", "cdecl")
    lv_textarea_set_cursor_pos.argtypes = [POINTER(lv_obj_t), c_int32]
    lv_textarea_set_cursor_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 166
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_cursor_hidden", "cdecl"):
        continue
    lv_textarea_set_cursor_hidden = _lib.get("lv_textarea_set_cursor_hidden", "cdecl")
    lv_textarea_set_cursor_hidden.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_textarea_set_cursor_hidden.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 173
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_cursor_click_pos", "cdecl"):
        continue
    lv_textarea_set_cursor_click_pos = _lib.get("lv_textarea_set_cursor_click_pos", "cdecl")
    lv_textarea_set_cursor_click_pos.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_textarea_set_cursor_click_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 180
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_pwd_mode", "cdecl"):
        continue
    lv_textarea_set_pwd_mode = _lib.get("lv_textarea_set_pwd_mode", "cdecl")
    lv_textarea_set_pwd_mode.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_textarea_set_pwd_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 187
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_one_line", "cdecl"):
        continue
    lv_textarea_set_one_line = _lib.get("lv_textarea_set_one_line", "cdecl")
    lv_textarea_set_one_line.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_textarea_set_one_line.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 196
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_text_align", "cdecl"):
        continue
    lv_textarea_set_text_align = _lib.get("lv_textarea_set_text_align", "cdecl")
    lv_textarea_set_text_align.argtypes = [POINTER(lv_obj_t), lv_label_align_t]
    lv_textarea_set_text_align.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 203
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_accepted_chars", "cdecl"):
        continue
    lv_textarea_set_accepted_chars = _lib.get("lv_textarea_set_accepted_chars", "cdecl")
    lv_textarea_set_accepted_chars.argtypes = [POINTER(lv_obj_t), String]
    lv_textarea_set_accepted_chars.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 210
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_max_length", "cdecl"):
        continue
    lv_textarea_set_max_length = _lib.get("lv_textarea_set_max_length", "cdecl")
    lv_textarea_set_max_length.argtypes = [POINTER(lv_obj_t), c_uint32]
    lv_textarea_set_max_length.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 220
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_insert_replace", "cdecl"):
        continue
    lv_textarea_set_insert_replace = _lib.get("lv_textarea_set_insert_replace", "cdecl")
    lv_textarea_set_insert_replace.argtypes = [POINTER(lv_obj_t), String]
    lv_textarea_set_insert_replace.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 258
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_text_sel", "cdecl"):
        continue
    lv_textarea_set_text_sel = _lib.get("lv_textarea_set_text_sel", "cdecl")
    lv_textarea_set_text_sel.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_textarea_set_text_sel.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 265
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_pwd_show_time", "cdecl"):
        continue
    lv_textarea_set_pwd_show_time = _lib.get("lv_textarea_set_pwd_show_time", "cdecl")
    lv_textarea_set_pwd_show_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_textarea_set_pwd_show_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 272
for _lib in _libs.values():
    if not _lib.has("lv_textarea_set_cursor_blink_time", "cdecl"):
        continue
    lv_textarea_set_cursor_blink_time = _lib.get("lv_textarea_set_cursor_blink_time", "cdecl")
    lv_textarea_set_cursor_blink_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_textarea_set_cursor_blink_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 283
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_text", "cdecl"):
        continue
    lv_textarea_get_text = _lib.get("lv_textarea_get_text", "cdecl")
    lv_textarea_get_text.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 290
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_placeholder_text", "cdecl"):
        continue
    lv_textarea_get_placeholder_text = _lib.get("lv_textarea_get_placeholder_text", "cdecl")
    lv_textarea_get_placeholder_text.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_placeholder_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 297
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_label", "cdecl"):
        continue
    lv_textarea_get_label = _lib.get("lv_textarea_get_label", "cdecl")
    lv_textarea_get_label.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_label.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 304
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_cursor_pos", "cdecl"):
        continue
    lv_textarea_get_cursor_pos = _lib.get("lv_textarea_get_cursor_pos", "cdecl")
    lv_textarea_get_cursor_pos.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_cursor_pos.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 311
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_cursor_hidden", "cdecl"):
        continue
    lv_textarea_get_cursor_hidden = _lib.get("lv_textarea_get_cursor_hidden", "cdecl")
    lv_textarea_get_cursor_hidden.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_cursor_hidden.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 318
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_cursor_click_pos", "cdecl"):
        continue
    lv_textarea_get_cursor_click_pos = _lib.get("lv_textarea_get_cursor_click_pos", "cdecl")
    lv_textarea_get_cursor_click_pos.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_cursor_click_pos.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 325
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_pwd_mode", "cdecl"):
        continue
    lv_textarea_get_pwd_mode = _lib.get("lv_textarea_get_pwd_mode", "cdecl")
    lv_textarea_get_pwd_mode.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_pwd_mode.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 332
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_one_line", "cdecl"):
        continue
    lv_textarea_get_one_line = _lib.get("lv_textarea_get_one_line", "cdecl")
    lv_textarea_get_one_line.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_one_line.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 339
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_accepted_chars", "cdecl"):
        continue
    lv_textarea_get_accepted_chars = _lib.get("lv_textarea_get_accepted_chars", "cdecl")
    lv_textarea_get_accepted_chars.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_accepted_chars.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 346
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_max_length", "cdecl"):
        continue
    lv_textarea_get_max_length = _lib.get("lv_textarea_get_max_length", "cdecl")
    lv_textarea_get_max_length.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_max_length.restype = c_uint32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 383
for _lib in _libs.values():
    if not _lib.has("lv_textarea_text_is_selected", "cdecl"):
        continue
    lv_textarea_text_is_selected = _lib.get("lv_textarea_text_is_selected", "cdecl")
    lv_textarea_text_is_selected.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_text_is_selected.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 390
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_text_sel_en", "cdecl"):
        continue
    lv_textarea_get_text_sel_en = _lib.get("lv_textarea_get_text_sel_en", "cdecl")
    lv_textarea_get_text_sel_en.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_text_sel_en.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 397
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_pwd_show_time", "cdecl"):
        continue
    lv_textarea_get_pwd_show_time = _lib.get("lv_textarea_get_pwd_show_time", "cdecl")
    lv_textarea_get_pwd_show_time.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_pwd_show_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 404
for _lib in _libs.values():
    if not _lib.has("lv_textarea_get_cursor_blink_time", "cdecl"):
        continue
    lv_textarea_get_cursor_blink_time = _lib.get("lv_textarea_get_cursor_blink_time", "cdecl")
    lv_textarea_get_cursor_blink_time.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_get_cursor_blink_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 414
for _lib in _libs.values():
    if not _lib.has("lv_textarea_clear_selection", "cdecl"):
        continue
    lv_textarea_clear_selection = _lib.get("lv_textarea_clear_selection", "cdecl")
    lv_textarea_clear_selection.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_clear_selection.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 420
for _lib in _libs.values():
    if not _lib.has("lv_textarea_cursor_right", "cdecl"):
        continue
    lv_textarea_cursor_right = _lib.get("lv_textarea_cursor_right", "cdecl")
    lv_textarea_cursor_right.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_cursor_right.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 426
for _lib in _libs.values():
    if not _lib.has("lv_textarea_cursor_left", "cdecl"):
        continue
    lv_textarea_cursor_left = _lib.get("lv_textarea_cursor_left", "cdecl")
    lv_textarea_cursor_left.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_cursor_left.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 432
for _lib in _libs.values():
    if not _lib.has("lv_textarea_cursor_down", "cdecl"):
        continue
    lv_textarea_cursor_down = _lib.get("lv_textarea_cursor_down", "cdecl")
    lv_textarea_cursor_down.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_cursor_down.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 438
for _lib in _libs.values():
    if not _lib.has("lv_textarea_cursor_up", "cdecl"):
        continue
    lv_textarea_cursor_up = _lib.get("lv_textarea_cursor_up", "cdecl")
    lv_textarea_cursor_up.argtypes = [POINTER(lv_obj_t)]
    lv_textarea_cursor_up.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 36
class struct_anon_172(Structure):
    pass

struct_anon_172.__slots__ = [
    'img',
    'dsc',
]
struct_anon_172._fields_ = [
    ('img', lv_img_ext_t),
    ('dsc', lv_img_dsc_t),
]

lv_canvas_ext_t = struct_anon_172# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 36

enum_anon_173 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 39

LV_CANVAS_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 39

lv_canvas_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 42

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 54
for _lib in _libs.values():
    if not _lib.has("lv_canvas_create", "cdecl"):
        continue
    lv_canvas_create = _lib.get("lv_canvas_create", "cdecl")
    lv_canvas_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_canvas_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 72
for _lib in _libs.values():
    if not _lib.has("lv_canvas_set_buffer", "cdecl"):
        continue
    lv_canvas_set_buffer = _lib.get("lv_canvas_set_buffer", "cdecl")
    lv_canvas_set_buffer.argtypes = [POINTER(lv_obj_t), POINTER(None), lv_coord_t, lv_coord_t, lv_img_cf_t]
    lv_canvas_set_buffer.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 81
for _lib in _libs.values():
    if not _lib.has("lv_canvas_set_px", "cdecl"):
        continue
    lv_canvas_set_px = _lib.get("lv_canvas_set_px", "cdecl")
    lv_canvas_set_px.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_color_t]
    lv_canvas_set_px.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 93
for _lib in _libs.values():
    if not _lib.has("lv_canvas_set_palette", "cdecl"):
        continue
    lv_canvas_set_palette = _lib.get("lv_canvas_set_palette", "cdecl")
    lv_canvas_set_palette.argtypes = [POINTER(lv_obj_t), c_uint8, lv_color_t]
    lv_canvas_set_palette.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 106
for _lib in _libs.values():
    if not _lib.has("lv_canvas_get_px", "cdecl"):
        continue
    lv_canvas_get_px = _lib.get("lv_canvas_get_px", "cdecl")
    lv_canvas_get_px.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t]
    lv_canvas_get_px.restype = lv_color_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_canvas_get_img", "cdecl"):
        continue
    lv_canvas_get_img = _lib.get("lv_canvas_get_img", "cdecl")
    lv_canvas_get_img.argtypes = [POINTER(lv_obj_t)]
    lv_canvas_get_img.restype = POINTER(lv_img_dsc_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_canvas_copy_buf", "cdecl"):
        continue
    lv_canvas_copy_buf = _lib.get("lv_canvas_copy_buf", "cdecl")
    lv_canvas_copy_buf.argtypes = [POINTER(lv_obj_t), POINTER(None), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t]
    lv_canvas_copy_buf.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 147
for _lib in _libs.values():
    if not _lib.has("lv_canvas_transform", "cdecl"):
        continue
    lv_canvas_transform = _lib.get("lv_canvas_transform", "cdecl")
    lv_canvas_transform.argtypes = [POINTER(lv_obj_t), POINTER(lv_img_dsc_t), c_int16, c_uint16, lv_coord_t, lv_coord_t, c_int32, c_int32, c_bool]
    lv_canvas_transform.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 157
for _lib in _libs.values():
    if not _lib.has("lv_canvas_blur_hor", "cdecl"):
        continue
    lv_canvas_blur_hor = _lib.get("lv_canvas_blur_hor", "cdecl")
    lv_canvas_blur_hor.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t), c_uint16]
    lv_canvas_blur_hor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 165
for _lib in _libs.values():
    if not _lib.has("lv_canvas_blur_ver", "cdecl"):
        continue
    lv_canvas_blur_ver = _lib.get("lv_canvas_blur_ver", "cdecl")
    lv_canvas_blur_ver.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t), c_uint16]
    lv_canvas_blur_ver.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 173
for _lib in _libs.values():
    if not _lib.has("lv_canvas_fill_bg", "cdecl"):
        continue
    lv_canvas_fill_bg = _lib.get("lv_canvas_fill_bg", "cdecl")
    lv_canvas_fill_bg.argtypes = [POINTER(lv_obj_t), lv_color_t, lv_opa_t]
    lv_canvas_fill_bg.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 184
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_rect", "cdecl"):
        continue
    lv_canvas_draw_rect = _lib.get("lv_canvas_draw_rect", "cdecl")
    lv_canvas_draw_rect.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_coord_t, lv_coord_t, POINTER(lv_draw_rect_dsc_t)]
    lv_canvas_draw_rect.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 197
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_text", "cdecl"):
        continue
    lv_canvas_draw_text = _lib.get("lv_canvas_draw_text", "cdecl")
    lv_canvas_draw_text.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_coord_t, POINTER(lv_draw_label_dsc_t), String, lv_label_align_t]
    lv_canvas_draw_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 209
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_img", "cdecl"):
        continue
    lv_canvas_draw_img = _lib.get("lv_canvas_draw_img", "cdecl")
    lv_canvas_draw_img.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, POINTER(None), POINTER(lv_draw_img_dsc_t)]
    lv_canvas_draw_img.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 219
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_line", "cdecl"):
        continue
    lv_canvas_draw_line = _lib.get("lv_canvas_draw_line", "cdecl")
    lv_canvas_draw_line.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t), c_uint32, POINTER(lv_draw_line_dsc_t)]
    lv_canvas_draw_line.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_polygon", "cdecl"):
        continue
    lv_canvas_draw_polygon = _lib.get("lv_canvas_draw_polygon", "cdecl")
    lv_canvas_draw_polygon.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t), c_uint32, POINTER(lv_draw_rect_dsc_t)]
    lv_canvas_draw_polygon.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 242
for _lib in _libs.values():
    if not _lib.has("lv_canvas_draw_arc", "cdecl"):
        continue
    lv_canvas_draw_arc = _lib.get("lv_canvas_draw_arc", "cdecl")
    lv_canvas_draw_arc.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_coord_t, c_int32, c_int32, POINTER(lv_draw_line_dsc_t)]
    lv_canvas_draw_arc.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 61
class struct_anon_174(Structure):
    pass

struct_anon_174.__slots__ = [
    'page',
    'header',
    'title_txt',
    'btn_w',
    'title_txt_align',
]
struct_anon_174._fields_ = [
    ('page', POINTER(lv_obj_t)),
    ('header', POINTER(lv_obj_t)),
    ('title_txt', String),
    ('btn_w', lv_coord_t),
    ('title_txt_align', c_uint8),
]

lv_win_ext_t = struct_anon_174# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 61

enum_anon_175 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

LV_WIN_PART_BG = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

_LV_WIN_PART_VIRTUAL_LAST = (LV_WIN_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

LV_WIN_PART_HEADER = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

LV_WIN_PART_CONTENT_SCROLLABLE = (LV_WIN_PART_HEADER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

LV_WIN_PART_SCROLLBAR = (LV_WIN_PART_CONTENT_SCROLLABLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

_LV_WIN_PART_REAL_LAST = (LV_WIN_PART_SCROLLBAR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 64

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 83
for _lib in _libs.values():
    if not _lib.has("lv_win_create", "cdecl"):
        continue
    lv_win_create = _lib.get("lv_win_create", "cdecl")
    lv_win_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_win_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_win_clean", "cdecl"):
        continue
    lv_win_clean = _lib.get("lv_win_clean", "cdecl")
    lv_win_clean.argtypes = [POINTER(lv_obj_t)]
    lv_win_clean.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 101
for _lib in _libs.values():
    if not _lib.has("lv_win_add_btn_right", "cdecl"):
        continue
    lv_win_add_btn_right = _lib.get("lv_win_add_btn_right", "cdecl")
    lv_win_add_btn_right.argtypes = [POINTER(lv_obj_t), POINTER(None)]
    lv_win_add_btn_right.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_win_add_btn_left", "cdecl"):
        continue
    lv_win_add_btn_left = _lib.get("lv_win_add_btn_left", "cdecl")
    lv_win_add_btn_left.argtypes = [POINTER(lv_obj_t), POINTER(None)]
    lv_win_add_btn_left.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_win_close_event_cb", "cdecl"):
        continue
    lv_win_close_event_cb = _lib.get("lv_win_close_event_cb", "cdecl")
    lv_win_close_event_cb.argtypes = [POINTER(lv_obj_t), lv_event_t]
    lv_win_close_event_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_win_set_title", "cdecl"):
        continue
    lv_win_set_title = _lib.get("lv_win_set_title", "cdecl")
    lv_win_set_title.argtypes = [POINTER(lv_obj_t), String]
    lv_win_set_title.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_win_set_header_height", "cdecl"):
        continue
    lv_win_set_header_height = _lib.get("lv_win_set_header_height", "cdecl")
    lv_win_set_header_height.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_win_set_header_height.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 141
for _lib in _libs.values():
    if not _lib.has("lv_win_set_btn_width", "cdecl"):
        continue
    lv_win_set_btn_width = _lib.get("lv_win_set_btn_width", "cdecl")
    lv_win_set_btn_width.argtypes = [POINTER(lv_obj_t), lv_coord_t]
    lv_win_set_btn_width.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 149
for _lib in _libs.values():
    if not _lib.has("lv_win_set_content_size", "cdecl"):
        continue
    lv_win_set_content_size = _lib.get("lv_win_set_content_size", "cdecl")
    lv_win_set_content_size.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t]
    lv_win_set_content_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 156
for _lib in _libs.values():
    if not _lib.has("lv_win_set_layout", "cdecl"):
        continue
    lv_win_set_layout = _lib.get("lv_win_set_layout", "cdecl")
    lv_win_set_layout.argtypes = [POINTER(lv_obj_t), lv_layout_t]
    lv_win_set_layout.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 163
for _lib in _libs.values():
    if not _lib.has("lv_win_set_scrollbar_mode", "cdecl"):
        continue
    lv_win_set_scrollbar_mode = _lib.get("lv_win_set_scrollbar_mode", "cdecl")
    lv_win_set_scrollbar_mode.argtypes = [POINTER(lv_obj_t), lv_scrollbar_mode_t]
    lv_win_set_scrollbar_mode.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 170
for _lib in _libs.values():
    if not _lib.has("lv_win_set_anim_time", "cdecl"):
        continue
    lv_win_set_anim_time = _lib.get("lv_win_set_anim_time", "cdecl")
    lv_win_set_anim_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_win_set_anim_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 177
for _lib in _libs.values():
    if not _lib.has("lv_win_set_drag", "cdecl"):
        continue
    lv_win_set_drag = _lib.get("lv_win_set_drag", "cdecl")
    lv_win_set_drag.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_win_set_drag.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 184
for _lib in _libs.values():
    if not _lib.has("lv_win_title_set_alignment", "cdecl"):
        continue
    lv_win_title_set_alignment = _lib.get("lv_win_title_set_alignment", "cdecl")
    lv_win_title_set_alignment.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_win_title_set_alignment.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 195
for _lib in _libs.values():
    if not _lib.has("lv_win_get_title", "cdecl"):
        continue
    lv_win_get_title = _lib.get("lv_win_get_title", "cdecl")
    lv_win_get_title.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_title.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 202
for _lib in _libs.values():
    if not _lib.has("lv_win_get_content", "cdecl"):
        continue
    lv_win_get_content = _lib.get("lv_win_get_content", "cdecl")
    lv_win_get_content.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_content.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 209
for _lib in _libs.values():
    if not _lib.has("lv_win_get_header_height", "cdecl"):
        continue
    lv_win_get_header_height = _lib.get("lv_win_get_header_height", "cdecl")
    lv_win_get_header_height.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_header_height.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 216
for _lib in _libs.values():
    if not _lib.has("lv_win_get_btn_width", "cdecl"):
        continue
    lv_win_get_btn_width = _lib.get("lv_win_get_btn_width", "cdecl")
    lv_win_get_btn_width.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_btn_width.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 224
for _lib in _libs.values():
    if not _lib.has("lv_win_get_from_btn", "cdecl"):
        continue
    lv_win_get_from_btn = _lib.get("lv_win_get_from_btn", "cdecl")
    lv_win_get_from_btn.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_from_btn.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 231
for _lib in _libs.values():
    if not _lib.has("lv_win_get_layout", "cdecl"):
        continue
    lv_win_get_layout = _lib.get("lv_win_get_layout", "cdecl")
    lv_win_get_layout.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_layout.restype = lv_layout_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 238
for _lib in _libs.values():
    if not _lib.has("lv_win_get_sb_mode", "cdecl"):
        continue
    lv_win_get_sb_mode = _lib.get("lv_win_get_sb_mode", "cdecl")
    lv_win_get_sb_mode.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_sb_mode.restype = lv_scrollbar_mode_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 245
for _lib in _libs.values():
    if not _lib.has("lv_win_get_anim_time", "cdecl"):
        continue
    lv_win_get_anim_time = _lib.get("lv_win_get_anim_time", "cdecl")
    lv_win_get_anim_time.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_anim_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 252
for _lib in _libs.values():
    if not _lib.has("lv_win_get_width", "cdecl"):
        continue
    lv_win_get_width = _lib.get("lv_win_get_width", "cdecl")
    lv_win_get_width.argtypes = [POINTER(lv_obj_t)]
    lv_win_get_width.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 268
for _lib in _libs.values():
    if not _lib.has("lv_win_title_get_alignment", "cdecl"):
        continue
    lv_win_title_get_alignment = _lib.get("lv_win_title_get_alignment", "cdecl")
    lv_win_title_get_alignment.argtypes = [POINTER(lv_obj_t)]
    lv_win_title_get_alignment.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 280
for _lib in _libs.values():
    if not _lib.has("lv_win_focus", "cdecl"):
        continue
    lv_win_focus = _lib.get("lv_win_focus", "cdecl")
    lv_win_focus.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t), lv_anim_enable_t]
    lv_win_focus.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 289
for _lib in _libs.values():
    try:
        ext = (POINTER(lv_win_ext_t)).in_dll(_lib, "ext")
        break
    except:
        pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_win.h: 299
for _lib in _libs.values():
    try:
        ext = (POINTER(lv_win_ext_t)).in_dll(_lib, "ext")
        break
    except:
        pass

enum_anon_176 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

LV_TABVIEW_TAB_POS_NONE = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

LV_TABVIEW_TAB_POS_TOP = (LV_TABVIEW_TAB_POS_NONE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

LV_TABVIEW_TAB_POS_BOTTOM = (LV_TABVIEW_TAB_POS_TOP + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

LV_TABVIEW_TAB_POS_LEFT = (LV_TABVIEW_TAB_POS_BOTTOM + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

LV_TABVIEW_TAB_POS_RIGHT = (LV_TABVIEW_TAB_POS_LEFT + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 42

lv_tabview_btns_pos_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 49

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 66
class struct_anon_177(Structure):
    pass

struct_anon_177.__slots__ = [
    'btns',
    'indic',
    'content',
    'tab_name_ptr',
    'point_last',
    'tab_cur',
    'tab_cnt',
    'anim_time',
    'btns_pos',
]
struct_anon_177._fields_ = [
    ('btns', POINTER(lv_obj_t)),
    ('indic', POINTER(lv_obj_t)),
    ('content', POINTER(lv_obj_t)),
    ('tab_name_ptr', POINTER(POINTER(c_char))),
    ('point_last', lv_point_t),
    ('tab_cur', c_uint16),
    ('tab_cnt', c_uint16),
    ('anim_time', c_uint16),
    ('btns_pos', lv_tabview_btns_pos_t, 3),
]

lv_tabview_ext_t = struct_anon_177# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 66

enum_anon_178 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

LV_TABVIEW_PART_BG = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

_LV_TABVIEW_PART_VIRTUAL_LAST = _LV_OBJ_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

LV_TABVIEW_PART_BG_SCROLLABLE = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

LV_TABVIEW_PART_TAB_BG = (LV_TABVIEW_PART_BG_SCROLLABLE + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

LV_TABVIEW_PART_TAB_BTN = (LV_TABVIEW_PART_TAB_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

LV_TABVIEW_PART_INDIC = (LV_TABVIEW_PART_TAB_BTN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

_LV_TABVIEW_PART_REAL_LAST = (LV_TABVIEW_PART_INDIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 68

lv_tabview_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 78

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 90
for _lib in _libs.values():
    if not _lib.has("lv_tabview_create", "cdecl"):
        continue
    lv_tabview_create = _lib.get("lv_tabview_create", "cdecl")
    lv_tabview_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_tabview_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_tabview_add_tab", "cdecl"):
        continue
    lv_tabview_add_tab = _lib.get("lv_tabview_add_tab", "cdecl")
    lv_tabview_add_tab.argtypes = [POINTER(lv_obj_t), String]
    lv_tabview_add_tab.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 108
for _lib in _libs.values():
    if not _lib.has("lv_tabview_clean_tab", "cdecl"):
        continue
    lv_tabview_clean_tab = _lib.get("lv_tabview_clean_tab", "cdecl")
    lv_tabview_clean_tab.argtypes = [POINTER(lv_obj_t)]
    lv_tabview_clean_tab.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_tabview_set_tab_act", "cdecl"):
        continue
    lv_tabview_set_tab_act = _lib.get("lv_tabview_set_tab_act", "cdecl")
    lv_tabview_set_tab_act.argtypes = [POINTER(lv_obj_t), c_uint16, lv_anim_enable_t]
    lv_tabview_set_tab_act.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 128
for _lib in _libs.values():
    if not _lib.has("lv_tabview_set_tab_name", "cdecl"):
        continue
    lv_tabview_set_tab_name = _lib.get("lv_tabview_set_tab_name", "cdecl")
    lv_tabview_set_tab_name.argtypes = [POINTER(lv_obj_t), c_uint16, String]
    lv_tabview_set_tab_name.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 135
for _lib in _libs.values():
    if not _lib.has("lv_tabview_set_anim_time", "cdecl"):
        continue
    lv_tabview_set_anim_time = _lib.get("lv_tabview_set_anim_time", "cdecl")
    lv_tabview_set_anim_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_tabview_set_anim_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 142
for _lib in _libs.values():
    if not _lib.has("lv_tabview_set_btns_pos", "cdecl"):
        continue
    lv_tabview_set_btns_pos = _lib.get("lv_tabview_set_btns_pos", "cdecl")
    lv_tabview_set_btns_pos.argtypes = [POINTER(lv_obj_t), lv_tabview_btns_pos_t]
    lv_tabview_set_btns_pos.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 153
for _lib in _libs.values():
    if not _lib.has("lv_tabview_get_tab_act", "cdecl"):
        continue
    lv_tabview_get_tab_act = _lib.get("lv_tabview_get_tab_act", "cdecl")
    lv_tabview_get_tab_act.argtypes = [POINTER(lv_obj_t)]
    lv_tabview_get_tab_act.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 160
for _lib in _libs.values():
    if not _lib.has("lv_tabview_get_tab_count", "cdecl"):
        continue
    lv_tabview_get_tab_count = _lib.get("lv_tabview_get_tab_count", "cdecl")
    lv_tabview_get_tab_count.argtypes = [POINTER(lv_obj_t)]
    lv_tabview_get_tab_count.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 167
for _lib in _libs.values():
    if not _lib.has("lv_tabview_get_tab", "cdecl"):
        continue
    lv_tabview_get_tab = _lib.get("lv_tabview_get_tab", "cdecl")
    lv_tabview_get_tab.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_tabview_get_tab.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 174
for _lib in _libs.values():
    if not _lib.has("lv_tabview_get_anim_time", "cdecl"):
        continue
    lv_tabview_get_anim_time = _lib.get("lv_tabview_get_anim_time", "cdecl")
    lv_tabview_get_anim_time.argtypes = [POINTER(lv_obj_t)]
    lv_tabview_get_anim_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tabview.h: 180
for _lib in _libs.values():
    if not _lib.has("lv_tabview_get_btns_pos", "cdecl"):
        continue
    lv_tabview_get_btns_pos = _lib.get("lv_tabview_get_btns_pos", "cdecl")
    lv_tabview_get_btns_pos.argtypes = [POINTER(lv_obj_t)]
    lv_tabview_get_btns_pos.restype = lv_tabview_btns_pos_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 44
class struct_anon_179(Structure):
    pass

struct_anon_179.__slots__ = [
    'page',
    'valid_pos',
    'valid_pos_cnt',
    'anim_time',
    'act_id',
    'drag_top_en',
    'drag_bottom_en',
    'drag_left_en',
    'drag_right_en',
]
struct_anon_179._fields_ = [
    ('page', lv_page_ext_t),
    ('valid_pos', POINTER(lv_point_t)),
    ('valid_pos_cnt', c_uint16),
    ('anim_time', c_uint16),
    ('act_id', lv_point_t),
    ('drag_top_en', c_uint8, 1),
    ('drag_bottom_en', c_uint8, 1),
    ('drag_left_en', c_uint8, 1),
    ('drag_right_en', c_uint8, 1),
]

lv_tileview_ext_t = struct_anon_179# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 44

enum_anon_180 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

LV_TILEVIEW_PART_BG = LV_PAGE_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

LV_TILEVIEW_PART_SCROLLBAR = LV_PAGE_PART_SCROLLBAR# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

LV_TILEVIEW_PART_EDGE_FLASH = LV_PAGE_PART_EDGE_FLASH# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

_LV_TILEVIEW_PART_VIRTUAL_LAST = _LV_PAGE_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

_LV_TILEVIEW_PART_REAL_LAST = _LV_PAGE_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 47

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 65
for _lib in _libs.values():
    if not _lib.has("lv_tileview_create", "cdecl"):
        continue
    lv_tileview_create = _lib.get("lv_tileview_create", "cdecl")
    lv_tileview_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_tileview_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 76
for _lib in _libs.values():
    if not _lib.has("lv_tileview_add_element", "cdecl"):
        continue
    lv_tileview_add_element = _lib.get("lv_tileview_add_element", "cdecl")
    lv_tileview_add_element.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_tileview_add_element.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_tileview_set_valid_positions", "cdecl"):
        continue
    lv_tileview_set_valid_positions = _lib.get("lv_tileview_set_valid_positions", "cdecl")
    lv_tileview_set_valid_positions.argtypes = [POINTER(lv_obj_t), POINTER(lv_point_t), c_uint16]
    lv_tileview_set_valid_positions.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 98
for _lib in _libs.values():
    if not _lib.has("lv_tileview_set_tile_act", "cdecl"):
        continue
    lv_tileview_set_tile_act = _lib.get("lv_tileview_set_tile_act", "cdecl")
    lv_tileview_set_tile_act.argtypes = [POINTER(lv_obj_t), lv_coord_t, lv_coord_t, lv_anim_enable_t]
    lv_tileview_set_tile_act.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_tileview.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_tileview_get_tile_act", "cdecl"):
        continue
    lv_tileview_get_tile_act = _lib.get("lv_tileview_get_tile_act", "cdecl")
    lv_tileview_get_tile_act.argtypes = [POINTER(lv_obj_t), POINTER(lv_coord_t), POINTER(lv_coord_t)]
    lv_tileview_get_tile_act.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 55
class struct_anon_181(Structure):
    pass

struct_anon_181.__slots__ = [
    'bg',
    'text',
    'btnm',
    'anim_time',
]
struct_anon_181._fields_ = [
    ('bg', lv_cont_ext_t),
    ('text', POINTER(lv_obj_t)),
    ('btnm', POINTER(lv_obj_t)),
    ('anim_time', c_uint16),
]

lv_msgbox_ext_t = struct_anon_181# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 55

enum_anon_182 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 58

LV_MSGBOX_PART_BG = LV_CONT_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 58

LV_MSGBOX_PART_BTN_BG = _LV_CONT_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 58

LV_MSGBOX_PART_BTN = (LV_MSGBOX_PART_BTN_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 58

lv_msgbox_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 64

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 77
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_create", "cdecl"):
        continue
    lv_msgbox_create = _lib.get("lv_msgbox_create", "cdecl")
    lv_msgbox_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_msgbox_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 89
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_add_btns", "cdecl"):
        continue
    lv_msgbox_add_btns = _lib.get("lv_msgbox_add_btns", "cdecl")
    lv_msgbox_add_btns.argtypes = [POINTER(lv_obj_t), POINTER(POINTER(c_char))]
    lv_msgbox_add_btns.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 100
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_set_text", "cdecl"):
        continue
    lv_msgbox_set_text = _lib.get("lv_msgbox_set_text", "cdecl")
    lv_msgbox_set_text.argtypes = [POINTER(lv_obj_t), String]
    lv_msgbox_set_text.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 107
for _lib in _libs.values():
    if _lib.has("lv_msgbox_set_text_fmt", "cdecl"):
        _func = _lib.get("lv_msgbox_set_text_fmt", "cdecl")
        _restype = None
        _errcheck = None
        _argtypes = [POINTER(lv_obj_t), String]
        lv_msgbox_set_text_fmt = _variadic_function(_func,_restype,_argtypes,_errcheck)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 114
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_set_anim_time", "cdecl"):
        continue
    lv_msgbox_set_anim_time = _lib.get("lv_msgbox_set_anim_time", "cdecl")
    lv_msgbox_set_anim_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_msgbox_set_anim_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 121
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_start_auto_close", "cdecl"):
        continue
    lv_msgbox_start_auto_close = _lib.get("lv_msgbox_start_auto_close", "cdecl")
    lv_msgbox_start_auto_close.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_msgbox_start_auto_close.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_stop_auto_close", "cdecl"):
        continue
    lv_msgbox_stop_auto_close = _lib.get("lv_msgbox_stop_auto_close", "cdecl")
    lv_msgbox_stop_auto_close.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_stop_auto_close.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_set_recolor", "cdecl"):
        continue
    lv_msgbox_set_recolor = _lib.get("lv_msgbox_set_recolor", "cdecl")
    lv_msgbox_set_recolor.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_msgbox_set_recolor.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 145
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_text", "cdecl"):
        continue
    lv_msgbox_get_text = _lib.get("lv_msgbox_get_text", "cdecl")
    lv_msgbox_get_text.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 153
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_active_btn", "cdecl"):
        continue
    lv_msgbox_get_active_btn = _lib.get("lv_msgbox_get_active_btn", "cdecl")
    lv_msgbox_get_active_btn.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_active_btn.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_active_btn_text", "cdecl"):
        continue
    lv_msgbox_get_active_btn_text = _lib.get("lv_msgbox_get_active_btn_text", "cdecl")
    lv_msgbox_get_active_btn_text.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_active_btn_text.restype = c_char_p
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 168
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_anim_time", "cdecl"):
        continue
    lv_msgbox_get_anim_time = _lib.get("lv_msgbox_get_anim_time", "cdecl")
    lv_msgbox_get_anim_time.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_anim_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 175
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_recolor", "cdecl"):
        continue
    lv_msgbox_get_recolor = _lib.get("lv_msgbox_get_recolor", "cdecl")
    lv_msgbox_get_recolor.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_recolor.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_msgbox.h: 183
for _lib in _libs.values():
    if not _lib.has("lv_msgbox_get_btnmatrix", "cdecl"):
        continue
    lv_msgbox_get_btnmatrix = _lib.get("lv_msgbox_get_btnmatrix", "cdecl")
    lv_msgbox_get_btnmatrix.argtypes = [POINTER(lv_obj_t)]
    lv_msgbox_get_btnmatrix.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 33
class struct_anon_183(Structure):
    pass

struct_anon_183.__slots__ = [
    'param',
]
struct_anon_183._fields_ = [
    ('param', POINTER(None)),
]

lv_objmask_mask_t = struct_anon_183# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 33

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 41
class struct_anon_184(Structure):
    pass

struct_anon_184.__slots__ = [
    'cont',
    'mask_ll',
]
struct_anon_184._fields_ = [
    ('cont', lv_cont_ext_t),
    ('mask_ll', lv_ll_t),
]

lv_objmask_ext_t = struct_anon_184# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 41

enum_anon_185 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 44

LV_OBJMASK_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 44

lv_objmask_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 47

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 59
for _lib in _libs.values():
    if not _lib.has("lv_objmask_create", "cdecl"):
        continue
    lv_objmask_create = _lib.get("lv_objmask_create", "cdecl")
    lv_objmask_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_objmask_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 71
for _lib in _libs.values():
    if not _lib.has("lv_objmask_add_mask", "cdecl"):
        continue
    lv_objmask_add_mask = _lib.get("lv_objmask_add_mask", "cdecl")
    lv_objmask_add_mask.argtypes = [POINTER(lv_obj_t), POINTER(None)]
    lv_objmask_add_mask.restype = POINTER(lv_objmask_mask_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 79
for _lib in _libs.values():
    if not _lib.has("lv_objmask_update_mask", "cdecl"):
        continue
    lv_objmask_update_mask = _lib.get("lv_objmask_update_mask", "cdecl")
    lv_objmask_update_mask.argtypes = [POINTER(lv_obj_t), POINTER(lv_objmask_mask_t), POINTER(None)]
    lv_objmask_update_mask.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_objmask.h: 87
for _lib in _libs.values():
    if not _lib.has("lv_objmask_remove_mask", "cdecl"):
        continue
    lv_objmask_remove_mask = _lib.get("lv_objmask_remove_mask", "cdecl")
    lv_objmask_remove_mask.argtypes = [POINTER(lv_obj_t), POINTER(lv_objmask_mask_t)]
    lv_objmask_remove_mask.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 40
class struct_anon_186(Structure):
    pass

struct_anon_186.__slots__ = [
    'scale_angle',
    'angle_ofs',
    'line_cnt',
    'cur_value',
    'min_value',
    'max_value',
    'mirrored',
]
struct_anon_186._fields_ = [
    ('scale_angle', c_uint16),
    ('angle_ofs', c_uint16),
    ('line_cnt', c_uint16),
    ('cur_value', c_int32),
    ('min_value', c_int32),
    ('max_value', c_int32),
    ('mirrored', c_uint8, 1),
]

lv_linemeter_ext_t = struct_anon_186# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 40

enum_anon_187 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 43

LV_LINEMETER_PART_MAIN = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 43

_LV_LINEMETER_PART_VIRTUAL_LAST = (LV_LINEMETER_PART_MAIN + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 43

_LV_LINEMETER_PART_REAL_LAST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 43

lv_linemeter_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 48

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 61
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_create", "cdecl"):
        continue
    lv_linemeter_create = _lib.get("lv_linemeter_create", "cdecl")
    lv_linemeter_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_linemeter_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 72
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_set_value", "cdecl"):
        continue
    lv_linemeter_set_value = _lib.get("lv_linemeter_set_value", "cdecl")
    lv_linemeter_set_value.argtypes = [POINTER(lv_obj_t), c_int32]
    lv_linemeter_set_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 80
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_set_range", "cdecl"):
        continue
    lv_linemeter_set_range = _lib.get("lv_linemeter_set_range", "cdecl")
    lv_linemeter_set_range.argtypes = [POINTER(lv_obj_t), c_int32, c_int32]
    lv_linemeter_set_range.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_set_scale", "cdecl"):
        continue
    lv_linemeter_set_scale = _lib.get("lv_linemeter_set_scale", "cdecl")
    lv_linemeter_set_scale.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_linemeter_set_scale.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_set_angle_offset", "cdecl"):
        continue
    lv_linemeter_set_angle_offset = _lib.get("lv_linemeter_set_angle_offset", "cdecl")
    lv_linemeter_set_angle_offset.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_linemeter_set_angle_offset.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_set_mirror", "cdecl"):
        continue
    lv_linemeter_set_mirror = _lib.get("lv_linemeter_set_mirror", "cdecl")
    lv_linemeter_set_mirror.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_linemeter_set_mirror.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 113
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_value", "cdecl"):
        continue
    lv_linemeter_get_value = _lib.get("lv_linemeter_get_value", "cdecl")
    lv_linemeter_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_value.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_min_value", "cdecl"):
        continue
    lv_linemeter_get_min_value = _lib.get("lv_linemeter_get_min_value", "cdecl")
    lv_linemeter_get_min_value.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_min_value.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_max_value", "cdecl"):
        continue
    lv_linemeter_get_max_value = _lib.get("lv_linemeter_get_max_value", "cdecl")
    lv_linemeter_get_max_value.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_max_value.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 134
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_line_count", "cdecl"):
        continue
    lv_linemeter_get_line_count = _lib.get("lv_linemeter_get_line_count", "cdecl")
    lv_linemeter_get_line_count.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_line_count.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 141
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_scale_angle", "cdecl"):
        continue
    lv_linemeter_get_scale_angle = _lib.get("lv_linemeter_get_scale_angle", "cdecl")
    lv_linemeter_get_scale_angle.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_scale_angle.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 148
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_angle_offset", "cdecl"):
        continue
    lv_linemeter_get_angle_offset = _lib.get("lv_linemeter_get_angle_offset", "cdecl")
    lv_linemeter_get_angle_offset.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_angle_offset.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_draw_scale", "cdecl"):
        continue
    lv_linemeter_draw_scale = _lib.get("lv_linemeter_draw_scale", "cdecl")
    lv_linemeter_draw_scale.argtypes = [POINTER(lv_obj_t), POINTER(lv_area_t), c_uint8]
    lv_linemeter_draw_scale.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_linemeter.h: 157
for _lib in _libs.values():
    if not _lib.has("lv_linemeter_get_mirror", "cdecl"):
        continue
    lv_linemeter_get_mirror = _lib.get("lv_linemeter_get_mirror", "cdecl")
    lv_linemeter_get_mirror.argtypes = [POINTER(lv_obj_t)]
    lv_linemeter_get_mirror.restype = c_bool
    break

lv_gauge_format_cb_t = CFUNCTYPE(UNCHECKED(None), POINTER(lv_obj_t), String, c_int, c_int32)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 38

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 53
class struct_anon_188(Structure):
    pass

struct_anon_188.__slots__ = [
    'lmeter',
    'values',
    'needle_colors',
    'needle_img',
    'needle_img_pivot',
    'style_needle',
    'style_strong',
    'needle_count',
    'label_count',
    'format_cb',
]
struct_anon_188._fields_ = [
    ('lmeter', lv_linemeter_ext_t),
    ('values', POINTER(c_int32)),
    ('needle_colors', POINTER(lv_color_t)),
    ('needle_img', POINTER(None)),
    ('needle_img_pivot', lv_point_t),
    ('style_needle', lv_style_list_t),
    ('style_strong', lv_style_list_t),
    ('needle_count', c_uint8),
    ('label_count', c_uint8),
    ('format_cb', lv_gauge_format_cb_t),
]

lv_gauge_ext_t = struct_anon_188# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 53

enum_anon_189 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

LV_GAUGE_PART_MAIN = LV_LINEMETER_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

LV_GAUGE_PART_MAJOR = _LV_LINEMETER_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

LV_GAUGE_PART_NEEDLE = (LV_GAUGE_PART_MAJOR + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

_LV_GAUGE_PART_VIRTUAL_LAST = _LV_LINEMETER_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

_LV_GAUGE_PART_REAL_LAST = _LV_LINEMETER_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 56

lv_gauge_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 63

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_gauge_create", "cdecl"):
        continue
    lv_gauge_create = _lib.get("lv_gauge_create", "cdecl")
    lv_gauge_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_gauge_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 87
for _lib in _libs.values():
    if not _lib.has("lv_gauge_set_needle_count", "cdecl"):
        continue
    lv_gauge_set_needle_count = _lib.get("lv_gauge_set_needle_count", "cdecl")
    lv_gauge_set_needle_count.argtypes = [POINTER(lv_obj_t), c_uint8, POINTER(lv_color_t)]
    lv_gauge_set_needle_count.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_gauge_set_value", "cdecl"):
        continue
    lv_gauge_set_value = _lib.get("lv_gauge_set_value", "cdecl")
    lv_gauge_set_value.argtypes = [POINTER(lv_obj_t), c_uint8, c_int32]
    lv_gauge_set_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_gauge_set_scale", "cdecl"):
        continue
    lv_gauge_set_scale = _lib.get("lv_gauge_set_scale", "cdecl")
    lv_gauge_set_scale.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint8, c_uint8]
    lv_gauge_set_scale.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 148
for _lib in _libs.values():
    if not _lib.has("lv_gauge_set_needle_img", "cdecl"):
        continue
    lv_gauge_set_needle_img = _lib.get("lv_gauge_set_needle_img", "cdecl")
    lv_gauge_set_needle_img.argtypes = [POINTER(lv_obj_t), POINTER(None), lv_coord_t, lv_coord_t]
    lv_gauge_set_needle_img.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 155
for _lib in _libs.values():
    if not _lib.has("lv_gauge_set_formatter_cb", "cdecl"):
        continue
    lv_gauge_set_formatter_cb = _lib.get("lv_gauge_set_formatter_cb", "cdecl")
    lv_gauge_set_formatter_cb.argtypes = [POINTER(lv_obj_t), lv_gauge_format_cb_t]
    lv_gauge_set_formatter_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 167
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_value", "cdecl"):
        continue
    lv_gauge_get_value = _lib.get("lv_gauge_get_value", "cdecl")
    lv_gauge_get_value.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_gauge_get_value.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 174
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_needle_count", "cdecl"):
        continue
    lv_gauge_get_needle_count = _lib.get("lv_gauge_get_needle_count", "cdecl")
    lv_gauge_get_needle_count.argtypes = [POINTER(lv_obj_t)]
    lv_gauge_get_needle_count.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 211
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_label_count", "cdecl"):
        continue
    lv_gauge_get_label_count = _lib.get("lv_gauge_get_label_count", "cdecl")
    lv_gauge_get_label_count.argtypes = [POINTER(lv_obj_t)]
    lv_gauge_get_label_count.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 249
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_needle_img", "cdecl"):
        continue
    lv_gauge_get_needle_img = _lib.get("lv_gauge_get_needle_img", "cdecl")
    lv_gauge_get_needle_img.argtypes = [POINTER(lv_obj_t)]
    lv_gauge_get_needle_img.restype = POINTER(c_ubyte)
    lv_gauge_get_needle_img.errcheck = lambda v,*a : cast(v, c_void_p)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 256
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_needle_img_pivot_x", "cdecl"):
        continue
    lv_gauge_get_needle_img_pivot_x = _lib.get("lv_gauge_get_needle_img_pivot_x", "cdecl")
    lv_gauge_get_needle_img_pivot_x.argtypes = [POINTER(lv_obj_t)]
    lv_gauge_get_needle_img_pivot_x.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_gauge.h: 263
for _lib in _libs.values():
    if not _lib.has("lv_gauge_get_needle_img_pivot_y", "cdecl"):
        continue
    lv_gauge_get_needle_img_pivot_y = _lib.get("lv_gauge_get_needle_img_pivot_y", "cdecl")
    lv_gauge_get_needle_img_pivot_y.argtypes = [POINTER(lv_obj_t)]
    lv_gauge_get_needle_img_pivot_y.restype = lv_coord_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 40
class struct_anon_190(Structure):
    pass

struct_anon_190.__slots__ = [
    'bar',
    'style_knob',
]
struct_anon_190._fields_ = [
    ('bar', lv_bar_ext_t),
    ('style_knob', lv_style_list_t),
]

lv_switch_ext_t = struct_anon_190# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 40

enum_anon_191 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 45

LV_SWITCH_PART_BG = LV_BAR_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 45

LV_SWITCH_PART_INDIC = LV_BAR_PART_INDIC# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 45

LV_SWITCH_PART_KNOB = _LV_BAR_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 45

_LV_SWITCH_PART_VIRTUAL_LAST = (LV_SWITCH_PART_KNOB + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 45

lv_switch_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 52

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 64
for _lib in _libs.values():
    if not _lib.has("lv_switch_create", "cdecl"):
        continue
    lv_switch_create = _lib.get("lv_switch_create", "cdecl")
    lv_switch_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_switch_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 75
for _lib in _libs.values():
    if not _lib.has("lv_switch_on", "cdecl"):
        continue
    lv_switch_on = _lib.get("lv_switch_on", "cdecl")
    lv_switch_on.argtypes = [POINTER(lv_obj_t), lv_anim_enable_t]
    lv_switch_on.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 82
for _lib in _libs.values():
    if not _lib.has("lv_switch_off", "cdecl"):
        continue
    lv_switch_off = _lib.get("lv_switch_off", "cdecl")
    lv_switch_off.argtypes = [POINTER(lv_obj_t), lv_anim_enable_t]
    lv_switch_off.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_switch.h: 90
for _lib in _libs.values():
    if not _lib.has("lv_switch_toggle", "cdecl"):
        continue
    lv_switch_toggle = _lib.get("lv_switch_toggle", "cdecl")
    lv_switch_toggle.argtypes = [POINTER(lv_obj_t), lv_anim_enable_t]
    lv_switch_toggle.restype = c_bool
    break

enum_anon_192 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 30

LV_ARC_TYPE_NORMAL = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 30

LV_ARC_TYPE_SYMMETRIC = (LV_ARC_TYPE_NORMAL + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 30

LV_ARC_TYPE_REVERSE = (LV_ARC_TYPE_SYMMETRIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 30

lv_arc_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 35

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 58
class struct_anon_193(Structure):
    pass

struct_anon_193.__slots__ = [
    'rotation_angle',
    'arc_angle_start',
    'arc_angle_end',
    'bg_angle_start',
    'bg_angle_end',
    'style_arc',
    'style_knob',
    'cur_value',
    'min_value',
    'max_value',
    'dragging',
    'type',
    'adjustable',
    'min_close',
    'chg_rate',
    'last_tick',
    'last_angle',
]
struct_anon_193._fields_ = [
    ('rotation_angle', c_uint16),
    ('arc_angle_start', c_uint16),
    ('arc_angle_end', c_uint16),
    ('bg_angle_start', c_uint16),
    ('bg_angle_end', c_uint16),
    ('style_arc', lv_style_list_t),
    ('style_knob', lv_style_list_t),
    ('cur_value', c_int16),
    ('min_value', c_int16),
    ('max_value', c_int16),
    ('dragging', c_uint16, 1),
    ('type', c_uint16, 2),
    ('adjustable', c_uint16, 1),
    ('min_close', c_uint16, 1),
    ('chg_rate', c_uint16),
    ('last_tick', c_uint32),
    ('last_angle', c_int16),
]

lv_arc_ext_t = struct_anon_193# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 58

enum_anon_194 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

LV_ARC_PART_BG = LV_OBJ_PART_MAIN# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

LV_ARC_PART_INDIC = (LV_ARC_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

LV_ARC_PART_KNOB = (LV_ARC_PART_INDIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

_LV_ARC_PART_VIRTUAL_LAST = (LV_ARC_PART_KNOB + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

_LV_ARC_PART_REAL_LAST = _LV_OBJ_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 61

lv_arc_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 68

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 80
for _lib in _libs.values():
    if not _lib.has("lv_arc_create", "cdecl"):
        continue
    lv_arc_create = _lib.get("lv_arc_create", "cdecl")
    lv_arc_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_arc_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 95
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_start_angle", "cdecl"):
        continue
    lv_arc_set_start_angle = _lib.get("lv_arc_set_start_angle", "cdecl")
    lv_arc_set_start_angle.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_start_angle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_end_angle", "cdecl"):
        continue
    lv_arc_set_end_angle = _lib.get("lv_arc_set_end_angle", "cdecl")
    lv_arc_set_end_angle.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_end_angle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 110
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_angles", "cdecl"):
        continue
    lv_arc_set_angles = _lib.get("lv_arc_set_angles", "cdecl")
    lv_arc_set_angles.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_arc_set_angles.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 117
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_bg_start_angle", "cdecl"):
        continue
    lv_arc_set_bg_start_angle = _lib.get("lv_arc_set_bg_start_angle", "cdecl")
    lv_arc_set_bg_start_angle.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_bg_start_angle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 124
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_bg_end_angle", "cdecl"):
        continue
    lv_arc_set_bg_end_angle = _lib.get("lv_arc_set_bg_end_angle", "cdecl")
    lv_arc_set_bg_end_angle.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_bg_end_angle.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 132
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_bg_angles", "cdecl"):
        continue
    lv_arc_set_bg_angles = _lib.get("lv_arc_set_bg_angles", "cdecl")
    lv_arc_set_bg_angles.argtypes = [POINTER(lv_obj_t), c_uint16, c_uint16]
    lv_arc_set_bg_angles.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 139
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_rotation", "cdecl"):
        continue
    lv_arc_set_rotation = _lib.get("lv_arc_set_rotation", "cdecl")
    lv_arc_set_rotation.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_rotation.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 146
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_type", "cdecl"):
        continue
    lv_arc_set_type = _lib.get("lv_arc_set_type", "cdecl")
    lv_arc_set_type.argtypes = [POINTER(lv_obj_t), lv_arc_type_t]
    lv_arc_set_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 153
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_value", "cdecl"):
        continue
    lv_arc_set_value = _lib.get("lv_arc_set_value", "cdecl")
    lv_arc_set_value.argtypes = [POINTER(lv_obj_t), c_int16]
    lv_arc_set_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 161
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_range", "cdecl"):
        continue
    lv_arc_set_range = _lib.get("lv_arc_set_range", "cdecl")
    lv_arc_set_range.argtypes = [POINTER(lv_obj_t), c_int16, c_int16]
    lv_arc_set_range.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 169
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_chg_rate", "cdecl"):
        continue
    lv_arc_set_chg_rate = _lib.get("lv_arc_set_chg_rate", "cdecl")
    lv_arc_set_chg_rate.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_arc_set_chg_rate.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 176
for _lib in _libs.values():
    if not _lib.has("lv_arc_set_adjustable", "cdecl"):
        continue
    lv_arc_set_adjustable = _lib.get("lv_arc_set_adjustable", "cdecl")
    lv_arc_set_adjustable.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_arc_set_adjustable.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 187
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_angle_start", "cdecl"):
        continue
    lv_arc_get_angle_start = _lib.get("lv_arc_get_angle_start", "cdecl")
    lv_arc_get_angle_start.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_angle_start.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 194
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_angle_end", "cdecl"):
        continue
    lv_arc_get_angle_end = _lib.get("lv_arc_get_angle_end", "cdecl")
    lv_arc_get_angle_end.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_angle_end.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 201
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_bg_angle_start", "cdecl"):
        continue
    lv_arc_get_bg_angle_start = _lib.get("lv_arc_get_bg_angle_start", "cdecl")
    lv_arc_get_bg_angle_start.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_bg_angle_start.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 208
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_bg_angle_end", "cdecl"):
        continue
    lv_arc_get_bg_angle_end = _lib.get("lv_arc_get_bg_angle_end", "cdecl")
    lv_arc_get_bg_angle_end.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_bg_angle_end.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 215
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_type", "cdecl"):
        continue
    lv_arc_get_type = _lib.get("lv_arc_get_type", "cdecl")
    lv_arc_get_type.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_type.restype = lv_arc_type_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 222
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_value", "cdecl"):
        continue
    lv_arc_get_value = _lib.get("lv_arc_get_value", "cdecl")
    lv_arc_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 229
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_min_value", "cdecl"):
        continue
    lv_arc_get_min_value = _lib.get("lv_arc_get_min_value", "cdecl")
    lv_arc_get_min_value.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_min_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 236
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_max_value", "cdecl"):
        continue
    lv_arc_get_max_value = _lib.get("lv_arc_get_max_value", "cdecl")
    lv_arc_get_max_value.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_max_value.restype = c_int16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 243
for _lib in _libs.values():
    if not _lib.has("lv_arc_is_dragged", "cdecl"):
        continue
    lv_arc_is_dragged = _lib.get("lv_arc_is_dragged", "cdecl")
    lv_arc_is_dragged.argtypes = [POINTER(lv_obj_t)]
    lv_arc_is_dragged.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_arc.h: 250
for _lib in _libs.values():
    if not _lib.has("lv_arc_get_adjustable", "cdecl"):
        continue
    lv_arc_get_adjustable = _lib.get("lv_arc_get_adjustable", "cdecl")
    lv_arc_get_adjustable.argtypes = [POINTER(lv_obj_t)]
    lv_arc_get_adjustable.restype = c_bool
    break

enum_anon_195 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 44

LV_SPINNER_TYPE_SPINNING_ARC = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 44

LV_SPINNER_TYPE_FILLSPIN_ARC = (LV_SPINNER_TYPE_SPINNING_ARC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 44

LV_SPINNER_TYPE_CONSTANT_ARC = (LV_SPINNER_TYPE_FILLSPIN_ARC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 44

lv_spinner_type_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 49

enum_anon_196 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 54

LV_SPINNER_DIR_FORWARD = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 54

LV_SPINNER_DIR_BACKWARD = (LV_SPINNER_DIR_FORWARD + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 54

lv_spinner_dir_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 58

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 68
class struct_anon_197(Structure):
    pass

struct_anon_197.__slots__ = [
    'arc',
    'arc_length',
    'time',
    'anim_type',
    'anim_dir',
]
struct_anon_197._fields_ = [
    ('arc', lv_arc_ext_t),
    ('arc_length', lv_anim_value_t),
    ('time', c_uint16),
    ('anim_type', lv_spinner_type_t, 2),
    ('anim_dir', lv_spinner_dir_t, 1),
]

lv_spinner_ext_t = struct_anon_197# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 68

enum_anon_198 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 71

LV_SPINNER_PART_BG = LV_ARC_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 71

LV_SPINNER_PART_INDIC = LV_ARC_PART_INDIC# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 71

_LV_SPINNER_PART_VIRTUAL_LAST = (LV_SPINNER_PART_INDIC + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 71

_LV_SPINNER_PART_REAL_LAST = _LV_ARC_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 71

lv_spinner_style_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 78

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 91
for _lib in _libs.values():
    if not _lib.has("lv_spinner_create", "cdecl"):
        continue
    lv_spinner_create = _lib.get("lv_spinner_create", "cdecl")
    lv_spinner_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_spinner_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_spinner_set_arc_length", "cdecl"):
        continue
    lv_spinner_set_arc_length = _lib.get("lv_spinner_set_arc_length", "cdecl")
    lv_spinner_set_arc_length.argtypes = [POINTER(lv_obj_t), lv_anim_value_t]
    lv_spinner_set_arc_length.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 109
for _lib in _libs.values():
    if not _lib.has("lv_spinner_set_spin_time", "cdecl"):
        continue
    lv_spinner_set_spin_time = _lib.get("lv_spinner_set_spin_time", "cdecl")
    lv_spinner_set_spin_time.argtypes = [POINTER(lv_obj_t), c_uint16]
    lv_spinner_set_spin_time.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_spinner_set_type", "cdecl"):
        continue
    lv_spinner_set_type = _lib.get("lv_spinner_set_type", "cdecl")
    lv_spinner_set_type.argtypes = [POINTER(lv_obj_t), lv_spinner_type_t]
    lv_spinner_set_type.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 127
for _lib in _libs.values():
    if not _lib.has("lv_spinner_set_dir", "cdecl"):
        continue
    lv_spinner_set_dir = _lib.get("lv_spinner_set_dir", "cdecl")
    lv_spinner_set_dir.argtypes = [POINTER(lv_obj_t), lv_spinner_dir_t]
    lv_spinner_set_dir.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 137
for _lib in _libs.values():
    if not _lib.has("lv_spinner_get_arc_length", "cdecl"):
        continue
    lv_spinner_get_arc_length = _lib.get("lv_spinner_get_arc_length", "cdecl")
    lv_spinner_get_arc_length.argtypes = [POINTER(lv_obj_t)]
    lv_spinner_get_arc_length.restype = lv_anim_value_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 143
for _lib in _libs.values():
    if not _lib.has("lv_spinner_get_spin_time", "cdecl"):
        continue
    lv_spinner_get_spin_time = _lib.get("lv_spinner_get_spin_time", "cdecl")
    lv_spinner_get_spin_time.argtypes = [POINTER(lv_obj_t)]
    lv_spinner_get_spin_time.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 150
for _lib in _libs.values():
    if not _lib.has("lv_spinner_get_type", "cdecl"):
        continue
    lv_spinner_get_type = _lib.get("lv_spinner_get_type", "cdecl")
    lv_spinner_get_type.argtypes = [POINTER(lv_obj_t)]
    lv_spinner_get_type.restype = lv_spinner_type_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 157
for _lib in _libs.values():
    if not _lib.has("lv_spinner_get_dir", "cdecl"):
        continue
    lv_spinner_get_dir = _lib.get("lv_spinner_get_dir", "cdecl")
    lv_spinner_get_dir.argtypes = [POINTER(lv_obj_t)]
    lv_spinner_get_dir.restype = lv_spinner_dir_t
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinner.h: 168
for _lib in _libs.values():
    if not _lib.has("lv_spinner_anim_cb", "cdecl"):
        continue
    lv_spinner_anim_cb = _lib.get("lv_spinner_anim_cb", "cdecl")
    lv_spinner_anim_cb.argtypes = [POINTER(None), lv_anim_value_t]
    lv_spinner_anim_cb.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 37
class struct_anon_199(Structure):
    pass

struct_anon_199.__slots__ = [
    'year',
    'month',
    'day',
]
struct_anon_199._fields_ = [
    ('year', c_uint16),
    ('month', c_int8),
    ('day', c_int8),
]

lv_calendar_date_t = struct_anon_199# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 37

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 57
class struct_anon_200(Structure):
    pass

struct_anon_200.__slots__ = [
    'today',
    'showed_date',
    'highlighted_dates',
    'btn_pressing',
    'highlighted_dates_num',
    'pressed_date',
    'day_names',
    'month_names',
    'style_header',
    'style_day_names',
    'style_date_nums',
]
struct_anon_200._fields_ = [
    ('today', lv_calendar_date_t),
    ('showed_date', lv_calendar_date_t),
    ('highlighted_dates', POINTER(lv_calendar_date_t)),
    ('btn_pressing', c_int8),
    ('highlighted_dates_num', c_uint16),
    ('pressed_date', lv_calendar_date_t),
    ('day_names', POINTER(POINTER(c_char))),
    ('month_names', POINTER(POINTER(c_char))),
    ('style_header', lv_style_list_t),
    ('style_day_names', lv_style_list_t),
    ('style_date_nums', lv_style_list_t),
]

lv_calendar_ext_t = struct_anon_200# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 57

enum_anon_201 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 60

LV_CALENDAR_PART_BG = 0# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 60

LV_CALENDAR_PART_HEADER = (LV_CALENDAR_PART_BG + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 60

LV_CALENDAR_PART_DAY_NAMES = (LV_CALENDAR_PART_HEADER + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 60

LV_CALENDAR_PART_DATE = (LV_CALENDAR_PART_DAY_NAMES + 1)# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 60

lv_calendar_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 66

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 78
for _lib in _libs.values():
    if not _lib.has("lv_calendar_create", "cdecl"):
        continue
    lv_calendar_create = _lib.get("lv_calendar_create", "cdecl")
    lv_calendar_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_calendar_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 94
for _lib in _libs.values():
    if not _lib.has("lv_calendar_set_today_date", "cdecl"):
        continue
    lv_calendar_set_today_date = _lib.get("lv_calendar_set_today_date", "cdecl")
    lv_calendar_set_today_date.argtypes = [POINTER(lv_obj_t), POINTER(lv_calendar_date_t)]
    lv_calendar_set_today_date.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 102
for _lib in _libs.values():
    if not _lib.has("lv_calendar_set_showed_date", "cdecl"):
        continue
    lv_calendar_set_showed_date = _lib.get("lv_calendar_set_showed_date", "cdecl")
    lv_calendar_set_showed_date.argtypes = [POINTER(lv_obj_t), POINTER(lv_calendar_date_t)]
    lv_calendar_set_showed_date.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 111
for _lib in _libs.values():
    if not _lib.has("lv_calendar_set_highlighted_dates", "cdecl"):
        continue
    lv_calendar_set_highlighted_dates = _lib.get("lv_calendar_set_highlighted_dates", "cdecl")
    lv_calendar_set_highlighted_dates.argtypes = [POINTER(lv_obj_t), POINTER(lv_calendar_date_t), c_uint16]
    lv_calendar_set_highlighted_dates.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 120
for _lib in _libs.values():
    if not _lib.has("lv_calendar_set_day_names", "cdecl"):
        continue
    lv_calendar_set_day_names = _lib.get("lv_calendar_set_day_names", "cdecl")
    lv_calendar_set_day_names.argtypes = [POINTER(lv_obj_t), POINTER(POINTER(c_char))]
    lv_calendar_set_day_names.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_calendar_set_month_names", "cdecl"):
        continue
    lv_calendar_set_month_names = _lib.get("lv_calendar_set_month_names", "cdecl")
    lv_calendar_set_month_names.argtypes = [POINTER(lv_obj_t), POINTER(POINTER(c_char))]
    lv_calendar_set_month_names.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 140
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_today_date", "cdecl"):
        continue
    lv_calendar_get_today_date = _lib.get("lv_calendar_get_today_date", "cdecl")
    lv_calendar_get_today_date.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_today_date.restype = POINTER(lv_calendar_date_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 147
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_showed_date", "cdecl"):
        continue
    lv_calendar_get_showed_date = _lib.get("lv_calendar_get_showed_date", "cdecl")
    lv_calendar_get_showed_date.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_showed_date.restype = POINTER(lv_calendar_date_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 155
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_pressed_date", "cdecl"):
        continue
    lv_calendar_get_pressed_date = _lib.get("lv_calendar_get_pressed_date", "cdecl")
    lv_calendar_get_pressed_date.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_pressed_date.restype = POINTER(lv_calendar_date_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 162
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_highlighted_dates", "cdecl"):
        continue
    lv_calendar_get_highlighted_dates = _lib.get("lv_calendar_get_highlighted_dates", "cdecl")
    lv_calendar_get_highlighted_dates.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_highlighted_dates.restype = POINTER(lv_calendar_date_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 169
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_highlighted_dates_num", "cdecl"):
        continue
    lv_calendar_get_highlighted_dates_num = _lib.get("lv_calendar_get_highlighted_dates_num", "cdecl")
    lv_calendar_get_highlighted_dates_num.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_highlighted_dates_num.restype = c_uint16
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 176
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_day_names", "cdecl"):
        continue
    lv_calendar_get_day_names = _lib.get("lv_calendar_get_day_names", "cdecl")
    lv_calendar_get_day_names.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_day_names.restype = POINTER(POINTER(c_char))
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 183
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_month_names", "cdecl"):
        continue
    lv_calendar_get_month_names = _lib.get("lv_calendar_get_month_names", "cdecl")
    lv_calendar_get_month_names.argtypes = [POINTER(lv_obj_t)]
    lv_calendar_get_month_names.restype = POINTER(POINTER(c_char))
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_calendar.h: 192
for _lib in _libs.values():
    if not _lib.has("lv_calendar_get_day_of_week", "cdecl"):
        continue
    lv_calendar_get_day_of_week = _lib.get("lv_calendar_get_day_of_week", "cdecl")
    lv_calendar_get_day_of_week.argtypes = [c_uint32, c_uint32, c_uint32]
    lv_calendar_get_day_of_week.restype = c_uint8
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 49
class struct_anon_202(Structure):
    pass

struct_anon_202.__slots__ = [
    'ta',
    'value',
    'range_max',
    'range_min',
    'step',
    'rollover',
    'digit_count',
    'dec_point_pos',
    'digit_padding_left',
]
struct_anon_202._fields_ = [
    ('ta', lv_textarea_ext_t),
    ('value', c_int32),
    ('range_max', c_int32),
    ('range_min', c_int32),
    ('step', c_int32),
    ('rollover', c_uint8, 1),
    ('digit_count', c_uint16, 4),
    ('dec_point_pos', c_uint16, 4),
    ('digit_padding_left', c_uint16, 4),
]

lv_spinbox_ext_t = struct_anon_202# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 49

enum_anon_203 = c_int# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 52

LV_SPINBOX_PART_BG = LV_TEXTAREA_PART_BG# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 52

LV_SPINBOX_PART_CURSOR = LV_TEXTAREA_PART_CURSOR# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 52

_LV_SPINBOX_PART_VIRTUAL_LAST = _LV_TEXTAREA_PART_VIRTUAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 52

_LV_SPINBOX_PART_REAL_LAST = _LV_TEXTAREA_PART_REAL_LAST# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 52

lv_spinbox_part_t = c_uint8# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 58

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 70
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_create", "cdecl"):
        continue
    lv_spinbox_create = _lib.get("lv_spinbox_create", "cdecl")
    lv_spinbox_create.argtypes = [POINTER(lv_obj_t), POINTER(lv_obj_t)]
    lv_spinbox_create.restype = POINTER(lv_obj_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 81
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_rollover", "cdecl"):
        continue
    lv_spinbox_set_rollover = _lib.get("lv_spinbox_set_rollover", "cdecl")
    lv_spinbox_set_rollover.argtypes = [POINTER(lv_obj_t), c_bool]
    lv_spinbox_set_rollover.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 88
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_value", "cdecl"):
        continue
    lv_spinbox_set_value = _lib.get("lv_spinbox_set_value", "cdecl")
    lv_spinbox_set_value.argtypes = [POINTER(lv_obj_t), c_int32]
    lv_spinbox_set_value.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 97
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_digit_format", "cdecl"):
        continue
    lv_spinbox_set_digit_format = _lib.get("lv_spinbox_set_digit_format", "cdecl")
    lv_spinbox_set_digit_format.argtypes = [POINTER(lv_obj_t), c_uint8, c_uint8]
    lv_spinbox_set_digit_format.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 104
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_step", "cdecl"):
        continue
    lv_spinbox_set_step = _lib.get("lv_spinbox_set_step", "cdecl")
    lv_spinbox_set_step.argtypes = [POINTER(lv_obj_t), c_uint32]
    lv_spinbox_set_step.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 112
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_range", "cdecl"):
        continue
    lv_spinbox_set_range = _lib.get("lv_spinbox_set_range", "cdecl")
    lv_spinbox_set_range.argtypes = [POINTER(lv_obj_t), c_int32, c_int32]
    lv_spinbox_set_range.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 119
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_set_padding_left", "cdecl"):
        continue
    lv_spinbox_set_padding_left = _lib.get("lv_spinbox_set_padding_left", "cdecl")
    lv_spinbox_set_padding_left.argtypes = [POINTER(lv_obj_t), c_uint8]
    lv_spinbox_set_padding_left.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 129
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_get_rollover", "cdecl"):
        continue
    lv_spinbox_get_rollover = _lib.get("lv_spinbox_get_rollover", "cdecl")
    lv_spinbox_get_rollover.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_get_rollover.restype = c_bool
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 136
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_get_value", "cdecl"):
        continue
    lv_spinbox_get_value = _lib.get("lv_spinbox_get_value", "cdecl")
    lv_spinbox_get_value.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_get_value.restype = c_int32
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 146
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_step_next", "cdecl"):
        continue
    lv_spinbox_step_next = _lib.get("lv_spinbox_step_next", "cdecl")
    lv_spinbox_step_next.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_step_next.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 152
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_step_prev", "cdecl"):
        continue
    lv_spinbox_step_prev = _lib.get("lv_spinbox_step_prev", "cdecl")
    lv_spinbox_step_prev.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_step_prev.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 158
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_increment", "cdecl"):
        continue
    lv_spinbox_increment = _lib.get("lv_spinbox_increment", "cdecl")
    lv_spinbox_increment.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_increment.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 164
for _lib in _libs.values():
    if not _lib.has("lv_spinbox_decrement", "cdecl"):
        continue
    lv_spinbox_decrement = _lib.get("lv_spinbox_decrement", "cdecl")
    lv_spinbox_decrement.argtypes = [POINTER(lv_obj_t)]
    lv_spinbox_decrement.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_draw/lv_img_cache.h: 38
class struct_anon_204(Structure):
    pass

struct_anon_204.__slots__ = [
    'dec_dsc',
    'life',
]
struct_anon_204._fields_ = [
    ('dec_dsc', lv_img_decoder_dsc_t),
    ('life', c_int32),
]

lv_img_cache_entry_t = struct_anon_204# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_draw/lv_img_cache.h: 38

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_draw/lv_img_cache.h: 52
for _lib in _libs.values():
    if not _lib.has("_lv_img_cache_open", "cdecl"):
        continue
    _lv_img_cache_open = _lib.get("_lv_img_cache_open", "cdecl")
    _lv_img_cache_open.argtypes = [POINTER(None), lv_color_t]
    _lv_img_cache_open.restype = POINTER(lv_img_cache_entry_t)
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_draw/lv_img_cache.h: 60
for _lib in _libs.values():
    if not _lib.has("lv_img_cache_set_size", "cdecl"):
        continue
    lv_img_cache_set_size = _lib.get("lv_img_cache_set_size", "cdecl")
    lv_img_cache_set_size.argtypes = [c_uint16]
    lv_img_cache_set_size.restype = None
    break

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_draw/lv_img_cache.h: 67
for _lib in _libs.values():
    if not _lib.has("lv_img_cache_invalidate_src", "cdecl"):
        continue
    lv_img_cache_invalidate_src = _lib.get("lv_img_cache_invalidate_src", "cdecl")
    lv_img_cache_invalidate_src.argtypes = [POINTER(None)]
    lv_img_cache_invalidate_src.restype = None
    break

# <built-in>
try:
    __WCHAR_MAX__ = 2147483647
except:
    pass

# <built-in>
try:
    __WCHAR_MIN__ = ((-__WCHAR_MAX__) - 1)
except:
    pass

__const = c_int# <command-line>: 4

# <command-line>: 7
try:
    CTYPESGEN = 1
except:
    pass

# /usr/include/stdc-predef.h: 19
try:
    _STDC_PREDEF_H = 1
except:
    pass

# /usr/include/stdc-predef.h: 38
try:
    __STDC_IEC_559__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 46
try:
    __STDC_IEC_559_COMPLEX__ = 1
except:
    pass

# /usr/include/stdc-predef.h: 58
try:
    __STDC_ISO_10646__ = 201706.0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/lvgl.h: 17
try:
    LVGL_VERSION_MAJOR = 7
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/lvgl.h: 18
try:
    LVGL_VERSION_MINOR = 8
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/lvgl.h: 19
try:
    LVGL_VERSION_PATCH = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/lvgl.h: 20
try:
    LVGL_VERSION_INFO = 'dev'
except:
    pass

# /usr/include/stdint.h: 23
try:
    _STDINT_H = 1
except:
    pass

# /usr/include/features.h: 19
try:
    _FEATURES_H = 1
except:
    pass

# /usr/include/features.h: 164
def __GNUC_PREREQ(maj, min):
    return 0

# /usr/include/features.h: 175
def __glibc_clang_prereq(maj, min):
    return 0

# /usr/include/features.h: 227
try:
    _DEFAULT_SOURCE = 1
except:
    pass

# /usr/include/features.h: 235
try:
    __GLIBC_USE_ISOC2X = 0
except:
    pass

# /usr/include/features.h: 241
try:
    __USE_ISOC11 = 1
except:
    pass

# /usr/include/features.h: 248
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 255
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 276
try:
    __USE_POSIX_IMPLICITLY = 1
except:
    pass

# /usr/include/features.h: 279
try:
    _POSIX_SOURCE = 1
except:
    pass

# /usr/include/features.h: 281
try:
    _POSIX_C_SOURCE = 200809.0
except:
    pass

# /usr/include/features.h: 316
try:
    __USE_POSIX = 1
except:
    pass

# /usr/include/features.h: 320
try:
    __USE_POSIX2 = 1
except:
    pass

# /usr/include/features.h: 324
try:
    __USE_POSIX199309 = 1
except:
    pass

# /usr/include/features.h: 328
try:
    __USE_POSIX199506 = 1
except:
    pass

# /usr/include/features.h: 332
try:
    __USE_XOPEN2K = 1
except:
    pass

# /usr/include/features.h: 333
# #undef __USE_ISOC95
try:
    del __USE_ISOC95
except NameError:
    pass

# /usr/include/features.h: 334
try:
    __USE_ISOC95 = 1
except:
    pass

# /usr/include/features.h: 335
# #undef __USE_ISOC99
try:
    del __USE_ISOC99
except NameError:
    pass

# /usr/include/features.h: 336
try:
    __USE_ISOC99 = 1
except:
    pass

# /usr/include/features.h: 340
try:
    __USE_XOPEN2K8 = 1
except:
    pass

# /usr/include/features.h: 342
try:
    _ATFILE_SOURCE = 1
except:
    pass

# /usr/include/features.h: 384
try:
    __USE_MISC = 1
except:
    pass

# /usr/include/features.h: 388
try:
    __USE_ATFILE = 1
except:
    pass

# /usr/include/features.h: 407
try:
    __USE_FORTIFY_LEVEL = 0
except:
    pass

# /usr/include/features.h: 415
try:
    __GLIBC_USE_DEPRECATED_GETS = 0
except:
    pass

# /usr/include/features.h: 438
try:
    __GLIBC_USE_DEPRECATED_SCANF = 0
except:
    pass

# /usr/include/features.h: 452
try:
    __GNU_LIBRARY__ = 6
except:
    pass

# /usr/include/features.h: 456
try:
    __GLIBC__ = 2
except:
    pass

# /usr/include/features.h: 457
try:
    __GLIBC_MINOR__ = 32
except:
    pass

# /usr/include/features.h: 459
def __GLIBC_PREREQ(maj, min):
    return (((__GLIBC__ << 16) + __GLIBC_MINOR__) >= ((maj << 16) + min))

# /usr/include/sys/cdefs.h: 19
try:
    _SYS_CDEFS_H = 1
except:
    pass

# /usr/include/sys/cdefs.h: 84
def __NTH(fct):
    return fct

# /usr/include/sys/cdefs.h: 94
def __glibc_clang_has_extension(ext):
    return 0

# /usr/include/sys/cdefs.h: 99
def __P(args):
    return args

# /usr/include/sys/cdefs.h: 100
def __PMT(args):
    return args

# /usr/include/sys/cdefs.h: 106
def __STRING(x):
    return x

__ptr_t = POINTER(None)# /usr/include/sys/cdefs.h: 109

# /usr/include/sys/cdefs.h: 144
try:
    __glibc_c99_flexarr_available = 1
except:
    pass

# /usr/include/sys/cdefs.h: 405
def __glibc_unlikely(cond):
    return cond

# /usr/include/sys/cdefs.h: 406
def __glibc_likely(cond):
    return cond

# /usr/include/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/bits/long-double.h: 21
try:
    __LDOUBLE_REDIRECTS_TO_FLOAT128_ABI = 0
except:
    pass

# /usr/include/sys/cdefs.h: 508
def __LDBL_REDIR1(name, proto, alias):
    return (name + proto)

# /usr/include/sys/cdefs.h: 509
def __LDBL_REDIR(name, proto):
    return (name + proto)

# /usr/include/sys/cdefs.h: 546
try:
    __HAVE_GENERIC_SELECTION = 1
except:
    pass

# /usr/include/bits/libc-header-start.h: 42
try:
    __GLIBC_USE_LIB_EXT2 = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 53
try:
    __GLIBC_USE_IEC_60559_BFP_EXT = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 59
try:
    __GLIBC_USE_IEC_60559_BFP_EXT_C2X = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 70
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 76
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 85
try:
    __GLIBC_USE_IEC_60559_TYPES_EXT = 0
except:
    pass

# /usr/include/bits/types.h: 24
try:
    _BITS_TYPES_H = 1
except:
    pass

# /usr/include/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/bits/timesize.h: 24
try:
    __TIMESIZE = __WORDSIZE
except:
    pass

__S16_TYPE = c_int# /usr/include/bits/types.h: 109

__U16_TYPE = c_uint# /usr/include/bits/types.h: 110

__S32_TYPE = c_int# /usr/include/bits/types.h: 111

__U32_TYPE = c_uint# /usr/include/bits/types.h: 112

__SLONGWORD_TYPE = c_long# /usr/include/bits/types.h: 113

__ULONGWORD_TYPE = c_ulong# /usr/include/bits/types.h: 114

__SQUAD_TYPE = c_long# /usr/include/bits/types.h: 128

__UQUAD_TYPE = c_ulong# /usr/include/bits/types.h: 129

__SWORD_TYPE = c_long# /usr/include/bits/types.h: 130

__UWORD_TYPE = c_ulong# /usr/include/bits/types.h: 131

__SLONG32_TYPE = c_int# /usr/include/bits/types.h: 132

__ULONG32_TYPE = c_uint# /usr/include/bits/types.h: 133

__S64_TYPE = c_long# /usr/include/bits/types.h: 134

__U64_TYPE = c_ulong# /usr/include/bits/types.h: 135

# /usr/include/bits/typesizes.h: 24
try:
    _BITS_TYPESIZES_H = 1
except:
    pass

__TIMER_T_TYPE = POINTER(None)# /usr/include/bits/typesizes.h: 71

# /usr/include/bits/typesizes.h: 73
class struct_anon_205(Structure):
    pass

struct_anon_205.__slots__ = [
    '__val',
]
struct_anon_205._fields_ = [
    ('__val', c_int * int(2)),
]

__FSID_T_TYPE = struct_anon_205# /usr/include/bits/typesizes.h: 73

# /usr/include/bits/typesizes.h: 81
try:
    __OFF_T_MATCHES_OFF64_T = 1
except:
    pass

# /usr/include/bits/typesizes.h: 84
try:
    __INO_T_MATCHES_INO64_T = 1
except:
    pass

# /usr/include/bits/typesizes.h: 87
try:
    __RLIM_T_MATCHES_RLIM64_T = 1
except:
    pass

# /usr/include/bits/typesizes.h: 90
try:
    __STATFS_MATCHES_STATFS64 = 1
except:
    pass

# /usr/include/bits/typesizes.h: 93
try:
    __KERNEL_OLD_TIMEVAL_MATCHES_TIMEVAL64 = 1
except:
    pass

# /usr/include/bits/typesizes.h: 103
try:
    __FD_SETSIZE = 1024
except:
    pass

# /usr/include/bits/time64.h: 24
try:
    _BITS_TIME64_H = 1
except:
    pass

# /usr/include/bits/wchar.h: 20
try:
    _BITS_WCHAR_H = 1
except:
    pass

# /usr/include/bits/wchar.h: 34
try:
    __WCHAR_MAX = __WCHAR_MAX__
except:
    pass

# /usr/include/bits/wchar.h: 42
try:
    __WCHAR_MIN = __WCHAR_MIN__
except:
    pass

# /usr/include/bits/wordsize.h: 4
try:
    __WORDSIZE = 64
except:
    pass

# /usr/include/bits/wordsize.h: 12
try:
    __WORDSIZE_TIME64_COMPAT32 = 1
except:
    pass

# /usr/include/bits/wordsize.h: 14
try:
    __SYSCALL_WORDSIZE = 64
except:
    pass

# /usr/include/bits/stdint-intn.h: 20
try:
    _BITS_STDINT_INTN_H = 1
except:
    pass

# /usr/include/bits/stdint-uintn.h: 20
try:
    _BITS_STDINT_UINTN_H = 1
except:
    pass

# /usr/include/stdint.h: 116
try:
    INT8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 117
try:
    INT16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 118
try:
    INT32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 121
try:
    INT8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 122
try:
    INT16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 123
try:
    INT32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 127
try:
    UINT8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 128
try:
    UINT16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 129
try:
    UINT32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 134
try:
    INT_LEAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 135
try:
    INT_LEAST16_MIN = ((-32767) - 1)
except:
    pass

# /usr/include/stdint.h: 136
try:
    INT_LEAST32_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 139
try:
    INT_LEAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 140
try:
    INT_LEAST16_MAX = 32767
except:
    pass

# /usr/include/stdint.h: 141
try:
    INT_LEAST32_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 145
try:
    UINT_LEAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 146
try:
    UINT_LEAST16_MAX = 65535
except:
    pass

# /usr/include/stdint.h: 147
try:
    UINT_LEAST32_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 152
try:
    INT_FAST8_MIN = (-128)
except:
    pass

# /usr/include/stdint.h: 154
try:
    INT_FAST16_MIN = ((-9.223372036854776e+18) - 1)
except:
    pass

# /usr/include/stdint.h: 155
try:
    INT_FAST32_MIN = ((-9.223372036854776e+18) - 1)
except:
    pass

# /usr/include/stdint.h: 162
try:
    INT_FAST8_MAX = 127
except:
    pass

# /usr/include/stdint.h: 164
try:
    INT_FAST16_MAX = 9.223372036854776e+18
except:
    pass

# /usr/include/stdint.h: 165
try:
    INT_FAST32_MAX = 9.223372036854776e+18
except:
    pass

# /usr/include/stdint.h: 173
try:
    UINT_FAST8_MAX = 255
except:
    pass

# /usr/include/stdint.h: 175
try:
    UINT_FAST16_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 176
try:
    UINT_FAST32_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 186
try:
    INTPTR_MIN = ((-9.223372036854776e+18) - 1)
except:
    pass

# /usr/include/stdint.h: 187
try:
    INTPTR_MAX = 9.223372036854776e+18
except:
    pass

# /usr/include/stdint.h: 188
try:
    UINTPTR_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 209
try:
    PTRDIFF_MIN = ((-9.223372036854776e+18) - 1)
except:
    pass

# /usr/include/stdint.h: 210
try:
    PTRDIFF_MAX = 9.223372036854776e+18
except:
    pass

# /usr/include/stdint.h: 222
try:
    SIG_ATOMIC_MIN = ((-2147483647) - 1)
except:
    pass

# /usr/include/stdint.h: 223
try:
    SIG_ATOMIC_MAX = 2147483647
except:
    pass

# /usr/include/stdint.h: 227
try:
    SIZE_MAX = 18446744073709551615
except:
    pass

# /usr/include/stdint.h: 239
try:
    WCHAR_MIN = __WCHAR_MIN
except:
    pass

# /usr/include/stdint.h: 240
try:
    WCHAR_MAX = __WCHAR_MAX
except:
    pass

# /usr/include/stdint.h: 244
try:
    WINT_MIN = 0
except:
    pass

# /usr/include/stdint.h: 245
try:
    WINT_MAX = 4294967295
except:
    pass

# /usr/include/stdint.h: 248
def INT8_C(c):
    return c

# /usr/include/stdint.h: 249
def INT16_C(c):
    return c

# /usr/include/stdint.h: 250
def INT32_C(c):
    return c

# /usr/include/stdint.h: 258
def UINT8_C(c):
    return c

# /usr/include/stdint.h: 259
def UINT16_C(c):
    return c

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 23
try:
    LV_HOR_RES_MAX = 1920
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 24
try:
    LV_VER_RES_MAX = 1080
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 32
try:
    LV_COLOR_DEPTH = 32
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 36
try:
    LV_COLOR_16_SWAP = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 41
try:
    LV_COLOR_SCREEN_TRANSP = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 47
try:
    LV_ANTIALIAS = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 51
try:
    LV_DISP_DEF_REFR_PERIOD = 30
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 56
try:
    LV_DPI = 130
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 65
try:
    LV_DISP_SMALL_LIMIT = 30
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 66
try:
    LV_DISP_MEDIUM_LIMIT = 50
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 67
try:
    LV_DISP_LARGE_LIMIT = 70
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 80
try:
    LV_MEM_CUSTOM = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 83
try:
    LV_MEM_SIZE = (32 * 1024)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 90
try:
    LV_MEM_ADR = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 93
try:
    LV_MEM_AUTO_DEFRAG = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 102
try:
    LV_MEMCPY_MEMSET_STD = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 106
try:
    LV_ENABLE_GC = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 121
try:
    LV_INDEV_DEF_READ_PERIOD = 30
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 124
try:
    LV_INDEV_DEF_DRAG_LIMIT = 10
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 127
try:
    LV_INDEV_DEF_DRAG_THROW = 10
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 131
try:
    LV_INDEV_DEF_LONG_PRESS_TIME = 400
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 135
try:
    LV_INDEV_DEF_LONG_PRESS_REP_TIME = 100
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 139
try:
    LV_INDEV_DEF_GESTURE_LIMIT = 50
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 142
try:
    LV_INDEV_DEF_GESTURE_MIN_VELOCITY = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 149
try:
    LV_USE_ANIMATION = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 158
try:
    LV_USE_SHADOW = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 164
try:
    LV_SHADOW_CACHE_SIZE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 168
try:
    LV_USE_OUTLINE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 171
try:
    LV_USE_PATTERN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 174
try:
    LV_USE_VALUE_STR = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 177
try:
    LV_USE_BLEND_MODES = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 180
try:
    LV_USE_OPA_SCALE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 183
try:
    LV_USE_IMG_TRANSFORM = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 186
try:
    LV_USE_GROUP = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 192
try:
    LV_USE_GPU = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 193
try:
    LV_USE_GPU_STM32_DMA2D = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 199
try:
    LV_USE_GPU_NXP_PXP = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 206
try:
    LV_USE_GPU_NXP_PXP_AUTO_INIT = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 209
try:
    LV_USE_GPU_NXP_VG_LITE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 212
try:
    LV_USE_FILESYSTEM = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 219
try:
    LV_USE_USER_DATA = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 222
try:
    LV_USE_PERF_MONITOR = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 225
try:
    LV_USE_API_EXTENSION_V6 = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 226
try:
    LV_USE_API_EXTENSION_V7 = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 233
try:
    LV_IMG_CF_INDEXED = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 236
try:
    LV_IMG_CF_ALPHA = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 244
try:
    LV_IMG_CACHE_DEF_SIZE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 254
try:
    LV_BIG_ENDIAN_SYSTEM = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 301
try:
    LV_TICK_CUSTOM = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 315
try:
    LV_USE_LOG = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 344
try:
    LV_USE_DEBUG = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 348
try:
    LV_USE_ASSERT_NULL = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 351
try:
    LV_USE_ASSERT_MEM = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 354
try:
    LV_USE_ASSERT_MEM_INTEGRITY = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 359
try:
    LV_USE_ASSERT_STR = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 363
try:
    LV_USE_ASSERT_OBJ = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 366
try:
    LV_USE_ASSERT_STYLE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 382
try:
    LV_FONT_MONTSERRAT_8 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 383
try:
    LV_FONT_MONTSERRAT_10 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 384
try:
    LV_FONT_MONTSERRAT_12 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 385
try:
    LV_FONT_MONTSERRAT_14 = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 386
try:
    LV_FONT_MONTSERRAT_16 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 387
try:
    LV_FONT_MONTSERRAT_18 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 388
try:
    LV_FONT_MONTSERRAT_20 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 389
try:
    LV_FONT_MONTSERRAT_22 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 390
try:
    LV_FONT_MONTSERRAT_24 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 391
try:
    LV_FONT_MONTSERRAT_26 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 392
try:
    LV_FONT_MONTSERRAT_28 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 393
try:
    LV_FONT_MONTSERRAT_30 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 394
try:
    LV_FONT_MONTSERRAT_32 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 395
try:
    LV_FONT_MONTSERRAT_34 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 396
try:
    LV_FONT_MONTSERRAT_36 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 397
try:
    LV_FONT_MONTSERRAT_38 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 398
try:
    LV_FONT_MONTSERRAT_40 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 399
try:
    LV_FONT_MONTSERRAT_42 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 400
try:
    LV_FONT_MONTSERRAT_44 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 401
try:
    LV_FONT_MONTSERRAT_46 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 402
try:
    LV_FONT_MONTSERRAT_48 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 405
try:
    LV_FONT_MONTSERRAT_12_SUBPX = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 406
try:
    LV_FONT_MONTSERRAT_28_COMPRESSED = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 407
try:
    LV_FONT_DEJAVU_16_PERSIAN_HEBREW = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 408
try:
    LV_FONT_SIMSUN_16_CJK = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 412
try:
    LV_FONT_UNSCII_8 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 413
try:
    LV_FONT_UNSCII_16 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 426
try:
    LV_FONT_FMT_TXT_LARGE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 431
try:
    LV_USE_FONT_COMPRESSED = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 434
try:
    LV_USE_FONT_SUBPX = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 440
try:
    LV_FONT_SUBPX_BGR = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 454
try:
    LV_USE_THEME_EMPTY = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 458
try:
    LV_USE_THEME_TEMPLATE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 467
try:
    LV_USE_THEME_MATERIAL = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 474
try:
    LV_USE_THEME_MONO = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 477
try:
    LV_THEME_DEFAULT_INIT = lv_theme_material_init
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 480
try:
    LV_THEME_DEFAULT_FLAG = LV_THEME_MATERIAL_FLAG_LIGHT
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 481
try:
    LV_THEME_DEFAULT_FONT_SMALL = pointer(lv_font_montserrat_14)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 482
try:
    LV_THEME_DEFAULT_FONT_NORMAL = pointer(lv_font_montserrat_14)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 483
try:
    LV_THEME_DEFAULT_FONT_SUBTITLE = pointer(lv_font_montserrat_14)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 484
try:
    LV_THEME_DEFAULT_FONT_TITLE = pointer(lv_font_montserrat_14)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 495
try:
    LV_TXT_ENC = LV_TXT_ENC_UTF8
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 498
try:
    LV_TXT_BREAK_CHARS = ' ,.;:-_'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 502
try:
    LV_TXT_LINE_BREAK_LONG_LEN = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 506
try:
    LV_TXT_LINE_BREAK_LONG_PRE_MIN_LEN = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 510
try:
    LV_TXT_LINE_BREAK_LONG_POST_MIN_LEN = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 513
try:
    LV_TXT_COLOR_CMD = '#'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 519
try:
    LV_USE_BIDI = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 531
try:
    LV_USE_ARABIC_PERSIAN_CHARS = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 534
try:
    LV_SPRINTF_CUSTOM = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 540
try:
    LV_SPRINTF_DISABLE_FLOAT = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 560
try:
    LV_USE_OBJ_REALIGN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 567
try:
    LV_USE_EXT_CLICK_AREA = LV_EXT_CLICK_AREA_TINY
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 577
try:
    LV_USE_ARC = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 580
try:
    LV_USE_BAR = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 583
try:
    LV_USE_BTN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 586
try:
    LV_USE_BTNMATRIX = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 589
try:
    LV_USE_CALENDAR = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 591
try:
    LV_CALENDAR_WEEK_STARTS_MONDAY = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 595
try:
    LV_USE_CANVAS = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 598
try:
    LV_USE_CHECKBOX = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 601
try:
    LV_USE_CHART = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 603
try:
    LV_CHART_AXIS_TICK_LABEL_MAX_LEN = 256
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 607
try:
    LV_USE_CONT = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 610
try:
    LV_USE_CPICKER = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 613
try:
    LV_USE_DROPDOWN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 616
try:
    LV_DROPDOWN_DEF_ANIM_TIME = 200
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 620
try:
    LV_USE_GAUGE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 623
try:
    LV_USE_IMG = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 626
try:
    LV_USE_IMGBTN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 629
try:
    LV_IMGBTN_TILED = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 633
try:
    LV_USE_KEYBOARD = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 636
try:
    LV_USE_LABEL = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 639
try:
    LV_LABEL_DEF_SCROLL_SPEED = 25
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 642
try:
    LV_LABEL_WAIT_CHAR_COUNT = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 645
try:
    LV_LABEL_TEXT_SEL = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 648
try:
    LV_LABEL_LONG_TXT_HINT = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 652
try:
    LV_USE_LED = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 654
try:
    LV_LED_BRIGHT_MIN = 120
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 655
try:
    LV_LED_BRIGHT_MAX = 255
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 659
try:
    LV_USE_LINE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 662
try:
    LV_USE_LIST = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 665
try:
    LV_LIST_DEF_ANIM_TIME = 100
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 669
try:
    LV_USE_LINEMETER = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 677
try:
    LV_LINEMETER_PRECISE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 681
try:
    LV_USE_OBJMASK = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 684
try:
    LV_USE_MSGBOX = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 687
try:
    LV_USE_PAGE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 690
try:
    LV_PAGE_DEF_ANIM_TIME = 400
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 694
try:
    LV_USE_SPINNER = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 696
try:
    LV_SPINNER_DEF_ARC_LENGTH = 60
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 697
try:
    LV_SPINNER_DEF_SPIN_TIME = 1000
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 698
try:
    LV_SPINNER_DEF_ANIM = LV_SPINNER_TYPE_SPINNING_ARC
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 702
try:
    LV_USE_ROLLER = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 705
try:
    LV_ROLLER_DEF_ANIM_TIME = 200
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 708
try:
    LV_ROLLER_INF_PAGES = 7
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 712
try:
    LV_USE_SLIDER = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 715
try:
    LV_USE_SPINBOX = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 718
try:
    LV_USE_SWITCH = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 721
try:
    LV_USE_TEXTAREA = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 723
try:
    LV_TEXTAREA_DEF_CURSOR_BLINK_TIME = 400
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 724
try:
    LV_TEXTAREA_DEF_PWD_SHOW_TIME = 1500
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 728
try:
    LV_USE_TABLE = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 730
try:
    LV_TABLE_COL_MAX = 12
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 731
try:
    LV_TABLE_CELL_STYLE_CNT = 4
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 736
try:
    LV_USE_TABVIEW = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 739
try:
    LV_TABVIEW_DEF_ANIM_TIME = 300
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 743
try:
    LV_USE_TILEVIEW = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 746
try:
    LV_TILEVIEW_DEF_ANIM_TIME = 300
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/../../../lv_conf.h: 750
try:
    LV_USE_WIN = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 25
try:
    LV_LOG_LEVEL_TRACE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 26
try:
    LV_LOG_LEVEL_INFO = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 27
try:
    LV_LOG_LEVEL_WARN = 2
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 28
try:
    LV_LOG_LEVEL_ERROR = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 29
try:
    LV_LOG_LEVEL_USER = 4
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 30
try:
    LV_LOG_LEVEL_NONE = 5
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 31
try:
    _LV_LOG_LEVEL_NUM = 6
except:
    pass

bool = c_bool# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stdbool.h: 33

# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stdbool.h: 34
try:
    true = 1
except:
    pass

# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stdbool.h: 35
try:
    false = 0
except:
    pass

# /usr/lib/gcc/x86_64-pc-linux-gnu/10.2.0/include/stdbool.h: 52
try:
    __bool_true_false_are_defined = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_types.h: 75
def LV_UNUSED(x):
    return (None (ord_if_char(x))).value

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_mem.h: 32
try:
    LV_MEM_BUF_MAX_NUM = 16
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 31
try:
    LV_NO_TASK_READY = 4294967295
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 22
def LV_MATH_MIN(a, b):
    return (a < b) and a or b

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 23
def LV_MATH_MIN3(a, b, c):
    return (LV_MATH_MIN ((LV_MATH_MIN (a, b)), c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 24
def LV_MATH_MIN4(a, b, c, d):
    return (LV_MATH_MIN ((LV_MATH_MIN (a, b)), (LV_MATH_MIN (c, d))))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 26
def LV_MATH_MAX(a, b):
    return (a > b) and a or b

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 27
def LV_MATH_MAX3(a, b, c):
    return (LV_MATH_MAX ((LV_MATH_MAX (a, b)), c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 28
def LV_MATH_MAX4(a, b, c, d):
    return (LV_MATH_MAX ((LV_MATH_MAX (a, b)), (LV_MATH_MAX (c, d))))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 30
def LV_MATH_ABS(x):
    return (x > 0) and x or (-x)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 32
def LV_MATH_UDIV255(x):
    return ((c_uint32 (ord_if_char(((c_uint32 (ord_if_char(x))).value * 32897)))).value >> 23)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 35
def LV_UMAX_OF(t):
    return (((1 << ((sizeof(t) * 8) - 1)) - 1) | (15 << ((sizeof(t) * 8) - 4)))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 36
def LV_SMAX_OF(t):
    return (((1 << ((sizeof(t) * 8) - 1)) - 1) | (7 << ((sizeof(t) * 8) - 4)))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 39
try:
    LV_TRIGO_SIN_MAX = 32767
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 40
try:
    LV_TRIGO_SHIFT = 15
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 42
try:
    LV_BEZIER_VAL_MAX = 1024
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_math.h: 43
try:
    LV_BEZIER_VAL_SHIFT = 10
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 75
try:
    LV_OPA_MIN = 2
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 76
try:
    LV_OPA_MAX = 253
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 85
try:
    LV_COLOR_SIZE = 32
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 100
try:
    LV_COLOR_MIX_ROUND_OFS = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 115
def LV_COLOR_GET_R1(c):
    return ((c.ch).red)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 116
def LV_COLOR_GET_G1(c):
    return ((c.ch).green)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 117
def LV_COLOR_GET_B1(c):
    return ((c.ch).blue)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 118
def LV_COLOR_GET_A1(c):
    return 255

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 125
def LV_COLOR_GET_R8(c):
    return ((c.ch).red)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 126
def LV_COLOR_GET_G8(c):
    return ((c.ch).green)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 127
def LV_COLOR_GET_B8(c):
    return ((c.ch).blue)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 128
def LV_COLOR_GET_A8(c):
    return 255

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 139
def LV_COLOR_GET_R16(c):
    return ((c.ch).red)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 141
def LV_COLOR_GET_G16(c):
    return ((c.ch).green)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 145
def LV_COLOR_GET_B16(c):
    return ((c.ch).blue)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 146
def LV_COLOR_GET_A16(c):
    return 255

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 153
def LV_COLOR_GET_R32(c):
    return ((c.ch).red)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 154
def LV_COLOR_GET_G32(c):
    return ((c.ch).green)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 155
def LV_COLOR_GET_B32(c):
    return ((c.ch).blue)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 156
def LV_COLOR_GET_A32(c):
    return ((c.ch).alpha)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 201
def LV_COLOR_GET_R(c):
    return (LV_COLOR_GET_R32 (c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 202
def LV_COLOR_GET_G(c):
    return (LV_COLOR_GET_G32 (c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 203
def LV_COLOR_GET_B(c):
    return (LV_COLOR_GET_B32 (c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 204
def LV_COLOR_GET_A(c):
    return (LV_COLOR_GET_A32 (c))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_color.h: 608
try:
    _LV_COLOR_HAS_MODERN_CPP = 0
except:
    pass

# /usr/include/string.h: 23
try:
    _STRING_H = 1
except:
    pass

# /usr/include/bits/libc-header-start.h: 37
# #undef __GLIBC_USE_LIB_EXT2
try:
    del __GLIBC_USE_LIB_EXT2
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 42
try:
    __GLIBC_USE_LIB_EXT2 = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 49
# #undef __GLIBC_USE_IEC_60559_BFP_EXT
try:
    del __GLIBC_USE_IEC_60559_BFP_EXT
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 53
try:
    __GLIBC_USE_IEC_60559_BFP_EXT = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 55
# #undef __GLIBC_USE_IEC_60559_BFP_EXT_C2X
try:
    del __GLIBC_USE_IEC_60559_BFP_EXT_C2X
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 59
try:
    __GLIBC_USE_IEC_60559_BFP_EXT_C2X = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 66
# #undef __GLIBC_USE_IEC_60559_FUNCS_EXT
try:
    del __GLIBC_USE_IEC_60559_FUNCS_EXT
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 70
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 72
# #undef __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X
try:
    del __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 76
try:
    __GLIBC_USE_IEC_60559_FUNCS_EXT_C2X = 0
except:
    pass

# /usr/include/bits/libc-header-start.h: 81
# #undef __GLIBC_USE_IEC_60559_TYPES_EXT
try:
    del __GLIBC_USE_IEC_60559_TYPES_EXT
except NameError:
    pass

# /usr/include/bits/libc-header-start.h: 85
try:
    __GLIBC_USE_IEC_60559_TYPES_EXT = 0
except:
    pass

# /usr/include/bits/types/locale_t.h: 20
try:
    _BITS_TYPES_LOCALE_T_H = 1
except:
    pass

# /usr/include/bits/types/__locale_t.h: 21
try:
    _BITS_TYPES___LOCALE_T_H = 1
except:
    pass

# /usr/include/string.h: 423
try:
    strerror_r = __xpg_strerror_r
except:
    pass

# /usr/include/strings.h: 19
try:
    _STRINGS_H = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 26
try:
    LV_COORD_MAX = (lv_coord_t (ord_if_char(((c_uint32 (ord_if_char(((c_uint32 (ord_if_char(1))).value << ((8 * sizeof(lv_coord_t)) - 1))))).value - 1000)))).value
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/../lv_misc/lv_area.h: 27
try:
    LV_COORD_MIN = (-LV_COORD_MAX)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 30
try:
    LV_INV_BUF_SIZE = 32
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 24
try:
    LV_SYMBOL_AUDIO = '\\xef\\x80\\x81'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 25
try:
    LV_SYMBOL_VIDEO = '\\xef\\x80\\x88'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 26
try:
    LV_SYMBOL_LIST = '\\xef\\x80\\x8b'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 27
try:
    LV_SYMBOL_OK = '\\xef\\x80\\x8c'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 28
try:
    LV_SYMBOL_CLOSE = '\\xef\\x80\\x8d'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 29
try:
    LV_SYMBOL_POWER = '\\xef\\x80\\x91'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 30
try:
    LV_SYMBOL_SETTINGS = '\\xef\\x80\\x93'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 31
try:
    LV_SYMBOL_HOME = '\\xef\\x80\\x95'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 32
try:
    LV_SYMBOL_DOWNLOAD = '\\xef\\x80\\x99'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 33
try:
    LV_SYMBOL_DRIVE = '\\xef\\x80\\x9c'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 34
try:
    LV_SYMBOL_REFRESH = '\\xef\\x80\\xa1'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 35
try:
    LV_SYMBOL_MUTE = '\\xef\\x80\\xa6'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 36
try:
    LV_SYMBOL_VOLUME_MID = '\\xef\\x80\\xa7'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 37
try:
    LV_SYMBOL_VOLUME_MAX = '\\xef\\x80\\xa8'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 38
try:
    LV_SYMBOL_IMAGE = '\\xef\\x80\\xbe'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 39
try:
    LV_SYMBOL_EDIT = '\\xef\\x8C\\x84'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 40
try:
    LV_SYMBOL_PREV = '\\xef\\x81\\x88'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 41
try:
    LV_SYMBOL_PLAY = '\\xef\\x81\\x8b'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 42
try:
    LV_SYMBOL_PAUSE = '\\xef\\x81\\x8c'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 43
try:
    LV_SYMBOL_STOP = '\\xef\\x81\\x8d'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 44
try:
    LV_SYMBOL_NEXT = '\\xef\\x81\\x91'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 45
try:
    LV_SYMBOL_EJECT = '\\xef\\x81\\x92'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 46
try:
    LV_SYMBOL_LEFT = '\\xef\\x81\\x93'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 47
try:
    LV_SYMBOL_RIGHT = '\\xef\\x81\\x94'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 48
try:
    LV_SYMBOL_PLUS = '\\xef\\x81\\xa7'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 49
try:
    LV_SYMBOL_MINUS = '\\xef\\x81\\xa8'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 50
try:
    LV_SYMBOL_EYE_OPEN = '\\xef\\x81\\xae'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 51
try:
    LV_SYMBOL_EYE_CLOSE = '\\xef\\x81\\xb0'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 52
try:
    LV_SYMBOL_WARNING = '\\xef\\x81\\xb1'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 53
try:
    LV_SYMBOL_SHUFFLE = '\\xef\\x81\\xb4'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 54
try:
    LV_SYMBOL_UP = '\\xef\\x81\\xb7'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 55
try:
    LV_SYMBOL_DOWN = '\\xef\\x81\\xb8'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 56
try:
    LV_SYMBOL_LOOP = '\\xef\\x81\\xb9'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 57
try:
    LV_SYMBOL_DIRECTORY = '\\xef\\x81\\xbb'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 58
try:
    LV_SYMBOL_UPLOAD = '\\xef\\x82\\x93'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 59
try:
    LV_SYMBOL_CALL = '\\xef\\x82\\x95'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 60
try:
    LV_SYMBOL_CUT = '\\xef\\x83\\x84'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 61
try:
    LV_SYMBOL_COPY = '\\xef\\x83\\x85'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 62
try:
    LV_SYMBOL_SAVE = '\\xef\\x83\\x87'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 63
try:
    LV_SYMBOL_CHARGE = '\\xef\\x83\\xa7'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 64
try:
    LV_SYMBOL_PASTE = '\\xef\\x83\\xAA'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 65
try:
    LV_SYMBOL_BELL = '\\xef\\x83\\xb3'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 66
try:
    LV_SYMBOL_KEYBOARD = '\\xef\\x84\\x9c'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 67
try:
    LV_SYMBOL_GPS = '\\xef\\x84\\xa4'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 68
try:
    LV_SYMBOL_FILE = '\\xef\\x85\\x9b'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 69
try:
    LV_SYMBOL_WIFI = '\\xef\\x87\\xab'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 70
try:
    LV_SYMBOL_BATTERY_FULL = '\\xef\\x89\\x80'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 71
try:
    LV_SYMBOL_BATTERY_3 = '\\xef\\x89\\x81'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 72
try:
    LV_SYMBOL_BATTERY_2 = '\\xef\\x89\\x82'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 73
try:
    LV_SYMBOL_BATTERY_1 = '\\xef\\x89\\x83'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 74
try:
    LV_SYMBOL_BATTERY_EMPTY = '\\xef\\x89\\x84'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 75
try:
    LV_SYMBOL_USB = '\\xef\\x8a\\x87'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 76
try:
    LV_SYMBOL_BLUETOOTH = '\\xef\\x8a\\x93'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 77
try:
    LV_SYMBOL_TRASH = '\\xef\\x8B\\xAD'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 78
try:
    LV_SYMBOL_BACKSPACE = '\\xef\\x95\\x9A'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 79
try:
    LV_SYMBOL_SD_CARD = '\\xef\\x9F\\x82'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 80
try:
    LV_SYMBOL_NEW_LINE = '\\xef\\xA2\\xA2'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 83
try:
    LV_SYMBOL_DUMMY = '\\xEF\\xA3\\xBF'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_symbol_def.h: 88
try:
    LV_SYMBOL_BULLET = '\\xE2\\x80\\xA2'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 44
try:
    LV_ANIM_REPEAT_INFINITE = 65535
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 60
def LV_DEBUG_IS_NULL(p):
    return (lv_debug_check_null (p))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 64
try:
    LV_DEBUG_CHECK_MEM_INTEGRITY = (lv_debug_check_mem_integrity ())
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_debug.h: 68
def LV_DEBUG_IS_STR(str):
    return ((lv_debug_check_null (str)) and (lv_debug_check_str (str)))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 23
try:
    LV_MASK_ID_INV = (-1)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 24
try:
    _LV_MASK_MAX_NUM = 16
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 29
try:
    LV_RADIUS_CIRCLE = 32767
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 32
try:
    LV_DEBUG_STYLE_SENTINEL_VALUE = 579381998
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 33
try:
    LV_DEBUG_STYLE_LIST_SENTINEL_VALUE = 2574765243
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 37
try:
    LV_STYLE_ID_MASK = 255
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 39
try:
    LV_STYLE_ATTR_NONE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 40
try:
    LV_STYLE_ATTR_INHERIT = (1 << 7)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 42
try:
    _LV_STYLE_CLOSING_PROP = 255
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 44
try:
    LV_STYLE_TRANS_NUM_MAX = 6
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 46
try:
    LV_STYLE_PROP_ALL = 255
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 86
def LV_STYLE_ATTR_GET_INHERIT(f):
    return (f & 128)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 87
def LV_STYLE_ATTR_GET_STATE(f):
    return (f & 127)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 89
try:
    LV_STYLE_ID_VALUE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 90
try:
    LV_STYLE_ID_COLOR = 9
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 91
try:
    LV_STYLE_ID_OPA = 12
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 92
try:
    LV_STYLE_ID_PTR = 14
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 205
try:
    LV_STYLE_STATE_POS = 8
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 206
try:
    LV_STYLE_STATE_MASK = 32512
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 207
try:
    LV_STYLE_INHERIT_MASK = 32768
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 604
def LV_DEBUG_IS_STYLE(style_p):
    return (lv_debug_check_style (style_p))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_style.h: 608
def LV_DEBUG_IS_STYLE_LIST(list_p):
    return (lv_debug_check_style_list (list_p))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 26
try:
    LV_BIDI_LRO = '\\xE2\\x80\\xAD'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_bidi.h: 27
try:
    LV_BIDI_RLO = '\\xE2\\x80\\xAE'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 32
try:
    LV_TXT_ENC_UTF8 = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_txt.h: 33
try:
    LV_TXT_ENC_ASCII = 2
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_label.h: 23
try:
    LV_DRAW_LABEL_NO_TXT_SEL = 65535
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 29
try:
    LV_IMG_PX_SIZE_ALPHA_BYTE = 4
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 32
def LV_IMG_BUF_SIZE_TRUE_COLOR(w, h):
    return (((LV_COLOR_SIZE / 8) * w) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 33
def LV_IMG_BUF_SIZE_TRUE_COLOR_CHROMA_KEYED(w, h):
    return (((LV_COLOR_SIZE / 8) * w) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 34
def LV_IMG_BUF_SIZE_TRUE_COLOR_ALPHA(w, h):
    return ((LV_IMG_PX_SIZE_ALPHA_BYTE * w) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 37
def LV_IMG_BUF_SIZE_ALPHA_1BIT(w, h):
    return (((w / 8) + 1) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 38
def LV_IMG_BUF_SIZE_ALPHA_2BIT(w, h):
    return (((w / 4) + 1) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 39
def LV_IMG_BUF_SIZE_ALPHA_4BIT(w, h):
    return (((w / 2) + 1) * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 40
def LV_IMG_BUF_SIZE_ALPHA_8BIT(w, h):
    return (w * h)

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 43
def LV_IMG_BUF_SIZE_INDEXED_1BIT(w, h):
    return ((LV_IMG_BUF_SIZE_ALPHA_1BIT (w, h)) + (4 * 2))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 44
def LV_IMG_BUF_SIZE_INDEXED_2BIT(w, h):
    return ((LV_IMG_BUF_SIZE_ALPHA_2BIT (w, h)) + (4 * 4))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 45
def LV_IMG_BUF_SIZE_INDEXED_4BIT(w, h):
    return ((LV_IMG_BUF_SIZE_ALPHA_4BIT (w, h)) + (4 * 16))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 46
def LV_IMG_BUF_SIZE_INDEXED_8BIT(w, h):
    return ((LV_IMG_BUF_SIZE_ALPHA_8BIT (w, h)) + (4 * 256))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 48
try:
    LV_IMG_ZOOM_NONE = 256
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 50
try:
    _LV_TRANSFORM_TRIGO_SHIFT = 10
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_buf.h: 51
try:
    _LV_ZOOM_INV_UPSCALE = 5
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 27
try:
    LV_FS_MAX_FN_LENGTH = 64
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 28
try:
    LV_FS_MAX_PATH_LENGTH = 256
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 44
try:
    LV_MAX_ANCESTOR_NUM = 8
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 46
try:
    LV_EXT_CLICK_AREA_OFF = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 47
try:
    LV_EXT_CLICK_AREA_TINY = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 48
try:
    LV_EXT_CLICK_AREA_FULL = 2
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 50
try:
    _LV_OBJ_PART_VIRTUAL_FIRST = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 51
try:
    _LV_OBJ_PART_REAL_FIRST = 64
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 1503
def LV_DEBUG_IS_OBJ(obj_p, obj_type):
    return (((lv_debug_check_null (obj_p)) and (lv_debug_check_obj_valid (obj_p))) and (lv_debug_check_obj_type (obj_p, obj_type)))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_refr.h: 23
try:
    LV_REFR_TASK_PRIO = LV_TASK_PRIO_MID
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 199
try:
    LV_HOR_RES = (lv_disp_get_hor_res ((lv_disp_get_default ())))
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_disp.h: 206
try:
    LV_VER_RES = (lv_disp_get_ver_res ((lv_disp_get_default ())))
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 30
try:
    LV_LABEL_DOT_NUM = 3
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 31
try:
    LV_LABEL_POS_LAST = 65535
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_label.h: 32
try:
    LV_LABEL_TEXT_SEL_OFF = LV_DRAW_LABEL_NO_TXT_SEL
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_line.h: 86
try:
    lv_line_set_y_inv = lv_line_set_y_invert
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 28
try:
    LV_CHART_POINT_DEF = LV_COORD_MIN
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_chart.h: 31
try:
    LV_CHART_TICK_LENGTH_AUTO = 255
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 31
try:
    LV_BAR_ANIM_STATE_START = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 34
try:
    LV_BAR_ANIM_STATE_END = 256
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 37
try:
    LV_BAR_ANIM_STATE_INV = (-1)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_bar.h: 40
try:
    LV_BAR_ANIM_STATE_NORM = 8
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 27
try:
    LV_BTNMATRIX_WIDTH_MASK = 7
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_btnmatrix.h: 28
try:
    LV_BTNMATRIX_BTN_NONE = 65535
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_keyboard.h: 35
try:
    LV_KEYBOARD_CTRL_BTN_FLAGS = (LV_BTNMATRIX_CTRL_NO_REPEAT | LV_BTNMATRIX_CTRL_CLICK_TRIG)
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_dropdown.h: 35
try:
    LV_DROPDOWN_POS_LAST = 65535
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_textarea.h: 36
try:
    LV_TEXTAREA_CURSOR_LAST = 32767
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 248
def LV_CANVAS_BUF_SIZE_TRUE_COLOR(w, h):
    return (LV_IMG_BUF_SIZE_TRUE_COLOR (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 249
def LV_CANVAS_BUF_SIZE_TRUE_COLOR_CHROMA_KEYED(w, h):
    return (LV_IMG_BUF_SIZE_TRUE_COLOR_CHROMA_KEYED (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 250
def LV_CANVAS_BUF_SIZE_TRUE_COLOR_ALPHA(w, h):
    return (LV_IMG_BUF_SIZE_TRUE_COLOR_ALPHA (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 253
def LV_CANVAS_BUF_SIZE_ALPHA_1BIT(w, h):
    return (LV_IMG_BUF_SIZE_ALPHA_1BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 254
def LV_CANVAS_BUF_SIZE_ALPHA_2BIT(w, h):
    return (LV_IMG_BUF_SIZE_ALPHA_2BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 255
def LV_CANVAS_BUF_SIZE_ALPHA_4BIT(w, h):
    return (LV_IMG_BUF_SIZE_ALPHA_4BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 256
def LV_CANVAS_BUF_SIZE_ALPHA_8BIT(w, h):
    return (LV_IMG_BUF_SIZE_ALPHA_8BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 259
def LV_CANVAS_BUF_SIZE_INDEXED_1BIT(w, h):
    return (LV_IMG_BUF_SIZE_INDEXED_1BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 260
def LV_CANVAS_BUF_SIZE_INDEXED_2BIT(w, h):
    return (LV_IMG_BUF_SIZE_INDEXED_2BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 261
def LV_CANVAS_BUF_SIZE_INDEXED_4BIT(w, h):
    return (LV_IMG_BUF_SIZE_INDEXED_4BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_canvas.h: 262
def LV_CANVAS_BUF_SIZE_INDEXED_8BIT(w, h):
    return (LV_IMG_BUF_SIZE_INDEXED_8BIT (w, h))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_widgets/lv_spinbox.h: 31
try:
    LV_SPINBOX_MAX_DIGIT_COUNT = 10
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 42
try:
    lv_checkbox_set_static_text = lv_checkbox_set_text_static
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 48
try:
    lv_chart_get_point_cnt = lv_chart_get_point_count
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 66
try:
    lv_dropdown_set_static_options = lv_dropdown_set_options_static
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 102
try:
    lv_label_set_static_text = lv_label_set_text_static
except:
    pass

lv_scrlbar_mode_t = lv_scrollbar_mode_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 150

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 152
try:
    LV_SCRLBAR_MODE_OFF = LV_SCROLLBAR_MODE_OFF
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 153
try:
    LV_SCRLBAR_MODE_ON = LV_SCROLLBAR_MODE_ON
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 154
try:
    LV_SCRLBAR_MODE_DRAG = LV_SCROLLBAR_MODE_DRAG
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 155
try:
    LV_SCRLBAR_MODE_AUTO = LV_SCROLLBAR_MODE_AUTO
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 156
try:
    LV_SCRLBAR_MODE_HIDE = LV_SCROLLBAR_MODE_HIDE
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 157
try:
    LV_SCRLBAR_MODE_UNHIDE = LV_SCROLLBAR_MODE_UNHIDE
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_api_map.h: 182
try:
    LV_ROLLER_MODE_INIFINITE = LV_ROLLER_MODE_INFINITE
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/lvgl.h: 122
def LV_VERSION_CHECK(x, y, z):
    return ((x == LVGL_VERSION_MAJOR) and ((y < LVGL_VERSION_MINOR) or ((y == LVGL_VERSION_MINOR) and (z <= LVGL_VERSION_PATCH))))

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 60
try:
    LV_DRV_INDEV_IRQ_READ = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 66
def LV_DRV_INDEV_SPI_XCHG_BYTE(data):
    return 0

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 75
def LV_DRV_INDEV_I2C_READ(last_read):
    return 0

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 86
try:
    USE_MONITOR = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 111
try:
    USE_WINDOWS = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 123
try:
    USE_GTK = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 130
try:
    USE_SSD1963 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 154
try:
    USE_R61581 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 178
try:
    USE_ST7565 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 189
try:
    USE_GC9A01 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 201
try:
    USE_UC1610 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 222
try:
    USE_SHARP_MIP = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 236
try:
    USE_ILI9341 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 250
try:
    USE_FBDEV = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 254
try:
    FBDEV_PATH = '/dev/fb0'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 261
try:
    USE_BSD_FBDEV = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 272
try:
    USE_DRM = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 288
try:
    USE_XPT2046 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 308
try:
    USE_FT5406EE8 = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 319
try:
    USE_AD_TOUCH = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 331
try:
    USE_MOUSE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 342
try:
    USE_MOUSEWHEEL = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 353
try:
    USE_LIBINPUT = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 364
try:
    USE_EVDEV = 1
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 368
try:
    USE_BSD_EVDEV = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 372
try:
    EVDEV_NAME = '/dev/input/event0'
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 373
try:
    EVDEV_SWAP_AXES = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 375
try:
    EVDEV_CALIBRATE = 0
except:
    pass

# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lv_drivers/gtkdrv/../../lv_drv_conf.h: 389
try:
    USE_KEYBOARD = 0
except:
    pass

_silence_gcc_warning = struct__silence_gcc_warning# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_log.h: 33

_lv_task_t = struct__lv_task_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_misc/lv_task.h: 60

__locale_data = struct___locale_data# /usr/include/bits/types/__locale_t.h: 31

__locale_struct = struct___locale_struct# /usr/include/bits/types/__locale_t.h: 28

_disp_t = struct__disp_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 147

_disp_drv_t = struct__disp_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_disp.h: 66

_lv_obj_t = struct__lv_obj_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_obj.h: 195

_lv_indev_t = struct__lv_indev_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 172

_lv_indev_drv_t = struct__lv_indev_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 81

_lv_indev_proc_t = struct__lv_indev_proc_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_hal/lv_hal_indev.h: 165

_lv_group_t = struct__lv_group_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/lv_group.h: 54

_lv_font_struct = struct__lv_font_struct# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_font/lv_font.h: 57

_lv_anim_t = struct__lv_anim_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 75

_lv_anim_path_t = struct__lv_anim_path_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_misc/lv_anim.h: 51

_lv_draw_mask_map_param_t = struct__lv_draw_mask_map_param_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_draw_mask.h: 161

_lv_fs_drv_t = struct__lv_fs_drv_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/../lv_misc/lv_fs.h: 63

_lv_img_decoder = struct__lv_img_decoder# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 87

_lv_img_decoder_dsc = struct__lv_img_decoder_dsc# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_core/../lv_draw/lv_img_decoder.h: 99

_lv_theme_t = struct__lv_theme_t# /home/gwillen/Sync/Programming/Python/lv_python/lib/./lvgl/src/lv_themes/lv_theme.h: 154

# No inserted files

# No prefix-stripping

