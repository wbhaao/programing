import sys
sys.setrecursionlimit(10**6)
k = int(input())


def DFS(start, visited, graph, group):
    visited[start] = group  # 현재 노드의 그룹 저장

    # 인접 노드 탐색
    for v in graph[start]:
        if visited[v] == 0:
            result = DFS(v, visited, graph, -group)
            if not result:
                return False
        else:
            if visited[v] == group:
                return False
    return True

# k 번 반복
for _ in range(k):
    # 정점 개수, 간선 개수
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        # 각 정점 추가
        a, b = map(int, sys.stdin.readline().split())
        # 정점 연결
        graph[a].append(b)
        graph[b].append(a)
    # 정점끼리 탐색
    for i in range(1, V+1):
        # 방문하지 않았다면 (DFS도중 방문할 수 있음)
        if visited[i] == 0:
            result = (DFS(i, visited, graph, 1))
            if not result:
                break
    if result: 
        print("YES") 
    else: 
        print("NO")