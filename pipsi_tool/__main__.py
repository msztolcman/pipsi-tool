#!/usr/bin/env python3

from pipsi_tool import utils
utils.validate_python_version()

import argparse
import os.path
import sys

from pipsi_tool import commands


PIPSI_BIN_DIR=os.path.expanduser('~/.local/venvs/')


def parse_args(argv):
    p = argparse.ArgumentParser(argv)

    sub = p.add_subparsers(dest='command')

    p_reinstall_all = sub.add_parser('reinstall-all', aliases=commands.get_aliases_for('reinstall-all'),
        help='')

    p_upgrade_all = sub.add_parser('upgrade-all', aliases=commands.get_aliases_for('upgrade-all'),
        help='')

    args = p.parse_args(argv)

    if not args.command:
        p.error('too few arguments')

    args.pipsi_bin_dir = os.path.expanduser('~/.local/venvs/')

    return args


def main(argv):
    args = parse_args(argv)

    cmd = commands.get(args.command)
    cmd = cmd(args)
    return cmd.execute()


sys.exit(main(sys.argv[1:]))
