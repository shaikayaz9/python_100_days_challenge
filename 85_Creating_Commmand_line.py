# Creating Coomand Line Utility in python

import argparse 

parser = argparse.ArgumentParser()


#add command line Argument
parser.add_argument("arg1",
help="description of argument 1")
parser.add_argument("arg2", 
help="description of argument 2")

# parse the argument
args = parser.parse_args()

print(args.arg1)
print(args.arg2)