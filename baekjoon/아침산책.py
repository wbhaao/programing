'''
중간에 실외가 껴있다. += 2
실내끼리만 있다 += 1
'''
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
V = int(read())
inOut = list(map(int, list(read())[:-1]))
inOut.insert(0, 0)
# [[], [2], [3, 4], [], [5], []]
tree = [[0] * (0) for _ in range(V + 1)] 
visited = [0] * (V+1)
result = 0
for i in range(V-1):
    N, M = map(int, read().split())
    tree[N].append(M)
    tree[M].append(N)
'''
어떻게 하느냐?
몰랴
'''
def DFS(cur, visited, tree, parNode):
    global result
    for t in tree[cur]:
        if inOut[t] == 1 and t!=parNode:
            result += 1
        elif inOut[t] == 0:
            DFS(t, visited, tree, cur)
for index, inO in enumerate(inOut):
    if inO == 1:
        DFS(index, visited, tree, 0)
print(result)