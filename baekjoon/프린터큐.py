from collections import deque

T = int(input())

for _ in range(T):
    N, index = map(int, input().split())
    queue = deque()
    lstlst = []
    lst = list(map(int, input().split()))
    for i in range(N):
        queue.append((i, lst[i]))
        lstlst.append(lst[i])
    cnt = 1
    while True:
        ind, value = queue.popleft()
        if queue and value < max(lstlst):
            queue.append((ind, value))
        else:
            lstlst.remove(max(lstlst))
            if ind == index:
                print(cnt)
                break
            cnt += 1
