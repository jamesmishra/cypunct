# cython: boundscheck=False
from __future__ import absolute_import

from libc.stdint cimport uint64_t
from cypunct.unicode_classes import COMMON_SEPARATORS


cpdef split(unicode input_str, frozenset split_chars=None):
    if split_chars is None:
        split_chars = COMMON_SEPARATORS
    output = []
    cdef unicode input_str_idx
    cdef uint64_t start_idx = 0
    cdef uint64_t idx
    cdef uint64_t input_str_len = len(input_str)
    for idx in range(input_str_len):
        input_str_idx = input_str[idx]
        if input_str_idx in split_chars:
            if start_idx != idx:
                output.append(input_str[start_idx:idx])
            start_idx = idx + 1
    output.append(input_str[start_idx:])
    return output
