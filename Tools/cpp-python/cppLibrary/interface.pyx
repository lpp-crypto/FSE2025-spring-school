#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2025-03-13 12:12:29>

from cppModule cimport *

def do_the_thing(to_print):
    return cpp_do_the_thing(to_print)
