#!/usr/bin/python3

'''
this script is the actual generator
'''

import sys # for stdin
import re # for match

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
		k,v = line.split(':')
		d[last][k]=v
for k, v in d.items():
	h_file_name='gen/'+k+'.h'
	c_file_name='gen/'+k+'.c'
	with open(c_file_name, 'w') as f:
		f.write('#include "{0}.h"\n'.format(h_file_name))
		f.write('class {0} {{\n'.format(k))
		f.write('private:\n'.format())
		for d_var, d_type in v.items():
			f.write('\t{0}:{1}\n'.format(d_var, d_type));
		f.write('}};\n'.format(k))
	with open(h_file_name, 'w') as f:
		f.write('#include "{0}.h"\n'.format(h_file_name))
		f.write('class {0} {{\n'.format(k))
		f.write('private:\n'.format())
		for d_var, d_type in v.items():
			f.write('\t{0}:{1}\n'.format(d_var, d_type));
		f.write('}};\n'.format(k))
