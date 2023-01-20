import numpy as np
import dd as dd

dd.call_srand()

a = dd.DD([1.0,0.0])
b = dd.DD([1.0,0.0])
c = a + b
print(a, b, c)

aa = dd.DD()
bb = dd.DD()

aa.rand()
bb.rand()
print(aa, bb)

zz = (aa + bb)*aa + bb/aa
print(zz)

print(zz.v[0])

qq = dd.DD()




xx = np.array([0x40726675d,0x256705d63], dtype=np.uint64)

dd.call_binary72_to_dd(xx, qq)

print(qq)

