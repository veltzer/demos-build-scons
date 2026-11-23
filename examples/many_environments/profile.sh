#!/bin/bash
scons_path=$(command -v scons)
{ python2 -m cProfile -s cumtime "${scons_path}" 2> /dev/null || true; } | head -n 20
