import argparse
# Define the parser
parser = argparse.ArgumentParser()
# Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
parser.add_argument('-name', action="store", dest='name', default='p0')
# Now, parse the command line arguments and store the values in the `args` variable
args = parser.parse_args()
# Individual arguments can be accessed as attributes...
print str(args.name)