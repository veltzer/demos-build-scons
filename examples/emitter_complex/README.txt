This example shows how a generator could generate many files and still get an incremental
build using scons.

Note that in this example the generator is not itself a build target (it is a python
script that requires no building).
that is why this example is called simple.

In real smartbuild the config for the scenario here will look like this:

	<module>
		<target type="bin" name="mygenerator">
			<source file="mygenerator.cc"/>
		</target>
		<target type="complex_generator" generator="mygenerator" output_list_generator="list_generated_files.py">
			<source file="generator_source.gen"/>
		</target>
	</module>
