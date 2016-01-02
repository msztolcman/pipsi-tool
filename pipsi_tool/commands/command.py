"""
Abstract class for commands
"""

# pylint: disable=too-few-public-methods,missing-docstring
class Command:
    def __init__(self, args):
        self.args = args

    def execute(self):
        return self.run()

    def run(self):
        """
        Abstract method for executing commands
        @return:
        """
        raise NotImplementedError("Not implemented yet...")
