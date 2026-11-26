#!/usr/bin/env python

import sys  # for path

# print something to see that we are ok...
print('here we are before scons...')

# /usr/lib/scons is where scons code is according to dpkg(1)
sys.path.insert(0, '/usr/lib/scons')

# now run scons
import SCons.Script  # noqa: E402  teaching: the import must come after the sys.path change above

SCons.Script.main()
