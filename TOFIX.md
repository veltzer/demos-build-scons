# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `examples/check_libraries_after_creation/SConstruct:11` - Python 2 `print "making", ...` statement is a SyntaxError under the Python 3 scons declared in `pyproject.toml`; since this example has no `SKIP.txt`, the aggregate `examples/SConstruct` (which `SConscript`s every non-skipped `*/SConstruct`) dies on it. Change to `print("making", target[0], "from", source)`. The same statement is in `SConstruct.old:11` - fix it or delete the stale `.old` file.
- `examples/emitter_simple/SConstruct:30` and `examples/emitter_complex/SConstruct:30` - `subprocess.check_output()` returns `bytes` in Python 3, so `out.rstrip()` / `out.split('\n')` on lines 33-37 raise `TypeError` and the emitter never works (both examples are currently hidden behind `SKIP.txt`). Pass `text=True` to `check_output`, then remove the `SKIP.txt` files if the examples build.

## Medium

- `rsconstruct.toml` - the repo has Python sources (`examples/**/*.py`, `examples_standalone/embed_scons/my_scons.py`, every `SConstruct`) and declares `ruff`/`mypy` in `pyproject.toml:52-54`, but there is no `[processor.ruff]`, so none of it is linted; `ruff check` currently reports 21 findings (e.g. F541 f-strings without placeholders at `examples/emitter_simple/generate.py:34,38,43,49,51`, I001 import order, C408 `dict()`). Add a ruff processor over the folders that hold the `.py` files and fix the findings. Either add a pytest/mypy use or drop the unused `pytest`/`mypy` dev deps.
- `examples/many_environments/mytest.py:1` and `examples/many_environments/profile.sh:2` - hardcode `python2`, which no longer exists on current distros; switch to `python3` (and in `profile.sh` profile the venv's `scons`).
- `examples_standalone/embed_scons/my_scons.py:10` - inserts `/usr/lib/scons` (Debian package path) into `sys.path`, but the repo installs scons from PyPI into `.venv`; the path is wrong there and the hack is unnecessary. Drop the `sys.path.insert` and use `#!/usr/bin/env python3` instead of `#!/usr/bin/python` (line 1).
- `examples/decider_c_cpp/README.txt` - the example directory holds only a README describing a comment-insensitive decider; there is no `SConstruct` or source. Implement the example or remove the directory.

## Low

- `examples/many_source_files/REAMDME.txt` - filename typo; rename to `README.txt` like every other example.
- `examples/*/SConstruct` - every SConstruct still starts with `from __future__ import print_function` (e.g. `examples/SConstruct:1`), a Python 2 leftover that is a no-op on the Python 3.14 the repo requires; remove it.
- `README.md:1-2` - one-line README with no list of the examples, how to run them (`cd examples && scons`), or what `SKIP.txt` means.
