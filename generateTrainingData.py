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
# A random number of characters A-Z, and space are generated,
# and each letter has 0-2 random bits flipped to introduce errors.

import random
from fonttable import fonttable

zero = '0'
one = '1'
minErrors = 0
maxErrors = 2
numChars = 1000

def flipBit(bitPattern, position):
    if bitPattern[position] == zero:
        bitPattern[position] = one
    else:
        bitPattern[position] = zero
        
    return bitPattern
    
def introduceErrors(bitPattern):
    numErrors = random.randint(minErrors,maxErrors)
    
    for error in range(numErrors):
        errorPosition = random.randint(0,len(bitPattern)-1)
        bitPattern = flipBit(bitPattern, errorPosition)
    
    return bitPattern  

def getBitPattern(asciiVal):
    bitPattern = []
    firstcol = (asciiVal - ord(' ')) * 5

    for col in range (0, 5):
        line = fonttable[firstcol + col]
        
        for row in [1, 2, 4, 8, 16, 32, 64]:
            if (line & row): 
                bitPattern.append(one)
            else: 
                bitPattern.append(zero)

    return bitPattern

def getRandomCharAZSpace():
    which = random.randint(0,26)
    if which == 0:
        return 32
    else: 
        return which + 64

def printSideways(bitPattern):
    print(bitPattern[-1])
    print(bitPattern[0:7])
    print(bitPattern[7:14])
    print(bitPattern[14:21])
    print(bitPattern[21:28])
    print(bitPattern[28:35])

# Main program starts here

f=open('training.dat', 'w')
for i in range(numChars):
    asciiVal = getRandomCharAZSpace()
    
    bitPattern = getBitPattern(asciiVal)
    bitPattern = introduceErrors(bitPattern)
    bitPattern.append(chr(asciiVal))

    bitString = ''.join(bitPattern)

    f.write(bitString+'\n')
    
f.close()