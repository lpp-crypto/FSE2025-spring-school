from sage.crypto.sboxes import sboxes

for k in sorted(sboxes.keys()):
    if "SERPENT" in k:
        print(k, list(sboxes[k]))
