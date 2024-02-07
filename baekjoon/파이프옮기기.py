'''
DP문제는 설계가 제일 중요한데
이차원 배열을 만들고 갈 수 있는 경우를 카운트 해보자
'''
from collections import deque
N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]
# d: 0 가로, 1 세로, 2 대각선
q = deque()
q.append((0, 1, 0))
answer = 0

while q:
    c, r, d = q.popleft()
    if r+1 == N and c+1 == N:
        answer += 1
        continue
    if d == 0:
        # 오른쪽방향이면
        if r+1 < N and dp[c][r+1] == 0:
            q.append((c, r+1, 0))
        if r+1 < N and c+1 < N and dp[c+1][r+1] == 0 and dp[c][r+1] == 0 and dp[c+1][r] == 0:
            q.append((c+1, r+1, 2))
    elif d == 1:
        # 아래쪽방향이면
        if c+1 < N and dp[c+1][r] == 0:
            q.append((c+1, r, 1))
        if r+1 < N and c+1 < N and dp[c+1][r+1] == 0 and dp[c][r+1] == 0 and dp[c+1][r] == 0:
            q.append((c+1, r+1, 2))
    elif d == 2:
        # 대각쪽방향이면
        if c+1 < N and dp[c+1][r] == 0:
            q.append((c+1, r, 0))
        if r+1 < N and dp[c][r+1] == 0:
            q.append((c, r+1, 1))
        if r+1 < N and c+1 < N and dp[c+1][r+1] == 0 and dp[c][r+1] == 0 and dp[c+1][r] == 0:
            q.append((c+1, r+1, 2))
print(answer)

