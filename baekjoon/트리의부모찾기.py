import sys
sys.setrecursionlimit(10**6)

V = int(input())
graph = [[] for _ in range(V+1)]
result = [0]*(V+1)
# 그래프와의 관계를 나타냄
for _ in range(V-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_Path(curNode, parNode):
    for g in graph[curNode]:
        if g!=parNode:
            result[g] = curNode
            find_Path(g, curNode)
find_Path(1, 0)
for i in range(2, V+1):
    print(result[i])