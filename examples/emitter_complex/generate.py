#!/usr/bin/python3

'''
this script is the actual generator

This script needs to be VERY deterministic, that is the reason for the sort() below
since python hashes dont always enumerate in the same order.
'''

import sys # for stdin
import re # for match

getter_name='get'
setter_name='set'

d=dict()
last=None
for line in sys.stdin:
	if re.match('^\w+:\s*', line):
		line=line.rstrip()
		line=line[:-1]
		d[line]=dict()
		last=line
	if re.match('^\s+\w+:\w+\s*$', line):
		line=line.strip()
		k,v=line.split(':')
		d[last][k]=v
for k in sorted(d.keys()):
	v=d[k]
	c_file_name='gen/'+k+'.cc'
	h_file_name='gen/'+k+'.hh'
	with open(h_file_name, 'w') as f:
		f.write('class {0} {{\n'.format(k))
		f.write('private:\n'.format())
		for d_var in sorted(v.keys()):
			d_type=v[d_var]
			f.write('\t{1} {0};\n'.format(d_var, d_type, k));
		f.write('public:\n'.format())
		for d_var in sorted(v.keys()):
			d_type=v[d_var]
			f.write('\t{1} {2}{0}();\n'.format(d_var, d_type, getter_name));
			f.write('\tvoid {2}{0}({1});\n'.format(d_var, d_type, setter_name));
		f.write('}};\n'.format(k))
	with open(c_file_name, 'w') as f:
		f.write('#include "{0}"\n'.format(h_file_name))
		for d_var in sorted(v.keys()):
			d_type=v[d_var]
			f.write('{1} {2}::{3}{0}() {{\n'.format(d_var, d_type, k, getter_name));
			f.write('}}\n'.format(d_var, d_type, k));
			f.write('void {2}::{3}{0}({1} val) {{\n'.format(d_var, d_type, k, setter_name));
			f.write('}}\n'.format(d_var, d_type, k));
