import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = 0
L = list(map(int, input().split()))
for l in L:
    if l not in stack:
        stack.append(l)
    else:
        answer = max(len(stack), answer)
        stack = stack[stack.index(l)+1:len(stack)-stack[::-1].index(l)+1]
        stack.append(l)

print(max(len(stack), answer))








