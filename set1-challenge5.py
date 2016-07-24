#!/usr/bin/env python


def repeatingXor(text, key):
	text = bytearray(text)
	key = bytearray(key)
	count = 0
	xorCombo = ""
	for i in text:
		niny = chr(i ^ key[count % 3])
		xorCombo = xorCombo + niny
		count = count + 1

	xorCombo = xorCombo.encode('hex')
	return xorCombo


def main():
	print "Challenge 5: "
	text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal" # Need as bytes
	key ='ICE'
	print ("Text to be encrypted: " + text)
	print ("Key for encryption: " + key)
	xorCombo = repeatingXor(text, key)
	print ("Encrypted Text: " + xorCombo)

main()
