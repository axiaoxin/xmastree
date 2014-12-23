#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('readme.md').read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='xmastree',
    version='0.0.1',
    description='merry xmas',
    long_description=readme,
    author='axiaoxin',
    author_email='254606826@qq.com',
    url='https://github.com/axiaoxin/xmastree',
    packages=[
        'xmastree',
    ],
    package_dir={'xmastree':
                 'xmastree'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='xmastree',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    entry_points={
        'console_scripts': ['xmastree = xmastree.XmasTree:show']
    },
    tests_require=test_requirements
)
