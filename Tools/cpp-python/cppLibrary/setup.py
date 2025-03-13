from setuptools import setup
from distutils.core import Extension
from Cython.Build import cythonize
import os
from sys import platform

if platform == 'darwin':	#macOs
    os.environ["CC"] = "clang"
    os.environ["CXX"] = "clang"
else:
    os.environ["CC"] = "g++"
    os.environ["CXX"] = "g++"
    extra_compile_args = ["-O3", "-march=native", "-std=c++17", "-pthread", "-Wno-narrowing"] #narrowing warnings in fp_lat when calling shape_t{p}
    extra_link_args=[]




module_doTheThing = Extension("cppModule", # <-- must match pxd file name!
                          sources=["interface.pyx"], # <-- must match pyx file name!
                          libraries=[],
                          include_dirs=['.'], 
                          language='c++',
                          extra_link_args=extra_link_args,
                          extra_compile_args=extra_compile_args)

setup(name='cppModule', # <-- must match pxd file name!
      ext_modules=cythonize([module_doTheThing], language_level = "3"))
