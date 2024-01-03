from collections import deque

N = int(input())
size = 2
grow_cnt = 0
time = 0

lst = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def find_shark(lst):
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 9:
                return [i, j]
            
dump1 = find_shark(lst)
q = deque()
q.append([dump1[0], dump1[1], 0])

while q:
    dump2 = q.popleft()
    i, j, k = dump2[0], dump2[1], dump2[2]
    for y, x in [[i+1, j], [i, j-1], [i-1, j], [i, j+1]]:
        if 0 <= y < N and 0 <= x < N and visited[y][x] == 0:
            visited[y][x] = 1
            # 물고기 먹을 수 있으면
            if lst[y][x] == 0:
                q.append([y, x, k+1])
            elif lst[y][x] < size:
                grow_cnt += 1
                # 사이즈 수 만큼 물고기를 먹었다면
                if grow_cnt == size:
                    size += 1
                    grow_cnt = 0
                q = deque()
                visited = [[0] * N for _ in range(N)]
                time += k+1
                lst[y][x] = 0
                q.append([y, x, 0])
            # 물고기를 먹을 수 없으면
            elif lst[y][x] >= size:
                pass

print(time)

