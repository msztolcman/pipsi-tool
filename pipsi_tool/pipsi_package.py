"""
Set of tools for working with pipsi packages
"""

import os
import os.path
import re
import subprocess

RXP_PACKAGES = re.compile(r'^\s*Package\s+"([a-zA-Z0-9_.-]+)"')


def gather_packages():
    """
    Find all pipsi packages
    :return:list
    """
    proc = subprocess.run(['pipsi', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)

    packages = []
    for line in proc.stdout.decode().splitlines():
        match = RXP_PACKAGES.search(line)
        if match:
            packages.append(match.group(1))

    packages.sort()
    return packages


def package_python_version(package, pipsi_venvs_dir):
    """
    Find major python version used with given package
    :param package:
    :param pipsi_venvs_dir:
    :return:str
    """
    package_bin_dir = os.path.join(pipsi_venvs_dir, package, 'bin')
    python_bin = os.path.join(package_bin_dir, 'python')

    python_version = None
    if os.path.islink(python_bin):
        python_version = os.readlink(python_bin).replace('python', '')[0]

    if not python_version:
        for ver in ('2.6', '2.7', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5'):
            if os.path.exists(os.path.join(package_bin_dir, 'python%s' % ver)):
                python_version = ver[0]
                break

    if not python_version:
        for ver in ('2', '3'):
            if os.path.exists(os.path.join(package_bin_dir, 'python%s' % ver)):
                python_version = ver
                break

    return python_version
