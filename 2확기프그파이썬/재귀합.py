lst = [1, 2, 3, 4, 5]
def foo(n):
    try:
        a = lst.pop()
        return foo(n+a)
    except:
        return n
print(foo(0))