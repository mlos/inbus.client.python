#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
import re
import sys
from setuptools import setup, find_packages

####################################################
NAME = "inbus-client"
KEYWORDS = ["client inbus publisher subscriber pub sub"]
META_PATH = os.path.join("src", "inbus", "__init__.py")
PACKAGES = find_packages(where="src")
CLASSIFIERS = [
        "License :: OSI Approved :: BSD License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Networking",
        "Topic :: System :: Distributed Computing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
####################################################
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
test_deps = [
    'mock;python_version<"3.3"',
    "pytest>=3.1",
    "pytest-cov"
]
install_deps = [
    "inbus-server>=1.0.0"
]

setup(
    name=NAME,
    version=find_meta("version"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    description=find_meta("description"),
    long_description=read("README.rst"),
    license=find_meta("license"),
    keywords=KEYWORDS,
    url=find_meta("uri"),
    download_url="https://github.com/mlos/inbus.client.python/tarball/" + find_meta("version"),
    packages=PACKAGES,
    package_dir={"": "src"},
    install_requires=install_deps,
    setup_requires=pytest_runner,
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx>=1.5.1'
        ],
        'test': test_deps,
        'qa': [
            'flake8',
            'rstcheck'
        ]
    },
    zip_safe=False,
    classifiers=CLASSIFIERS
)
