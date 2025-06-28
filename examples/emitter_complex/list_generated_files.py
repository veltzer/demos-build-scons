#!/usr/bin/python3

'''
this is a script with no dependencies that knows how to get the source file and emit
a list of the generated files.
'''

import sys # for stdin
import re # for match

for line in sys.stdin:
    if re.match(r'^\w+:\s*', line):
        line=line.rstrip()
        line=line[:-1]
        print('gen/'+line+'.cc')
        print('gen/'+line+'.hh')
