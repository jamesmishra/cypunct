import io
import os
from setuptools import Extension
from setuptools import setup

version = '0.1.1.dev0'

DESCRIPTION = (
    "Cypunct is a Cython package to split Unicode "
    "strings based on a given frozenset of Unicode code points."
)

ROOT = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(ROOT, 'README.rst'), encoding='utf8') as f:
    README = f.read()

setup(
    name="cypunct",
    description=DESCRIPTION,
    long_description=README,
    keywords="unicode string splitting",
    author="James Mishra",
    author_email="j@jamesmishra.com",
    url="https://github.com/jamesmishra/cypunct",
    license='MIT',
    version=version,
    packages=["cypunct"],
    py_modules=[
        "cypunct.cypunct",
        "cypunct.unicode_classes",
        "cypunct.test_suite"
        ],
    ext_modules=[
        Extension(
            "cypunct.cypunct", sources=["cypunct/cypunct.pyx"]
        )
    ],
    setup_requires=[
        # Setuptools 18.0 properly handles Cython extensions.
        'setuptools>=18.0',
        'cython',
        "zest.releaser"
    ],
    tests_require=[
        # We compare our speed benchmarks to a Unicode regex
        # compiled with the third-party "regex" package.
        'regex'
    ],
    test_suite="cypunct.test_suite",
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    zip_safe=False
)
