'''
W[i][j] 값은 i에서 j로 가기 위한 값이다
이때 최솟값으로 1,2,3,4를 순회하고 돌아오는 방법
순서 상관 X

백트래킹 + DFS를 통해 풀어야함
DFS로 하나의 경우의 수를 만들고 그 경우의 값보다
높게 나온다면 가지치기한다

min_value
dfs
sys
'''
'''from sys import stdin
from sys import maxsize
N = int(stdin.readline())

lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

min_value = maxsize

# 행에 대한 visited
notVisit = [i for i in range(N)]
def dfs(notV, root, value):
    global min_value
    notV.remove(root)
    # print(root)
    if value > min_value:
        return
    for v in notV:
        if lst[root][v] != 0:
            dfs(list(notV), v, value+lst[root][v])
    # 틀린 이유 : ROOT에서 0번지로 가는 VALUE 검사를 하지 않음(0이여도 통과되게 했다)
    if notV == [] and lst[root][0]:
        # print(value+lst[-1][0])
        min_value = min(value+lst[root][0], min_value)
dfs(list(notVisit), 0, 0)
print(min_value)
'''
'''
어떻게 풀었지
아이디어가 빨리 나와서 쉽게 푼 것 같다

백트랙킹 미적용 코드 : 416ms
백트랙킹 적용 코드 : 56ms
'''

'''
다른 사람 풀이
import sys


def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
profile


얘꺼 성능개선해서 아래꺼 됨
150ms 대
->
56ms 로 변신
'''

import sys

def dfs(start, now, value, cnt, visited):
    global ans
    visited[now] = 1
    if cnt == N: # N칸 다 돌았으면
        if a[now][start]: # 내 코드에도 똑같은 if 있음 if ... lst[root][0]
            value += a[now][start] #  시작으로 돌아가는 값
            if ans > value:
                ans = value
        return

    if value > ans: # 도중에도 ans가 value보다 크면
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            dfs(start, i, value + a[now][i], cnt + 1, list(visited))

N = int(input())
a = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
dfs(0, 0, 0, 1, list(visited))
print(ans)