import sys

input = sys.stdin.readline

N = int(input())
stack = []
for i in range(N):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))
