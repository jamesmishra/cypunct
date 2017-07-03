# coding=utf-8
# pylint: skip-file
"""
Run all tests for cypunct.

Common bits of data are module-level globals, but the
actual test code is in the ``Tests`` class.

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import timeit
import unittest

TEST_SETUP = """

import cypunct

import regex

baseline = regex.compile(
    r'[\p{Punctuation}\p{Separator}\p{Symbol}\p{Other}]+',
    flags=regex.MULTILINE
)

# These variables are named after the Unicode character
# classes they belong to. I wanted two different examples for the
# character classes P, S, C, and Z.
Po = u"!"
Ps = u"("

Sc = u"$"
Sm = u"<"

Cc = u" "
Cf = u"\u0600"

Zs = u" "
Zp = u"\u2029"

# This is a sample of a typical input sentence that we
# might get.
testcase = u'''James{0}{1}{2}{3}{4}{5}{6}{7}is{1}the{2}
best{3}person{4}ever{5}to{6}have{7}ever lived.
'''.format(Po, Ps, Sc, Sm, Cc, Cf, Zs, Zp) * 2000

# This is a sample of a typical
exhaustive_testcase = u"James".join(
    cypunct.unicode_classes.COMMON_SEPARATORS)

custom_split_set = set([u"a"])
"""

exec(TEST_SETUP)


class Tests(unittest.TestCase):

    bench_iterations = 300

    def test_benchmark(self):
        """Benchmark our code against a regex baseline."""
        baseline_speed = timeit.timeit(
            "baseline.split(testcase)",
            setup=TEST_SETUP,
            number=self.bench_iterations,
        )
        cypunct_speed = timeit.timeit(
            "cypunct.split(testcase)",
            setup=TEST_SETUP,
            number=self.bench_iterations,
        )
        print(
            "\nBenchmark results: ({0} loops)\n\n".format(
                self.bench_iterations))
        print("baseline speed:", baseline_speed, sep="\t")
        print("cypunct speed:", cypunct_speed, sep="\t")

    def test_equality(self):
        """Check we split on the same tokens as the baseline."""
        baseline_split = baseline.split(exhaustive_testcase)
        cypunct_split = cypunct.split(exhaustive_testcase)
        baseline_split_set = set(baseline_split)
        cypunct_split_set = set(cypunct_split)
        assert baseline_split[0] == u''
        assert baseline_split[1:] == cypunct_split
        assert baseline_split_set == cypunct_split_set
        assert baseline_split_set == set((u'', u'James'))

    def test_custom_split_set(self):
        """Test that we can use our own split frozensets."""
        expected = ['J', 'mes is ', ' kind ', 'nd mor', 'l hum', 'n.']
        actual = cypunct.split(
            "James is a kind and moral human.",
            frozenset(['a'])
        )
        assert expected == actual
