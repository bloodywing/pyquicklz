# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from cffi import FFI
import os

ffibuilder = FFI()

cur_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(cur_dir, '..', 'quicklz.c')) as f:
    ffibuilder.set_source("_pyquicklz", f.read())

with open(os.path.join(cur_dir, 'quicklz_api.h')) as f:
    ffibuilder.cdef(f.read())

if __name__ == '__main__':
    ffibuilder.compile(verbose=True, tmpdir=cur_dir)
