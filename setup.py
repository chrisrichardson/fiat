#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (3, 6):
    print("Python 3.6 or higher required, please upgrade.")
    sys.exit(1)


setup(name="fenics-fiat",
      description="FInite element Automatic Tabulator",
      author="Robert C. Kirby et al.",
      author_email="fenics-dev@googlegroups.com",
      url="https://bitbucket.org/fenics-project/fiat/",
      use_scm_version={'parentdir_prefix_version': 'fenics-fiat-'},
      setup_requires=["setuptools_scm"],
      license="LGPL v3 or later",
      packages=["FIAT"],
      install_requires=["numpy", "sympy"])
