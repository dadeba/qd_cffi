from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
void c_dd_add(const double *a, const double *b, double *c);
void c_dd_sub(const double *a, const double *b, double *c);
void c_dd_mul(const double *a, const double *b, double *c);
void c_dd_div(const double *a, const double *b, double *c);
void c_dd_rand(double *a);
""")

ffibuilder.set_source("_qd", """
    #include <qd/c_qd.h>
    #include <qd/c_dd.h>
    #include <qd/fpu.h>
""", libraries=["qd"])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
