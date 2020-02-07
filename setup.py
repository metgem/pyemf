#!/usr/bin/env python3

PKG_NAME = "pyemf"

setup_kw = dict(
    name = PKG_NAME,
    version = "2.1.2alpha",
    description = "pyemf is a pure python module that provides bindings for an ECMA-234 compliant vector graphics library",
    license = "LGPLv2",
    author = "Rob McMullen",
    author_email = "robm@users.sourceforge.net",
    url = "https://github.com/metgem/pyemf",
    platforms='any',
	packages = [PKG_NAME],

    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                     'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Multimedia :: Graphics',
                     ]
    )

if __name__ == '__main__':
    from setuptools import setup
    setup(**setup_kw)
