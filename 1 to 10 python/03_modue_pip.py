# in python we have 2 type of module 
# 1 built in module = those modules are ready to import and use and ship with python interpreter.
# 2 external module = those modules are imported froma third party file or can be installed using a package manager like pip or conda.


import pandas  # this is a example of external module.
import hashlib # this is a example of built in module

print("hi")

pandas.read_csv("one.csv")
m = hashlib.sha256()
print(m)



'''
Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.

External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

The pip command
It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command
'''

#day 03 in python (ayaz)