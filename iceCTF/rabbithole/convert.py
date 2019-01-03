#!/usr/bin/python3

import sys

inp = sys.argv[1]

with open(inp, "rb") as input_file:
    with open("isolated.txt", "wb") as output_file:
        byte = input_file.read(1)
        while byte:
            if byte == b'\xf0':
                output_file.write(input_file.read(3))

            byte = input_file.read(1)