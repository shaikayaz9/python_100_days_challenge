#generators are diffrent from list ,are used in python to generate on the flies-values


def my_generator():
    for i in range(5):
        yield i
        

# its help us when we need a data its easy for readlibility & less memory

gen =my_generator()

print(next(gen)) #0
print(next(gen)) #1
print(next(gen)) #2
# print(next(gen)) #3
# print(next(gen)) #4 

