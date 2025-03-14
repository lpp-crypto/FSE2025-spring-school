from sage.all import *

p = 2**12 - 5
gf = GF(p)

def MiMC(x, K):
    R = 0
    d = 3
    while d**R <= p:
        R += 1
    y = x
    for i in range(0, R):
        y = (y + K + gf(i))**d
    return y

print(MiMC(gf(0), gf(0)),  ' should be 3604')
print(MiMC(gf(1), gf(0)),  ' should be 239')
print(MiMC(gf(0), gf(2)),  ' should be 1198')
