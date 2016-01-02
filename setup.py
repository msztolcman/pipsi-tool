from pipsi_tool import utils
utils.validate_python_version()

from codecs import open
from os import path
from setuptools import setup, find_packages


BASE_DIR = path.abspath(path.dirname(__file__))

with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pipsi-tool',
    version='1.0.1',
    description='pipsi-tool is set of helpers for https://github.com/mitsuhiko/pipsi',
    long_description=long_description,
    url='http://msztolcman.github.io/pipsi-tool/',
    author='Marcin Sztolcman',
    author_email='marcin@urzenia.net',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['argparse', ],
    packages=find_packages(),

    keywords='pipsi',

    entry_points={
        'console_scripts': [
            'pipsi-tool=pipsi_tool.__main__:main',
        ],
    },
)

