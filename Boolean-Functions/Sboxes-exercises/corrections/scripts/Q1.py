from sage.crypto.sboxes import sboxes

s = sboxes["PRESENT"]
print(len(s))
print(len(list(s)))
