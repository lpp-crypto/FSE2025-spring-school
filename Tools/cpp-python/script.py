#!/usr/bin/sage
# -*- python-mode -*-


from sage.all import *

from sys import argv
import os

from cppLibrary import do_the_thing




# !SECTION! Main program 

if __name__ == "__main__":
    if len(argv) < 1:
        print("needs at least one argument")
    else:
        numbers = do_the_thing(argv[1].encode("ascii"))
        print(numbers)
