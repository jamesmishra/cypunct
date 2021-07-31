# cython: boundscheck=False
from __future__ import absolute_import

from libc.stdint cimport uint64_t
from cypunct.unicode_classes import COMMON_SEPARATORS


cpdef split(unicode input_str, frozenset split_chars=None):
    """
    Split a unicode str with a frozenset of code points as delimiters.

    Example:
        >>> from cypunct import split
        >>> split("James Mishra is the... best human ever, or so I think.", frozenset({' ', '.', ','}))
        ['James', 'Mishra', 'is', 'the', 'best', 'human', 'ever', 'or', 'so', 'I', 'think', '']

    Args:
        input_str(unicode): A string that you want to split into a
            list of Unicode strings.

        split_chars(frozenset): This is a ``frozenset`` (and no,
            a regular ``set`` won't do), of delimiters. Each
            delimiter should be a single Unicode code point.
            If ``split_chars`` is not provided, we will default to
            ``cypunt.unicode_classes.COMMON_SEPARATORS``.

    Returns:
        (list): A list of Unicode strings, made up of splitted
            portions of ``input_str``, not including any of the
            delimiters in ``split_chars``.

    """
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
