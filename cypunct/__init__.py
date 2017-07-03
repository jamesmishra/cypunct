"""
Split a Unicode string by a frozenset of delimiters.

See ``cypunct.split``'s docstring for more information.
"""
from __future__ import absolute_import

import sys

from cypunct.cypunct import split

if sys.maxunicode != 1114111:
    raise UnicodeError(
        "Cypunct is not compatible with this distribution of Python. "
        "Please upgrade to Python 3.3 or better... or recompile "
        "your current Python installation to to use UCS-4."
        "\r\n\r\n",
        "See https://stackoverflow.com/a/29109996/49143 for details."
    )
