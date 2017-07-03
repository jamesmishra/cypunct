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
    ]
)
