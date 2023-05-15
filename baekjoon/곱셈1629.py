a, b, c = map(int, input().split())
sum_ = 0
def foo(b):
    if b==1:
        return a
    else:
        return foo(b//2) * foo(b-b//2)
        
print(foo(b)%c)