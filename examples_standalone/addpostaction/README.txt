This example shows how you can add a python function that will be
called after targets are built by scons.

This example shows that if you add post action to a binary say and expect it to add
the post action to anything deduced then you are wrong. If you want to create a binary
where you have a post action after each object file creation you have to do it explicitly.
