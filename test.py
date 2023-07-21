from collections import deque
a = int(input())
lst = []
visited = [False] * (a**2)
result = 0
for i in range(a):
    lst.append(list(map(int, input().split())))
q = deque()
nebo = 0
for y in range(a):
    for x in range(a):
        if lst[y][x] == 1 and visited[y*a+x]==False:
            q.append((y, x))
            visited[y*a+x] = True
            nebo += 1
            while q:
                cy, cx = q.popleft()
                for yi, xi in ((-1, 1), (1, 1), (-1, -1) ,(1, -1)):
                    if cy+yi<0 or cx+xi<0 or cy+yi>=a or cx+xi>=a:
                        continue
                    if lst[cy+yi][cx+xi] == 1 and visited[(cy+yi)*a+cx+xi]==False:
                        q.append((cy+yi, cx+xi))
                        nebo += 1
            if nebo == 3:
                result += 1
            nebo = 0
            q = deque()