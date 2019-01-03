#!/usr/bin/python3

import sys

input_file = sys.argv[1]
output_file = open("twenty.txt", "w")
num = int(sys.argv[2])

with open(input_file, "r") as f:
    chunk = f.read(num)
    while chunk:
        output_file.write(chunk[0])
        chunk = f.read(num)