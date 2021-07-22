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

def main():
    parser = argparse.ArgumentParser(usage="Manage currently sourced workspaces and environment variables.")
    parser.add_argument('selection', choices=[
        'activate',
        'deactivate',
        'index',
        'deindex',
        'current',
        'clear',
        'configure',
        'source'
        ], help="\
                - activate: The specified workspace or configuration will be sourced in following terminal windows.\n\
                - deactivate: The specified workspace or configuration will no longer be sourced in following terminal windows.\n\
                - index: Make the rosactive local database aware of a ROS workspace.\n\
                - deindex: Make the rosactive local database no longer aware of a ROS workspace.\n\
                - current: Set the current workspace (will become the destination for roscd)\n\
                - clear: Deactivate all currently sourced workspaces or configurations.\n\
                - configure: Create collections of sourced content so they can all be sourced at once later.\n\
                - source: Source additional environment variables with each terminal.\n\
        ")
    parsed = parser.parse_args()

if __name__ == '__main__':
    main()
