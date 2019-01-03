#!/usr/bin/python3

import sys
from collections import namedtuple

output = ""

def write_letter(code):
    global output
    print(str(code) + " : " + chr(code))
    output += chr(code)

input_word = input()

alphabet = [chr(x) for x in range(32, 127)]

def test_printable(ord):
    global alphabet
    if chr(ord) in alphabet:
        return True

# skip first letter
input_idx = 1

output = ""

while input_idx < len(input_word):
    section = input_word[input_idx : input_idx + 4]
    # print ("decoding \"" + section + "\"...")

    ############################################################################
    # first character
    character = ord(section[0])
    first_char_possible = set()
    # print ("analyzing character : \'" + chr(character) + "\'")
    
    if character != 0x20:
        # character - 0x20 = input >> 22
        possible_input = (character - 0x20) << 2

        if test_printable(possible_input | 0b00):
            first_char_possible.add(chr(possible_input | 0b00))
        if test_printable(possible_input | 0b01):
            first_char_possible.add(chr(possible_input | 0b01))
        if test_printable(possible_input | 0b11):
            first_char_possible.add(chr(possible_input | 0b11))
        if test_printable(possible_input | 0b10):
            first_char_possible.add(chr(possible_input | 0b10))
    else: # character was 0x20
        for i in range(0, 4):
            if test_printable(ord(i)):
                first_char_possible.add(chr(i))

    ############################################################################
    # second character
    character = ord(section[1])
    second_char_possible = set()
    # print ("analyzing character : \'" + chr(character) + "\'")
    
    orsrc_by_char = {}

    for char in first_char_possible:
        if (ord(char) << 4) & 0x30 != 0:
            orsrc_by_char[char] = (((ord(char) << 4) & 0x30) + 0x20)
        else:
            orsrc_by_char[char] = (0x20)

    valid_first_chars = set()

    for orsch_char in orsrc_by_char:
        for char in alphabet:
            if (ord(char) >> 4) | orsrc_by_char[orsch_char] == character:
                second_char_possible.add(char)
                valid_first_chars.add(orsch_char)

    # trim first list
    first_char_possible = first_char_possible.intersection(valid_first_chars)

    ############################################################################
    # third character
    character = ord(section[2])
    third_char_possible = set()
    # print ("analyzing character : \'" + chr(character) + "\'")
    
    orsrc_by_char = {}

    for char in second_char_possible:
        if (ord(char) << 2) & 0x3c != 0:
            orsrc_by_char[char] = (((ord(char) << 2) & 0x3c) + 0x20)
        else:
            orsrc_by_char[char] = (0x20)

    valid_second_chars = set()

    for orsch_char in orsrc_by_char:
        for char in alphabet:
            if (ord(char) >> 6) | orsrc_by_char[orsch_char] == character:
                third_char_possible.add(char)
                valid_second_chars.add(orsch_char)

    # trim first list
    second_char_possible = second_char_possible.intersection(valid_second_chars)

    ############################################################################
    # fourth character
    character = ord(section[3])
    fourth_char_possible = set()
    # print ("analyzing character : \'" + chr(character) + "\'")
    
    if character != 0x20:
        # character - 0x20 = input & 0x3f
        possible_input = (character - 0x20) & 0x3f

        if test_printable(possible_input | 0b00 << 6):
            fourth_char_possible.add(chr(possible_input | 0b00 << 6))
        if test_printable(possible_input | 0b01 << 6):
            fourth_char_possible.add(chr(possible_input | 0b01 << 6))
        if test_printable(possible_input | 0b10 << 6):
            fourth_char_possible.add(chr(possible_input | 0b10 << 6))
        if test_printable(possible_input | 0b11 << 6):
            fourth_char_possible.add(chr(possible_input | 0b11 << 6))
    else: # character was 0x20
        fourth_char_possible.add(chr(0))
        fourth_char_possible.add(chr(0b01000000))
    
    input_idx += 4

    output += ''.join(first_char_possible)
    output += ''.join(second_char_possible)
    # output += list(third_char_possible)[0]
    output += ''.join(fourth_char_possible.intersection(third_char_possible))

    # print(first_char_possible)
    # print(second_char_possible)
    # print(fourth_char_possible.intersection(third_char_possible))

print('\'' + output + '\'')