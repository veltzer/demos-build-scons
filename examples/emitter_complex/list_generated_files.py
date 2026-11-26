#!/usr/bin/env python

'''
this is a script with no dependencies that knows how to get the source file and emit
a list of the generated files.
'''

import re  # for match
import sys  # for stdin

for line in sys.stdin:
    if re.match(r'^\w+:\s*', line):
        name=line.rstrip()[:-1]
        print('gen/'+name+'.cc')
        print('gen/'+name+'.hh')
