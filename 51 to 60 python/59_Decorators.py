# Decorators in python

#modify our function statement
def greet(funx):
    def main_func():
        print("Good Morning")
        funx()
        print("Thanks for using this Function")
    return main_func

# @greet
def hello():
    print("hello world")

# hello()
greet(hello)()
