#! /usr/local/env python3
import sys
import binascii
import string
import operator
import re

def scoreText(txt):                                             # Get score for text
        lamb = lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' '
        scr = filter(lamb, txt)
        lenScr = float(len(scr))
        nScr = lenScr / len(txt)
        return nScr

def decipherSingleXor(msg):
    ans = []
    chars = []
    for i in range(256):
        chars = [chr(y ^ i) for y in msg]                   # Loop through and xor individual digit
        nScr = scoreText(chars)
        ans.append([nScr, ''.join(chars), i])
    return max(ans, key=lambda x: x[0])                       # return highest score

def main():
	print ("Challenge 3: ")
	cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	cipher = cipher.decode('hex')
	cipher = bytearray(cipher)
	ni = decipherSingleXor(cipher)
	print (ni, "\n")

main()
