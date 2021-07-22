#!/usr/bin/env python3
"""
Manage currently sourced workspaces and environment variables.
Copyright © 2021 cst0 (Chris Thierauf, chris@cthierauf.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import argparse
import sys
from os import mkdir, environ
from os.path import exists, join, expanduser


def check_for_firsttime():
    return not exists(join(expanduser("~"), ".rosactive/settings.yaml"))


def init_file_structure():
    print(
        "This appears to be your first time running Rosactive."
        " First time setup will start now."
    )
    if "ROS_DISTRO" in environ.keys():
        print(
                "ERROR: You appear to have some ROS content still sourced "
                "in your shell configuration. Please only use rosactive in "
                "an environment where no ROS content has been sourced (so "
                "that rosactive can do all the management)"
        )
        sys.exit()

    print("Doing initial file structure setup...", end="")
    # create dir if it does not already exist
    if not exists(join(expanduser("~"), ".rosactive")):
        mkdir(join(expanduser("~"), ".rosactive"))
    # create file if it does not already exist
    open(join(expanduser("~"), ".rosactive/settings.yaml"), "w+").write("")
    print("Done!")

    print("Going to ")


def main():
    if check_for_firsttime():
        init_file_structure()

    # parser = argparse.ArgumentParser(usage="Manage currently sourced workspaces and environment variables.")
    # group = parser.add_mutually_exclusive_group(required=True)
    # group.add_argument('--activate'   , action="store_true", help="The specified workspace or configuration will be sourced in following terminal windows")
    # group.add_argument('--deactivate' , action="store_true", help="The specified workspace or configuration will no longer be sourced in following terminal windows")
    # group.add_argument('--index'      , action="store_true", help="Make the rosactive local database aware of a ROS workspace")
    # group.add_argument('--deindex'    , action="store_true", help="Make the rosactive local database no longer aware of a ROS workspace")
    # group.add_argument('--current'    , action="store_true", help="Set the current workspace (will become the destination for roscd")
    # group.add_argument('--clear'      , action="store_true", help="Deactivate all currently sourced workspaces or configurations")
    # group.add_argument('--configure'  , action="store_true", help="Create collections of sourced content so they can all be sourced at once later")
    # group.add_argument('--source'     , action="store_true", help="Source additional environment variables with each terminal")
    # parsed = parser.parse_args()


if __name__ == "__main__":
    main()
