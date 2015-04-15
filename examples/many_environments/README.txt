This example shows that creating scons environments takes time.

The python executable (mytest.py) shows that this is probably a scons(1) bug since
it does something similar and runs 100x faster.

Note that as the SConstruct shows, nulling the scons default tool set does
not help for this issue.

deepcopy does not work for scons Envs!!!.
