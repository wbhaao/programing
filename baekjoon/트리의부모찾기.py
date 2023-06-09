import sys
sys.setrecursionlimit(10**6)

V = int(input())
graph = [[] for _ in range(V+1)]
visited = [0]*(V+1)
visited[0] = 1
cur = 2
print(graph)
# 그래프와의 관계를 나타냄
for _ in range(V-1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def find_Path(curNode, parNode):
    # curNode : 현재 노드
    # i : 연결노드
    
    for i in range(1, V+1):
        global cur
        if graph[curNode][i]==1 and visited[i]==0 and i!=parNode:
            if i == cur:
                cur+=1
                # visited[i] = 1
                print(curNode)
                find_Path(i, curNode)
            else:
                find_Path(i, curNode)
while cur<=V:
    find_Path(1, 0)
