#!/usr/bin/python3

w = open('mask', 'w')

maskp = 'onion'

with open('onion3.txt', 'rb') as f:
    c = f.read(5)
    while len(c) == 5:
        for j in range(0, 5):
            w.write(chr(ord(maskp[j]) & c[j]))
        c = f.read(5)