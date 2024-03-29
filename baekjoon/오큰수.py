import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []
# 비교당할 애
stack.append(0)
# 1부터 n-1까지
for i in range(1, n):
    while stack and A[i] > A[stack[-1]]:
        answer[stack.pop()] = A[i]
    stack.append(i)
print(*answer)