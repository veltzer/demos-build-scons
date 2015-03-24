This example shows how to write a custom builder.
In this case the builder is used to compress javascript.

NOTES:
- you can add builders using the two following syntax variations:
		env=Environment(BUIDLERS={ [your builders here]})
	or with this:
		env.Append(BUILDERS={ 'Compress': compress_builder })
