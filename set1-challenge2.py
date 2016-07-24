#! /usr/local/env python
import sys
import binascii
import string
import operator
import re

def xorStuff(decodedHexNum, decodedNum2):
	decodedHexNum = decodedHexNum.decode('hex')
	decodedNum2 = decodedNum2.decode('hex')
	fNum = ''
	n = 0

	for i in decodedHexNum:
		ni = ord(i)^ord(decodedNum2[n])

		nini = chr(ni)

		fNum = fNum + nini
		n = n + 1

	fNum = fNum.encode('hex')
	return fNum

def main():

	combo = "1c0111001f010100061a024b53535009181c"
	print "Combo: " + combo
	xorNum = "686974207468652062756c6c277320657965"
	print "XorNum: " + xorNum
	comboXor = xorStuff(combo, xorNum)
	print "comboXor: " + comboXor

main()
