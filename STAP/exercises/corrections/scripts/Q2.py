from sage.all import *

p = 2**12 - 5
gf = GF(p)
X = gf.polynomial_ring("X").gen()


def MiMC(x, K):
    R = 0
    d = 2
    while gcd(d, p-1) > 1:
        d += 1
    while d**R <= p:
        R += 1
    y = x
    for i in range(0, R):
        y = (y + K + gf(i))**d
    return y

print(MiMC(X, gf(0)))
