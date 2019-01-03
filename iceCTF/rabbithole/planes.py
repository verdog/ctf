#!/usr/bin/python3

import sys

byte = int(sys.argv[1])

with open('onion3.txt', 'r') as f:
    w = open('plane_' + str(byte), "w")
    chunk = f.read(8)
    while chunk:
        if len(chunk) < 8:
            break

        write_byte = 0
        for i in range(0, 8):
            write_byte |= (ord(chunk[i]) & (1 << byte)) << i
        w.write(chr(write_byte))
        
        chunk = f.read(8)