#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# readmeta.py - part of the FDroid server tools
# Copyright (C) 2014 Daniel Martí <mvdan@mvdan.cc>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os, metadata

def main():

    if not os.path.isdir('metadata'):
        return

    metadata.read_metadata(xref=False, store=False)

if __name__ == "__main__":
    main()
