#!/usr/bin/env python3

import pkg_resources
import platform
import sys

if pkg_resources.parse_version(platform.python_version()) < pkg_resources.parse_version('3.5.0'):
    print("Sorry, Python 3.5+ is required")
    sys.exit(1)


import argparse
import os.path

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

if __name__ == '__main__':
    main(sys.argv[1:])