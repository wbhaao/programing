N, M = map(int, input().split())
answer = 0
while N>=M:
    answer += N // M
    N = N % M + N // M

print(answer)