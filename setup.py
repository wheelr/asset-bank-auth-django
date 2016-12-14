import os

from setuptools import find_packages
from setuptools import setup

_CURRENT_DIR_PATH = os.path.abspath(os.path.dirname(__file__))

_README_CONTENTS = open(os.path.join(_CURRENT_DIR_PATH, 'README.md')).read()

_VERSION = '1.0.0'

_LONG_DESCRIPTION = _README_CONTENTS

setup(
    name='asset-bank-auth-django',
    version=_VERSION,
    description="Django app to allow integration with the Asset Bank 'Secure Link to App' functionality",
    long_description=_LONG_DESCRIPTION,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    keywords='django asset bank auth',
    author='Bright Interactive',
    author_email='info@bright-interactive.co.uk',
    url='http://www.bright-interactive.com/',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['assetbankauth'],
    install_requires=[
        'pycrypto>=2.6.1',
        'Django>=1.8',
    ]
)
