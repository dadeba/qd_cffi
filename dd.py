import numpy as np
from _qd import ffi, lib

def write_dd(a):
    x = ffi.cast("const double *", a.v.ctypes.data)
    lib.c_dd_write(x)
    
def cast_dd(a, b, c):
    x = ffi.cast("const double *", a.v.ctypes.data)
    y = ffi.cast("const double *", b.v.ctypes.data)
    z = ffi.cast("double *", c.v.ctypes.data)
    return x, y, z

def dd_add(a, b, c):
    x, y, z = cast_dd(a, b, c)
    lib.c_dd_add(x, y, z)
    
def dd_sub(a, b, c):
    x, y, z = cast_dd(a, b, c)
    lib.c_dd_sub(x, y, z)

def dd_mul(a, b, c):
    x, y, z = cast_dd(a, b, c)
    lib.c_dd_mul(x, y, z)

def dd_div(a, b, c):
    x, y, z = cast_dd(a, b, c)
    lib.c_dd_div(x, y, z)

def dd_rand(a):
    z = ffi.cast("double *", a.v.ctypes.data)
    lib.c_dd_rand(z)

def call_srand():
    lib.call_srand()

def call_binary72_to_dd(a, c):
    x = ffi.cast("const uint64_t [2]", a.ctypes.data)
    z = ffi.cast("double *", c.v.ctypes.data)
    lib.binary72_to_dd(x, z)
    
class DD:
    def __init__(self, v = [0.0, 0.0]):
        self.v = np.array(v, dtype=np.float64)

    def gen(self):
        return DD()

    def __add__(self, y):
        z = DD()
        dd_add(self, y, z)
        return z

    def __sub__(self, y):
        z = DD()
        dd_sub(self, y, z)
        return z

    def __mul__(self, y):
        z = DD()
        dd_mul(self, y, z)
        return z

    def __truediv__(self, y):
        z = DD()
        dd_div(self, y, z)
        return z

    def rand(self):
        dd_rand(self)
        
    def __str__(self):
        return self.v.__str__()
