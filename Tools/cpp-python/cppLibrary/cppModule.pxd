#!/usr/bin/sage
#-*- Python -*-
# Time-stamp: <2025-03-13 12:09:10>


from libcpp.vector cimport vector
from libcpp.string cimport string
from libc.stdint cimport int64_t, uint64_t

cdef extern from "sources.cpp":
    cdef vector[uint64_t] cpp_do_the_thing(const string to_print)
