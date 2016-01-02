import subprocess
import sys

from pipsi_tool.commands.command import Command
from pipsi_tool.pipsi_package import gather_packages


class UpgradeAll(Command):
    def run(self):
        packages = gather_packages()
        for package in packages:
            subprocess.run(['pipsi', 'upgrade', package], stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)
