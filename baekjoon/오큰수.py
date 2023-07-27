import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []
# 비교당할 애
stack.append(0)
# 1부터 n-1까지
for i in range(1, n):
    # stack이 남아있고, 맨 뒤 스택보다 비교할 애가 더 크면
    while stack and A[stack[-1]] < A[i]:
        # 오큰수 찾은거 
        answer[stack.pop()] = A[i]
    # 비교한애 오큰수도 찾게 append
    stack.append(i)

print(*answer)