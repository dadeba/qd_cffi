#include <qd/qd_real.h>
#include <qd/dd_real.h>

union binary64 
{
  double v;
  unsigned long long i;
};

#define MASK(x) ((0x1ULL<<(x))-0x1ULL)

static inline uint64_t accessn(uint64_t x, uint64_t hi, uint64_t lo)
{
  uint64_t size, res;
  size = hi - lo + 1;
  res = (x>>lo) & MASK(size);
  return res;
}

static inline uint64_t access1(uint64_t x, uint64_t o)
{
  uint64_t res;
  res = (x>>o) & 0x1ULL;
  return res;
}

qd_real conv_binary72_qd(const uint64_t a[2])
{
  uint64_t sign, exp, man;
  int e;
  qd_real q1, q2, q;

  if (a[0] == 0x0 && a[1] == 0x0) return (qd_real)0.0;
  
  sign = access1(a[0], 35);
  exp  = accessn(a[0], 34, 24);

  man  = accessn(a[0], 23, 0);
  man  = (0x1ULL<<24)|man;
  q1 = man*pow(2.0,(double)36.0);
  q2 = a[1];

  q = q1 + q2;

  e = exp-1023LL;
  q = q*pow(2.0, (double)e);

  q = q*pow(2.0, (double)-60.0);

  if (sign == 0x1ULL) q = -q;

  return q;
}

extern "C" {
  void binary72_to_dd(const uint64_t a[2], double *res)
  {
    qd_real q = conv_binary72_qd(a);
    res[0] = q.x[0];
    res[1] = q.x[1];
    //  res[2] = q.x[2];
    //  res[3] = q.x[2];
  }
}
