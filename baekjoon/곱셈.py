A, B, C = map(int, input().split())

def foo(a, c):
    return foo(a % c) + foo(a % c) % C

print(foo(A, C))