#!/usr/bin/env python3

import random

def hammingDistance(str1, str2):
    # Count the number of differences between equal length strings str1 and str2 and return it
    return sum([bin(str1[i] ^ str2[i]).count('1') for i in range(len(str1))])


def findKeySize(lines):
    keysize = random.randint(2, 40)
    count = 0




def main():

    str1 = b'this is a test'
    str2 = b'wokka wokka!!!'
    diffs = hammingDistance(str1, str2)
    print(diffs)

    encrypted = open("ch6File.txt")
    with open("encryptedFile.txt", 'r') as f:
        lines = f.readlines()

    findKeySize(lines)


main()
