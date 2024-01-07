'''
비트마스크 문제이니
숫자를 2진법으로 변환해 풀이한다

그렇게 BFS를 사용해 방의 크기를 구함
벽에 막힐 때 인접한 방을 알기 위해 
막힌 벽 너머도 조사
각 방의 좌표마다 그 좌표에 해당하는 방의 크기를 줄것
그래서 인접한 방의 크기를 한번에 알 수 있음
그 조합이 가장 큰것이 3번 답

이중포문 돌아야함
bfs 써야함
'''

from collections import deque

cnt, max_size, size = 0, 0, 0

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

room_value_list = [0]

for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
            q = deque()
            q.append((i, j))
            visited[i][j] = cnt
            size = 1
            while q:
                y, x = q.popleft()
                # 남동북서
                for s, iy, ix in zip(list(bin(lst[y][x])[2:].zfill(4)), [y+1, y, y-1, y], [x, x+1, x, x-1]):
                    if 0 <= iy < M and 0 <= ix < N and s == "0" and visited[iy][ix] == 0:
                        size += 1
                        visited[iy][ix] = cnt
                        q.append((iy, ix))
            room_value_list.append(size)
            max_size = max(max_size, size)

two_room = max_size

for i in range(M):
    for j in range(N): 
        if i+1 < M and visited[i+1][j] != visited[i][j]:
            two_room = max(room_value_list[visited[i][j]]+room_value_list[visited[i+1][j]], two_room)
        if j+1 < N and visited[i][j+1] != visited[i][j]:
            two_room = max(room_value_list[visited[i][j]]+room_value_list[visited[i][j+1]], two_room)

print(f"{cnt}\n{max_size}\n{two_room}")