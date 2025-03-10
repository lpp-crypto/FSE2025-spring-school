from sage.crypto.sboxes import sboxes
from sboxU import *

def ddt_by_hand(s):
    # we already know the first row since it corresponds to a zero
    # input diffrerence
    size = len(s)
    result = [[size] + [0 for delta_in in range(1, size)]]
    for delta_in in range(1, size):
        row = [0 for x in range(0, size)] # yes, [0]*size would work,
                                         # but multiplying lists can
                                         # have fun/disastrous side
                                         # effects
        for x in range(0, size):
            delta_out = oplus(s[oplus(x, delta_in)], s[x])
            row[delta_out] += 1
        result.append(row)
    return result

if __name__ == "__main__":
    s = list(sboxes["PRINCE"])
    for row in ddt_by_hand(s):
        print(row)
