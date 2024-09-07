#local & global veriable

x = 4
print(x)


def hello():
    global x #global keyword
    x = 7
    print(x +6)

    print("hello bro")

print(x)
hello()