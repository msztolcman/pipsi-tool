"""
Utils
"""

import platform
import sys

import pkg_resources

def validate_python_version():
    """
    Verify python version and exits if version is too low
    :return:
    """
    if pkg_resources.parse_version(platform.python_version()) < pkg_resources.parse_version('3.5.0'):
        print("Sorry, Python 3.5+ is required")
        sys.exit(1)
