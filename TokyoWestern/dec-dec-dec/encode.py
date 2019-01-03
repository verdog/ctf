#!/usr/bin/python3

import sys

output = ""

def write_letter(code):
    global output
    # print(str(code) + " : " + chr(code))
    output += chr(code)

input_word = sys.argv[1]

# length
length = (((len(input_word) * 4 * 0xaaaaaaab) & 0xffffffff00000000) >> 32) // 2 + 1
# print ("Length: " + str(length))

# pad end with zeros until it is a multiple of 3 in length
while len(input_word) % 3 != 0:
    input_word += chr(0x0)

# first letter
code = (len(input_word) & 0x3f) + 0x20
write_letter(code)

input_idx = 0
counter = 0

while counter < len(input_word):
    letter_code = ord(input_word[input_idx])

    if (letter_code >> 2) != 0:
        write_letter((letter_code >> 2) + 0x20)
    else:
        write_letter(0x20)
    
    # orsrc
    if ((letter_code) << 4) & 0x30 != 0:
        orsrc = (((letter_code) << 4) & 0x30) + 0x20
    else:
        orsrc = 0x20

    # get letter    
    letter_code = ord(input_word[input_idx + 1])

    write_letter(((letter_code) >> 4) | orsrc)

    #orsrc
    if ((letter_code) << 2) & 0x3c != 0:
        orsrc = (((letter_code) << 2) & 0x3c) + 0x20
    else:
        orsrc = 0x20
    
    # get letter
    letter_code = ord(input_word[input_idx + 2])

    write_letter(((letter_code) >> 6) | orsrc)

    if (letter_code) & 0x3f != 0:
        write_letter(((letter_code) & 0x3f) + 0x20)
    else:
        write_letter(0x20)

    counter += 3
    input_idx += 3

print(output)