N = int(input())
H = list(map(int, input().split()))
answer = [0] * N
for p in range(1, N+1):
    t = H[p-1]
    cnt = 0
    for i in range(N):
        if cnt == t and answer[i] == 0:
            answer[i] = p
            break
        elif answer[i] == 0:
            cnt += 1
print(*answer)