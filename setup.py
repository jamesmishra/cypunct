from setuptools import Extension
from setuptools import setup

setup(
    name="cypunct",
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
    ],
    tests_require=[
        # We compare our speed benchmarks to a Unicode regex
        # compiled with the third-party "regex" package.
        'regex'
    ],
    test_suite="cypunct.test_suite"
)
