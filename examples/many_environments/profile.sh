#!/bin/bash
python2 -m cProfile -s cumtime `which scons` 2> /dev/null | head -n 20
