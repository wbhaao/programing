import heapq
T = int(input())

for i in range(T):
    N = int(input())
    h = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(N-1):
        a = heapq.heappop(h)+heapq.heappop(h)
        heapq.heappush(h, a)
        answer += a
    print(answer)