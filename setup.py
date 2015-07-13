# -*- coding: utf-8 -*-
"""\
=========
test.tags
=========

Python package to test tags
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup, find_packages
import os, sys

version = '1.0.0.dev0'

this_directory = os.path.abspath(os.path.dirname(__file__))

def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',),('CHANGES.rst',))]
    )
dev_require = []
dev_require += ['nose', 'coverage']
if sys.version_info < (2, 7):
    dev_require += ['unittest2']


setup(name='TagsTest',
      version=version,
      description="Python package to test tags",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
          ],
      keywords='',  # FIXME: Add whatefer fits
      author='Jean',
      author_email='jean@localhost',
      url='http://pypi.python.org/pypi/TagsTest',
      license='GPLv3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['test'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
          ],
      entry_points={
          },
      tests_require=dev_require,
      test_suite='nose.collector',
      extras_require={
          'dev': dev_require
      })
