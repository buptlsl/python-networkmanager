#!/usr/bin/python

from distutils.core import setup

setup(name = "python-networkmanager",
      version = "1.0.1",
      author = "Dennis Kaarsemaker",
      author_email = "dennis@kaarsemaker.net",
      url = "http://github.com/seveas/python-networkmanager",
      description = "Easy communication with NetworkManager",
      py_modules = ["NetworkManager"],
      scripts = ["n-m"],
      classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Networking',
      ]
)
