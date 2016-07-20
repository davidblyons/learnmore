#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
#
#  mpg.py
#
#  Copyright 2016 David Lyons < davidblyons@gmail.com >
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
print("This will calculate MPG given miles driven and gallons used.")

miles_driven = float(input("Enter miles driven:"))
gallons_used = float(input("Enter gallons used:"))

mpg = miles_driven / gallons_used
print('Miles per gallon: ', round(mpg, 2),' mpg')
