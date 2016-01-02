"""
Command 'upgrade-all' for pipsi-tool
"""

import subprocess
import sys

from pipsi_tool.commands.command import Command
from pipsi_tool.pipsi_package import gather_packages


class UpgradeAll(Command):
    """
    Class for command upgrade-all
    """
    def run(self):
        """
        Run action
        :return:
        """
        packages = gather_packages()
        for package in packages:
            subprocess.run(['pipsi', 'upgrade', package], stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
