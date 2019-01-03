#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = open("clean.txt", "wb")

with open(input_file, "rb") as f:
    byte = f.read(1)
    while byte:
        if byte == b'\xf0':
            # skip
            f.read(3)
        elif byte == b'\xe9':
            f.read(2)
        else:
            output_file.write(byte)
            output_file.write(f.read(2))
        byte = f.read(1)
