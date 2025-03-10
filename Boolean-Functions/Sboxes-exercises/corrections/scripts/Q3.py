from sage.crypto.sboxes import sboxes
from sboxU import *

from collections import defaultdict

s = list(sboxes["AES"])
diff_spec = differential_spectrum(s)

# All coefficients occur a number of times that is a multiple of 255
for k in diff_spec.keys():
    print(k, diff_spec[k] % 255)

d = ddt(s)
for delta_in in range(1, 256):
    row_count = defaultdict(int)
    for delta_out in range(0, 256):
        row_count[d[delta_in][delta_out]] += 1
    print("{:02x} : {}".format(
        delta_in,
        pretty_spectrum(row_count)
    ))
