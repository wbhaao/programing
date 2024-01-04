'''
연결 요소 : 간선으로 연결된 노드 묶음
BFS를 통해 연결 요소를 세면 된다

이차원 배열에 연결된 노드를 넣는다

'''
from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
visited = [0]*(N+1)
lst = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

q = deque()
cnt = 0

for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        q.append(i)
        visited[i] = 1
        while q:
            vv = q.popleft()
            for l in lst[vv]:
                if visited[l] == 0 and l not in q:
                    q.append(l)
                    visited[l] = 1

print(cnt)

'''
다른 사람의 풀이

그냥 DFS인거 뺴고 다 똑같다

import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    

visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(i)
        
print(count)
'''