import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())

lst = [[] for _ in range(N+1)]

result = [0] * (N+1)
indegree = [0] * (N+1)

for i in range(M):
    A, B, C = map(int, input().split())
    lst[A].append([B, C])  
    indegree[B] += 1
q = deque()
q.append((N, 1))

while q:
    # maybe 7
    now, count = q.popleft()
    # i : now를 만들기 위해 필요한 부품들
    # i[0]:부품번호, i[1]:필요개수
    for i in lst[now]:
        # 계산할꺼니까 제거
        indegree[i[0]] -= 1
        # 필요한 부품의 하위 부품 (자식자식)
        for k in lst[i[0]]:
            # 필요한 개수만큼 하위 부품 곱하기
            k[1] *= count
        # 다 계산했으면 퇴장
        if indegree[i[0]] == 0:
            for z in lst[i[0]]:
                result[z[0]] += z[1]
            q.append((i[0], i[1]))
print(result)