from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef("""
void c_dd_add(const double *a, const double *b, double *c);
void c_dd_sub(const double *a, const double *b, double *c);
void c_dd_mul(const double *a, const double *b, double *c);
void c_dd_div(const double *a, const double *b, double *c);
void c_dd_sqrt(const double *a, double *b);
void c_dd_sqr(const double *a, double *b);
void c_dd_abs(const double *a, double *b);
void c_dd_npwr(const double *a, int b, double *c);
void c_dd_nroot(const double *a, int b, double *c);
void c_dd_nint(const double *a, double *b);
void c_dd_aint(const double *a, double *b);
void c_dd_floor(const double *a, double *b);
void c_dd_ceil(const double *a, double *b);
void c_dd_exp(const double *a, double *b);
void c_dd_log(const double *a, double *b);
void c_dd_log10(const double *a, double *b);
void c_dd_sin(const double *a, double *b);
void c_dd_cos(const double *a, double *b);
void c_dd_tan(const double *a, double *b);
void c_dd_asin(const double *a, double *b);
void c_dd_acos(const double *a, double *b);
void c_dd_atan(const double *a, double *b);
void c_dd_atan2(const double *a, const double *b, double *c);
void c_dd_sinh(const double *a, double *b);
void c_dd_cosh(const double *a, double *b);
void c_dd_tanh(const double *a, double *b);
void c_dd_asinh(const double *a, double *b);
void c_dd_acosh(const double *a, double *b);
void c_dd_atanh(const double *a, double *b);
void c_dd_sincos(const double *a, double *s, double *c);
void c_dd_sincosh(const double *a, double *s, double *c);
void c_dd_rand(double *a);
void c_dd_write(const double *a);
void call_srand();
void binary72_to_dd(const uint64_t a[], double *res);
""")

ffibuilder.set_source(
    module_name = "_qd",
    source="""
    #include <qd/c_qd.h>
    #include <qd/c_dd.h>
    #include <qd/fpu.h>
    #include "call_srand.h"
    #include "binary72utils.h"
""",
    sources=['call_srand.c', 'binary72utils.cpp'],
    libraries=["qd", "stdc++"],
    include_dirs=[],
    library_dirs=[]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
