#!/usr/bin/python2

'''
this tests to see how long it takes to clone python hashes
'''

# create a "fat" dictionary with 1000 key,value pairs...
d=dict()
for x in range(1000):
	d[str(x)]=str(x)

# now clone the dictionary 10,000 times...

for x in range(10000):
	e=d.copy()
