#!/usr/bin/python3

import base64
import sys

def encode(filename):
    with open(filename, "r") as f:
        s = f.readline().strip()
        return base64.b64encode((''.join([chr(ord(s[x])+([5,-1,3,-3,2,15,-6,3,9,1,-3,-5,3,-15] * 3)[x]) for x in range(len(s))])).encode('utf-8')).decode('utf-8')[::-1]*5

def mine(filename):
    output = ''
    l = [5,-1,3,-3,2,15,-6,3,9,1,-3,-5,3,-15] * 3
    with open(filename, "r") as f:
        s = f.readline().strip()
        for i in range(len(s)):
            output += chr(ord(s[i]) + l[i])

    return base64.b64encode(output.encode('utf-8')).decode('utf-8')[::-1] * 5

def reverse(string):
    print("decoding " + string)
    l = [5,-1,3,-3,2,15,-6,3,9,1,-3,-5,3,-15] * 3

    string = string[0:len(string)//5] # reduce to one instance
    string = string[::-1] # de-reverse
    string = base64.b64decode(string).decode('utf-8') # de-base64

    output = ''
    for i in range(len(string)):
        output += (chr(ord(string[i]) - l[i]))

    return output

filename = sys.argv[1]

print(encode(filename))
print(mine(filename))

print(reverse(mine(filename)))