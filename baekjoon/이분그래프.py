from collections import deque
import sys
read = sys.stdin.readline
color = 0
cnt = read()
for i in range(cnt):
    # 정점 개수, 간선 개수
    n, m = map(int, read().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)] 
    # [visited, color]
    # red : 0, blue : 1
    visit_list2 = [0,0] * (n + 1)
    for z in range(m):
        a, b = map(int, read().split())
        graph[a][b] = 1
        graph[b][a] = 1
        
    q = deque(1)
    visit_list2[0] = [1, color]
    
    # queue를 통해 우선순위 정하면서
    while q:
        # 현재 노드를 대기열에서 삭제
        vv = q.popleft()
        # 현재 노드 출력
        print(vv, end=" ")
        # 주변 노드 있으면 대기열에 저장 (작은순)
        for z in range(1, n+1):
            if color == visit_list2[z][1]:
                break
            if graph[vv][z] == 1 and visit_list2[z][0]==0:
                q.append(z)
                visit_list2[z] = 1
    # color 반전
    color ^= 1