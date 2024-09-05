# finally key words run alwyas if use return statement also its run always print

def func1():
    try:
        i = int(input("Enter new values : "))
        l = [ 1,2,4,56]
        print(l[i])
    except:
        print("Some error occurred")
        return 0


    finally:
     print("hello bhai i am alwyas run")

x = func1()
print(x)