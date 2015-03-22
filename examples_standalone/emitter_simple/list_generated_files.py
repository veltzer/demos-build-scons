#!/usr/bin/python

# this is a script with no dependencies that knows how to get the source file and emit
# a list of the generated files.

from __future__ import print_function
import sys # for stdin
import re # for match

for line in sys.stdin:
	if re.match('^\w+:\s*', line):
		line=line.rstrip()
		line=line[:-1]
		print(line+'.c')
		print(line+'.h')
