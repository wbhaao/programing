import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * (N)
stack = []
result = []
cnt = 1
for i in range(N):
    lst[i] = int(input())
for i in range(N):
    while lst[i] >= cnt:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    if stack[-1]==lst[i]:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit()
for r in result:
    print(r)
