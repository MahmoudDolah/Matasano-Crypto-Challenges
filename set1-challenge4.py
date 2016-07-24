#!/usr/env/bin python3

import re
from challenge3 import scoreText
from challenge3 import decipherSingleXor

def findSingleXor(lines):
    ans = []
    for aLine in lines:                                              # Get Lines from File
        strLine = re.sub('[\n]','', aLine).decode('hex')
        aLine = bytearray(strLine)
        nini = decipherSingleXor(aLine)                              # Use code from challenge 3 and obligatory Monty Python reference
        ans.append(nini)
    return (max(ans, key = lambda x: x[0]))                     # return one with highest score


def main():
    with open('ch4File.txt', 'r') as f:
        lines = f.readlines()

    ans = findSingleXor(lines)
    print (ans, "\n")

main()
