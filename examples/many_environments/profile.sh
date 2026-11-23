#!/bin/bash
python2 -m cProfile -s cumtime "$(command -v scons)" 2> /dev/null | head -n 20
