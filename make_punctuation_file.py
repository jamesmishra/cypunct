#!/usr/bin/env python3
"""
Build the frozensets of unicode punctuation that we want.

This creates a Python file with frozensets for every
Unicode character class, and then one for all the
punctuation and symbol classes.
"""
from collections import defaultdict

FILE_HEADER = '''
# coding=utf-8
# pylint: skip-file
"""
Load frozensets for every Unicode character class, and then some.


"""
from __future__ import unicode_literals

'''

COMMON_SEPARATORS = frozenset(('C', 'P', 'S', 'Z'))


def frozenset_repr(iterable):
    """
    Return a repr() of frozenset compatible with Python 2.6.

    Python 2.6 doesn't have set literals, and newer versions
    of Python use set literals in the ``frozenset()`` ``__repr__()``.
    """
    return "frozenset(({0}))".format(
        ", ".join(map(repr, iterable))
    )


def char_classes_to_vars(character_classes):
    """Return an iterable over Unicode character classes.

    More precisely, we take a dictionary mapping Unicode character
    classes and a list of characters in that class... and then
    we return an iterable of strings, where each string represents
    a Python assignment. The variable name is the character class,
    and the value is a frozenset of the characters in the class.
    """
    classes = sorted(character_classes.keys())
    for char_class in classes:
        yield "{0} = {1}\n\n".format(
            char_class,
            frozenset_repr(character_classes[char_class])
        )

def main():
    """Run the script."""
    character_classes = defaultdict(list)
    with open("UnicodeData.txt", encoding="utf-8") as read_handle:
        for raw_line in read_handle:
            line = raw_line.split(";")
            char = chr(int(line[0], base=16))
            char_class = line[2]
            char_superclass = char_class[0]
            character_classes[char_class].append(char)
            character_classes[char_superclass].append(char)
            if char_superclass in COMMON_SEPARATORS:
                character_classes['COMMON_SEPARATORS'].append(char)

    with open('cypunct/unicode_classes.py', 'w') as write_handle:
        write_handle.write(FILE_HEADER)
        write_handle.writelines(char_classes_to_vars(character_classes))


if __name__ == "__main__":
    main()
