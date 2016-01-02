"""
Command 'reinstall-all' for pipsi-tool
"""

import subprocess
import sys

from pipsi_tool.commands.command import Command
from pipsi_tool.pipsi_package import gather_packages, package_python_version


class ReinstallAll(Command):
    """
    Class for command reinstall-all
    """
    def run(self):
        """
        Run action
        :return:
        """
        packages = gather_packages()
        for package in packages:
            if package == 'pipsi':
                continue

            python_version = package_python_version(package, self.args.pipsi_venvs_dir)
            print("Reinstalling %s with python%s" % (package, python_version))
            subprocess.run(['pipsi', 'uninstall', '--yes', package], stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin, check=True)
            subprocess.run(['pipsi', 'install', '--python', 'python%s' % python_version, package], stdout=sys.stdout, stderr=sys.stderr,
                    stdin=sys.stdin, check=True)
            print()
