from sboxU import *
from sage.crypto.sboxes import sboxes

sigma = list(sboxes["PRINCE"])

def L(x):
    result = 0
    tmp = 0
    for x_i in x:
        tmp = oplus(tmp, x_i)
    return [oplus(tmp, x[i]) for i in range(0, 4)]


def split_in_nibbles(y):
    result = []
    for i in range(0, 4):
        result.append(y & 0xf)
        y = y >> 4
    return result

def concatenate_nibbles(x):
    return sum((x[i] << (4*i)) for i in range(0, 4))


def test_nibble_manipulations():
    for t in range(0, 10):
        x = randint(0, 2**16-1)
        x_vec = split_in_nibbles(x)
        print(x, concatenate_nibbles(x_vec), x_vec)


def mini_spn(big_x):
    x = split_in_nibbles(big_x)
    # S-layer
    for i in range(0, len(x)):
        x[i] = sigma[x[i]]
    # L-layer
    x = L(x)
    # S-layer
    for i in range(0, len(x)):
        x[i] = sigma[x[i]]
    return concatenate_nibbles(x)


if __name__ == "__main__":
    big_sbox = [0 for x in range(0, 2**16)]
    for x in range(0, 2**16):
        big_sbox[x] = mini_spn(x)
    print(pretty_spectrum(differential_spectrum(big_sbox)))
