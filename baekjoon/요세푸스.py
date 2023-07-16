from collections import deque

queue = deque()
result = []

n, k = map(int, input().split())
# 입력
for i in range(1, n+1):
    queue.append(i)

while queue:
    # 순서 바꾸기!!!
    for i in range(k-1):
        queue.append(queue.popleft())
    # 정답 빼기
    result.append(queue.popleft())

# 출력
print("<",end='')
for i in range(len(result)-1):
    print(f"{result[i]}, ", end='')
print(result[len(result)-1], end='')
print(">")