#!/usr/bin/env python3

"""
pipsi_tool is set of helpers that are missing in pipsi (https://github.com/mitsuhiko/pipsi)
"""

from pipsi_tool import utils
utils.validate_python_version()

# pylint: disable=wrong-import-order
import argparse
import os.path
import sys

from pipsi_tool import commands


PIPSI_BIN_DIR = os.path.expanduser('~/.local/venvs/')


def parse_args(argv):
    """
    Parse arguments
    :param argv:
    :return:argparse.Namespace
    """
    # pylint: disable=invalid-name
    p = argparse.ArgumentParser()

    p.add_argument('--venvs-dir', type=str, dest='pipsi_venvs_dir', default='~/.local/venvs/',
        help='')

    sub = p.add_subparsers(dest='command')

    # pylint: disable=unused-variable
    p_reinstall_all = sub.add_parser('reinstall-all', aliases=commands.get_aliases_for('reinstall-all'),
        help='')

    # pylint: disable=unused-variable
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
    """
    :param argv:
    :return:
    """
    args = parse_args(argv)

    cmd = commands.get(args.command)
    cmd = cmd(args)
    return cmd.execute()


sys.exit(main(sys.argv[1:]))
