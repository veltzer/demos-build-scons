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
    if re.match(r'^\w+:\s*', line):
        line=line.rstrip()
        line=line[:-1]
        d[line]=dict()
        last=line
    if re.match(r'^\s+\w+:\w+\s*$', line):
        line=line.strip()
        k,v=line.split(':')
        d[last][k]=v
for k in sorted(d.keys()):
    v=d[k]
    c_file_name='gen/'+k+'.cc'
    h_file_name='gen/'+k+'.hh'
    with open(h_file_name, 'w') as f:
        f.write(f'class {k} {{\n')
        f.write(f'private:\n')
        for d_var in sorted(v.keys()):
            d_type=v[d_var]
            f.write(f'\t{d_type} {d_var};\n');
        f.write(f'public:\n')
        for d_var in sorted(v.keys()):
            d_type=v[d_var]
            f.write(f'\t{d_type} {getter_name}{d_var}();\n');
            f.write(f'\tvoid {setter_name}{d_var}({d_type});\n');
        f.write(f'}};\n')
    with open(c_file_name, 'w') as f:
        f.write(f'#include "{h_file_name}"\n')
        for d_var in sorted(v.keys()):
            d_type=v[d_var]
            f.write(f'{d_type} {k}::{getter_name}{d_var}() {{\n');
            f.write(f'}}\n');
            f.write(f'void {k}::{setter_name}{d_var}({d_type} val) {{\n');
            f.write(f'}}\n');
