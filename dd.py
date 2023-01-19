import numpy as np
from _qd import ffi, lib

def dd_add(a, b, c):
    x = ffi.cast("const double *", a.ctypes.data)
    y = ffi.cast("const double *", b.ctypes.data)
    z = ffi.cast("double *", c.ctypes.data)
    lib.c_dd_add(x, y, z)
    
def dd_sub(a, b, c):
    x = ffi.cast("const double *", a.ctypes.data)
    y = ffi.cast("const double *", b.ctypes.data)
    z = ffi.cast("double *", c.ctypes.data)
    lib.c_dd_sub(x, y, z)

def dd_mul(a, b, c):
    x = ffi.cast("const double *", a.ctypes.data)
    y = ffi.cast("const double *", b.ctypes.data)
    z = ffi.cast("double *", c.ctypes.data)
    lib.c_dd_mul(x, y, z)

def dd_div(a, b, c):
    x = ffi.cast("const double *", a.ctypes.data)
    y = ffi.cast("const double *", b.ctypes.data)
    z = ffi.cast("double *", c.ctypes.data)
    lib.c_dd_div(x, y, z)

def dd_rand(a):
    z = ffi.cast("double *", a.ctypes.data)
    lib.c_dd_rand(z)

def call_srand():
    lib.call_srand()

class DD:
    def __init__(self, v = [0.0, 0.0]):
        self.v = np.array(v, dtype=np.float64)
        
    def __add__(self, y):
        z = DD()
        dd_add(self.v, y.v, z.v)
        return z

    def __sub__(self, y):
        z = DD()
        dd_sub(self.v, y.v, z.v)
        return z

    def __mul__(self, y):
        z = DD()
        dd_mul(self.v, y.v, z.v)
        return z

    def __truediv__(self, y):
        z = DD()
        dd_div(self.v, y.v, z.v)
        return z

    def rand(self):
        dd_rand(self.v)

    def __str__(self):
        return self.v.__str__()
