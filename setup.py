#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


setup(
    name='pytaxonomies',
    version='0.5',
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    maintainer='Raphaël Vinot',
    url='https://github.com/MISP/PyTaxonomies',
    description='Python API for the taxonomies.',
    packages=['pytaxonomies'],
    scripts=['bin/pytaxonomies'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet',
    ],
    tests_requires=['nose'],
    test_suite='nose.collector',
    install_requires=['requests'],
)
