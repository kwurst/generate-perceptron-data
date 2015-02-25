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
# A random number of characters are generated,
# and each letter has 0-2 random bits flipped to introduce errors.

import random
from fonttable import fonttable
from characterbitmaps import *

numChars = 10000

def getRandomCharASCII():
    return random.randint(32,126)

f=open('training.dat', 'w')
for i in range(numChars):
    asciiVal = getRandomCharASCII()
    
    bitPattern = getBitPattern(asciiVal)
    bitPattern = introduceErrors(bitPattern)
    bitPattern.append(chr(asciiVal))

    bitString = ''.join(bitPattern)

    f.write(bitString+'\n')
    
f.close()