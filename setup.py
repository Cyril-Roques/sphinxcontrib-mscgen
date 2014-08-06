# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
Fork for Python 3

This package contains the mscgen_ Sphinx_ extension.

.. _mscgen: http://www.mcternan.me.uk/mscgen/
.. _Sphinx: http://sphinx.pocoo.org/

Allow mscgen-formatted Message Sequence Chart (MSC) graphs to be included in
Sphinx-generated documents inline. For example::

    .. msc::

        hscale = "0.5";

        a,b,c;

        a->b [ label = "ab()" ] ;
        b->c [ label = "bc(TRUE)"];
        c=>c [ label = "process()" ];

'''

requires = ['Sphinx>=0.6']

setup(
    name='sphinxcontrib-mscgen',
    version='0.4.1',
    url='https://github.com/alfred82santa/sphinxcontrib-mscgen',
    download_url='https://github.com/alfred82santa/sphinxcontrib-mscgen',
    license='BOLA',
    author='Leandro Lucarella',
    author_email='llucax@gmail.com',
    description='mscgen Sphinx extension for Python 3',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.3',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
