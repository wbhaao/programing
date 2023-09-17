'''
빙산 쉬운 버전
'''
from collections import deque
N = int(input())
lst = [[0] * (N+2)]
answer = []
for i in range(N):
    lst.append([0]+list(map(int, list(input())))+[0])
lst.append([0] * (N+2))
# print(lst)
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if lst[i][j] == 1:
            q = deque()
            q.append((i, j))
            lst[i][j] = 0
            cnt += 1
            answer.append(1)
            while q:
                y, x = q.popleft()
                for yy, xx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if lst[yy+y][xx+x] == 1:
                        q.append([yy+y, xx+x])
                        lst[yy+y][xx+x] = 0
                        answer[-1] += 1
print(len(answer))
for i in sorted(answer):
    print(i)




