from os import path

__projectname__ = 'buildertron'
__version__ = '0.1.0'
__homepage__ = 'https://github.com/swprojects/Buildertron'
__author__ = 'Simon Wu'
__description__ = 'A buildozer front-end for Linux'
__author_email__ = 'swprojects@runbox.com',

__classifiers__ = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

try:
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README'), encoding='utf-8') as readme_file:
        __readme__ = readme_file.read()
except Exception:
    __readme__ = ''

try:
    with open(path.join(here, 'HISTORY'), encoding='utf-8') as history_file:
        __history__ = history_file.read().replace('.. :changelog:', '')
except Exception:
    __history__ = ''
