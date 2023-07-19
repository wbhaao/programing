'''
그래프 탐색을 써야한다
자식의 개수를 보고 더 적은 쪽으로 물을 보내는 방식
아니면 완전 탐색으로 dfs, bfs
위로 해보고 안되면 bfs 
'''

# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for i in range(1, M+1):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# q = deque()
# q.append((1, 100.0))
# # queue를 통해 우선순위 정하면서
# result = 0
# while q:
#     # 현재 노드를 대기열에서 삭제
#     index, amount = q.popleft()
#     # 주변 노드 있으면 대기열에 저장 (작은순)
#     for g in graph[index]:
#         q.append((g, 1/len(graph[index])))
#     if len(graph[index]) == 0:
#         result = max(result, amount)
# print(result)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((1, 100.0))
result = 0
while q:
    index, amount = q.popleft()
    if graph[index]:
        flow = amount / len(graph[index])
        for g in graph[index]:
            q.append((g, flow))
    else:
        result = max(result, amount)
print(round(result, 11))




