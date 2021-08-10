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
from os import mkdir, environ, walk, sep, remove
from os.path import exists, join, expanduser


class rosactive:
    def __init__(self):
        self.rosactive_dir = ".rosactive"
        self.settings_file = "settings.yaml"
        self.index_file = "index.yaml"
        self.arg_list = []

        if self.check_for_firsttime():
            self.init_file_structure()
            sys.exit(0)

        parsed = self.parse_args()
        self.run_arg(parsed)
        print(vars(parsed))

    def check_for_firsttime(self):
        return not self.check_for_settings()

    def get_settings_path(self):
        return join(expanduser("~"), self.rosactive_dir, self.settings_file)

    def get_index_path(self):
        return join(expanduser("~"), self.rosactive_dir, self.settings_file)

    def check_for_settings(self):
        return exists(self.get_settings_path())

    def check_for_index(self):
        return exists(self.get_index_path())

    def create_files(self):
        if self.check_for_settings():
            remove(self.get_settings_path())
        if self.check_for_index():
            remove(self.get_index_path())
        open(self.get_settings_path(), "w+").write("")
        open(self.get_index_path(), "w+").write("")

    def init_file_structure(self):
        print(
            "This appears to be your first time running Rosactive."
            " First time setup will start now."
        )
        if "ROS_DISTRO" in environ.keys():
            print(
                "ERROR: You appear to have some ROS content still sourced "
                "in your shell configuration. Please only use rosactive in "
                "an environment where no ROS content has been sourced (so "
                "that rosactive can do all the management)."
            )
            sys.exit()

        print("Doing initial file structure setup...", end="")
        # create dir if it does not already exist
        if not exists(join(expanduser("~"), ".rosactive")):
            mkdir(join(expanduser("~"), ".rosactive"))
        # create settings, index file if it does not already exist (also clear contents)
        self.create_files()
        print("Done!")

        print("Going to search for indexable workspaces in your home directory.")
        homedir = expanduser("~")
        # max depth of 5 dir's into user directory to find CMakeLists
        maxdepth = 5 + homedir.count(sep)
        potential_workspaces = []

        # walk through all directories in the user's home directory (up to maxdepth)
        for root, _, files in walk(homedir):
            if root.count(sep) < maxdepth:
                for f in files:
                    # ignore hidden directories
                    if root.find(str(sep) + ".") > 0:
                        continue
                    # found src/CMakeLists.txt: this could be a ROS workspace worth indexing.
                    if f == "CMakeLists.txt" and root.endswith("src"):
                        potential_workspaces.append((root, f))

        # now that we have some candidates, we can check if they're actual workspaces and not something else:
        workspaces = []
        for ws in potential_workspaces:
            root, f = ws
            f = open(join(root, f), "r")
            # cmakelists.txt in a catkin workspace will end with 'catkin_workspace()', so we can search for that:
            if "catkin_workspace" in f.read():
                # cool, found one-- but we're in foo/bar/src/CMakeLists, we want to be tracking foo/bar.
                spl = root.split(sep)
                nosrc = sep.join(spl[:-1])
                workspaces.append(nosrc)

        print(
            "Indexing ROS workspaces."
            "No files will be touched (all indexing takes place in ~/.rosactive)"
        )
        for ws in workspaces:
            print(" - " + str(ws))
            self.index(ws)
        print("Initial setup all done! You can now create project configurations.")

    def index(self, string: str):
        with open(join(expanduser("~"), self.rosactive_dir, self.index_file), "a") as f:
            f.write(string + "\n")

    def activate(self, ws):
        pass

    def deactivate(self, ws):
        pass

    def deindex(self, ws):
        pass

    def display(self, ws):
        pass

    def genconfig(self, ws):
        pass

    def reconfig(self, ws):
        pass

    def list(self, ws):
        pass

    def rm(self, ws):
        pass

    def parse_args(self) -> argparse.Namespace:
        self.arg_list = [
            (
                "activate",
                "The specified workspace or configuration will be sourced in following terminal windows",
                self.activate,
            ),
            (
                "deactivate",
                "The specified workspace or configuration will no longer be sourced in following terminal windows",
                self.deactivate,
            ),
            (
                "index",
                "Index a new workspace so that Rosactive can auto-source it later.",
                self.index,
            ),
            (
                "deindex",
                "Remove workspace from Rosactive index (all folders/files will be left untouched).",
                self.deindex,
            ),
            (
                "display",
                "Display the details of the current or specified configuration.",
                self.display,
            ),
            (
                "genconfig",
                "Create a new configuration to be activated/deactivated later.",
                self.genconfig,
            ),
            ("reconfig", "Reconfigure an existing configuration.", self.reconfig),
            ("list", "List available configurations.", self.list),
            ("rm", "Delete an existing configuration.", self.rm),
        ]

        parser = argparse.ArgumentParser(
            usage="Manage currently sourced workspaces and environment variables."
        )
        mutual_exclusive_args = parser.add_mutually_exclusive_group()
        for (arg_name, arg_help, _) in self.arg_list:
            mutual_exclusive_args.add_argument(
                "--" + arg_name, help=arg_help, action="store_true"
            )

        parser.add_argument('argv', nargs='*')

        return parser.parse_args()

    def run_arg(self, parsed):
        arg_count = 0
        parsed = vars(parsed)
        function = None
        for (arg, _, func) in self.arg_list:
            if parsed[arg]:
                arg_count += 1
                function = func

        if arg_count < 1:
            print("Mode argument required: run argparse --help for usage information.")
            sys.exit(1)
        if arg_count > 1:
            print("Too many mode arguments: specify only one at a time.")
            sys.exit(2)

        function(parsed['argv'])


if __name__ == "__main__":
    rosactive()
