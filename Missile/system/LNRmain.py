import LNmain.definitions as definitions
import tkinter
from builtins import *
from builtins import str, dict, bool, int, property, type, list, bytes, bytearray, tuple, float, complex, slice, \
    memoryview, zip, range, BaseException
from pipes import Template, stepkinds, SOURCE, SINK
from tkinter import *
import time

from isort import io
from plyer import notification
import keyboard
import numpy
import enum
import sys
import re
from tkinter.constants import *
import _tkinter # If this fails your Python may not be configured for Tk
TclError = _tkinter.TclError
from multiprocessing import *
import types
import LNmain.ref as ref


from ast import AST, mod
from io import BufferedRandom, BufferedReader, BufferedWriter, FileIO, TextIOWrapper
from types import CodeType, MappingProxyType, TracebackType #_Cell
from typing import (
    IO,
    AbstractSet,
    Any,
    AsyncIterable,
    AsyncIterator,
    BinaryIO,
    ByteString,
    Callable,
    FrozenSet,
    Generic,
    ItemsView,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    MutableMapping,
    MutableSequence,
    MutableSet,
    NoReturn,
    Protocol,
    Reversible,
    Sequence,
    Set,
    Sized,
    SupportsAbs,
    SupportsBytes,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    SupportsRound,
    Tuple,
    Type,
    TypeVar,
    Union,
    ValuesView,
    overload
)
#from typing_extensions import Literal, SupportsIndex, final
import os
import tempfile
from shlex import quote

wantobjects = 1

TkVersion = float(_tkinter.TK_VERSION)
TclVersion = float(_tkinter.TCL_VERSION)

READABLE = _tkinter.READABLE
WRITABLE = _tkinter.WRITABLE
EXCEPTION = _tkinter.EXCEPTION


_magic_re = re.compile(r'([\\{}])')
_space_re = re.compile(r'([\s])', re.ASCII)
_support_default_root = 1
_default_root = None

out = 0
IO_ERROR = 631

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.
_S = TypeVar("_S")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_TT = TypeVar("_TT", bound="type")
_TBE = TypeVar("_TBE", bound="BaseException")

if '__main__' in sys.modules:
    sys.modules['__mp_main__'] = sys.modules['__main__']

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_KT_co = TypeVar("_KT_co", covariant=True)  # Key type covariant containers.
_VT_co = TypeVar("_VT_co", covariant=True)  # Value type covariant containers.
_S = TypeVar("_S")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")
_T4 = TypeVar("_T4")
_T5 = TypeVar("_T5")
_TT = TypeVar("_TT", bound="type")
_TBE = TypeVar("_TBE", bound="BaseException")



class linear(object):

    def __init__(self, master=None, value=None, name=None):
        """Construct a variable

        MASTER can be given as master widget.
        VALUE is an optional value (defaults to "")
        NAME is an optional Tcl name (defaults to PY_VARnum).

        If NAME matches an existing variable and VALUE is omitted
        then the existing value is retained.
        """
        # check for type of NAME parameter to override weird error message
        # raised from Modules/_tkinter.c:SetVar like:
        # TypeError: setvar() takes exactly 3 arguments (2 given)
        if name is not None and not isinstance(name, str):
            raise TypeError("name must be a string")
        global _varnum
        if not master:
            master = _default_root
        self._root = master._root()
        self._tk = master.tk
        if name:
            self._name = name
        else:
            self._name = 'PY_VAR' + repr(_varnum)
            _varnum += 1
        if value is not None:
            self.initialize(value)
        elif not self._tk.getboolean(self._tk.call("info", "exists", self._name)):
            self.initialize(self._default)

    def __init_subclass__(cls, **kwargs):
        pass

    def __hex__(self):
        pass

    def __dir__(self):
        pass

    def __unicode__(self):
        pass

    def __oct__(self):
        pass

    def __complex__(self):
        raise NotImplementedError

    def __main___(self, *args):
        pass

    def list(self, *args):
        pass

    def createModule(self, spec):
        pass

    def createGUI(self, size_x, size_y, vsys):
        tkinter.create(vsys, vsys, vsys, True)

    def draw(self, method, **kwargs):
        pass

    def erase(self):
        pass

    def clear(self):
        pass

    def close(self, mode):
        pass

    def saveToDisk(self, disk, location):
        pass

    def loadFromDisk(self, disk, location):
        f = open(location, "r")
        print(disk, f.read())
        f.close()

    def wait(self, secs):
        time.sleep(secs)

    def reloadFromDisk(self):
        pass

    def saveAll(self, location):
        pass

    def diskData(self):
        pass

    def calculate(self, operation, x1, x2, x3, x4, x5, x6, x7, x8):
        if operation == 'add':
            out = x1 +x2+x3+x4+x5+x6+x7+x8
            print(out)
        if operation == 'sub':
            out = x1 -x2
            print(out)
        if operation == 'mul':
            out = x1 *x2
            print(out)
        if operation == 'div':
            out = x1 /x2
            print(out)
        if operation == 'exp':
            out = x1 ** x2
            print(out)
        if operation == 'sqrt':
            out = numpy.sqrt(x1)
            print(out)
        if operation == 'pi':
            out = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
            print(out)



    def recordToDisk(self, arm, location):
        pass

    def IOcontrol(self):
        print(io.__all__)

    def keyTrack(self):
        pass

    def sendNotif(title, message, icon, wait):
         notification.notify(
            title=title,
            message=message,
            app_icon=icon,
            timeout=wait,
         )

    def sysInfo(self):
        pass

    def update(self):
        """Enter event loop until all pending events have been processed by Tcl."""
        self.tk.call('update')


    def linearIntersect(self):
        pass

    def linearParralel(self):
        pass

    def linearRelation(self):
        pass

    def asymmetricalMirror(self):
        pass

    def symmetricalMirror(self):
        pass

    def rotate(self):
        pass

    def transform(self):
        pass


    def trace_path(self):
        pass

    def trace_vinfo(self):
        pass


    def array(self):
        pass

    def barrier(self):
        pass

    def bounded_semaphore(self):
        pass

    def condition(self):
        pass

    def event(self):
        pass

    def event_type(self):
        pass

    def joinable_queue(self):
        pass

    def lock(self, object, lid):
        pass

    def manager(self):
        pass

    def pipe(self):
        pass

    def pool(self):
        pass

    def queue(self):
        pass

    def RLock(self):
        pass

    def raw_array(self):
        pass

    def raw_value(self):
        pass

    def semaphore(self):
        pass

    def simple_queue(self):
        pass

    def value(self, var):
        if var == var:
            return var

    def _exception_(self):
        pass

    def allow_connection_pickling(self):
        pass

    def cpu_count(self):
        pass

    def freeze_support(self):
        pass

    def get_all_start_methods(self):
        pass

    def get_context(self):
        pass

    def get_logger(self):
        pass

    def get_start_method(self):
        pass

    def log_to_stderr(self):
        pass

    def set_executable(self):
        pass

    def set_forkserver_preload(self) -> object:
        pass

    def set_start_method(self):
        pass

    def KeyError(self):
        pass

    def __preload__(cls: type[set_forkserver_preload], __message: str, __exceptions: Sequence[BaseException]) -> set_forkserver_preload(self=0):
        pass

    def __network__(self, ntype, version, system, err: bool, errCurrent: str, stat: str):
        info = [ntype, version, system]
        if err == True:
           return stat, errCurrent, info
        else:
            return info, stat
    def listR(self, v1, v2, v3, column):
        lst = 'ArrayData: ' + str([column, v1, v2, v3])
        return lst


    if sys.version_info >= (3, 9):
        from types import GenericAlias

    def _SupportsTrunc(Protocol):
        pass
    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
    #def __subclasses__(self: _TT) -> list[_TT]: ...
    def __instancecheck__(self, instance: Any) -> bool: ...
    def __subclasscheck__(self, subclass: type) -> bool: ...
    def __pow__(self, __x: int, __modulo: int | None = ...) -> Any: ...  # Return type can be int or float, depending on x.
    def __rpow__(self, x: int, mod: int | None = ...) -> Any: ...
    def __and__(self, n: int) -> int: ...
    def __or__(self, n: int) -> int: ...
    def __xor__(self, n: int) -> int: ...
    def __lshift__(self, n: int) -> int: ...
    def __rshift__(self, n: int) -> int: ...
    def __rand__(self, n: int) -> int: ...
    def __ror__(self, n: int) -> int: ...
    def __rxor__(self, n: int) -> int: ...
    def __rlshift__(self, n: int) -> int: ...
    def __rrshift__(self, n: int) -> int: ...
    def __neg__(self) -> int: ...
    def __pos__(self) -> int: ...
    def __invert__(self) -> int: ...
    def __trunc__(self) -> int: ...
    def __ceil__(self) -> int: ...
    def __floor__(self) -> int: ...
    def __getnewargs__(self) -> tuple[int]: ...
    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __lt__(self, x: int) -> bool: ...
    def __le__(self, x: int) -> bool: ...
    def __gt__(self, x: int) -> bool: ...
    def __ge__(self, x: int) -> bool: ...
    def __str__(self) -> str: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    def __abs__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __index__(self) -> int: ...
    def __eq__(self, x: object) -> bool: ...
    def __ne__(self, x: object) -> bool: ...
    def __str__(self) -> str:...
    def __eq__(self, other):
        return str(self) == str(other)
    definitions.__eq__(self=0, other = 0)

class render(object):
    def point(self, corner=str, lx=int, ly=int, lz=int, lw=int, lv=int):
            pass

    def hover(self, lx=int, ly=int, lz=int, lw=int, lv=int):
            pass

