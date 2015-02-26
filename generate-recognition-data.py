# Copyright (C) 2015 Karl R. Wurst
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA

####################################################################
# Generate random character training data for a perceptron
#
# The characters are 5x7 (5 bits wide, 7 bits high)
# turned sideways (90 degrees clockwise) from bitmaps posted
# by G. Forrest Cook and released under the GPLv3 license.
# See fonttable.py for bitmaps.
# 
# A text file is read, each character converted to the bitmap,
# and each character has 0-2 random bits flipped to introduce errors.

import random
from fonttable import fonttable
from characterbitmaps import *
import codecs

fin = codecs.open('recognition.txt', 'r', 'utf-8')
fout=open('recognition.dat', 'w')

text = fin.read()
linecount = 0
for char in text:
    if ord(char) not in range(32, 127):
        char = ' '
    
    bitPattern = getBitPattern(ord(char))
    bitPattern = introduceErrors(bitPattern)
    
    bitString = ''.join(bitPattern)

    fout.write(bitString + str(linecount) + '\n')
    linecount = linecount + 1

fout.close()