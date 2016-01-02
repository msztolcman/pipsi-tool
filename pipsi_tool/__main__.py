#!/usr/bin/env python3

from pipsi_tool import utils
utils.validate_python_version()

import argparse
import os.path
import sys

from pipsi_tool import commands


PIPSI_BIN_DIR=os.path.expanduser('~/.local/venvs/')


def parse_args(argv):
    p = argparse.ArgumentParser()

    p.add_argument('--venvs-dir', type=str, dest='pipsi_venvs_dir', default='~/.local/venvs/',
        help='')

    sub = p.add_subparsers(dest='command')

    p_reinstall_all = sub.add_parser('reinstall-all', aliases=commands.get_aliases_for('reinstall-all'),
        help='')

    p_upgrade_all = sub.add_parser('upgrade-all', aliases=commands.get_aliases_for('upgrade-all'),
        help='')

    args = p.parse_args(argv)

    args.pipsi_venvs_dir = os.path.expanduser(args.pipsi_venvs_dir)
    if not os.path.isdir(args.pipsi_venvs_dir):
        p.error("Directory %s not found: is pipsi installed?" % args.pipsi_venvs_dir)

    if not args.command:
        p.error('too few arguments')

    return args


def main(argv):
    args = parse_args(argv)

    cmd = commands.get(args.command)
    cmd = cmd(args)
    return cmd.execute()


sys.exit(main(sys.argv[1:]))
