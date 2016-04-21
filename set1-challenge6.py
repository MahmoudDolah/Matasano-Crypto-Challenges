import random


def hammingDistance(str1, str2):
    # Count the number of differences between equal length strings str1 and str2 and return it
    diffs = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            diffs += 1
    return diffs

def findKeySize(lines):
    keysize = random.randint(2, 40)

    count = 0




def main():

    str1 = "this is a test"
    str2 = "wokka wokka!!!"
    diffs = hammingDistance(str1, str2)
    print diffs

    file encrypted = open("encryptedFile.txt")
    with open("encryptedFile.txt", 'r') as f:
        lines = f.readlines()

    findKeySize(lines)


main()
