#! /usr/local/env python

import base64
import binascii

def hexToBase64(hexNum):
	binNum = binascii.unhexlify(hexNum)
	fNum = binascii.b2a_base64(binNum)
	return fNum

def main():
	hexNum = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	print (hexNum)
	fNum = hexToBase64(hexNum)
	print "Converted to base 64 is: "
	print (fNum)

main()
