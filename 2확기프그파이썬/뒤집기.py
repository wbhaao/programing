lst = [1, 2, 3, 4, 5]
def foo():
    try:
        foo()
        print(lst.pop())
    except:
        pass
foo()
