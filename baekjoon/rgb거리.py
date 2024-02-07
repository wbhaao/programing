'''
1번집은 2번집과 달라야한다
N번집은 N-1번집과 달라야한다
i번째 집은 i-1, i+1과 달라야한다

각 줄에는 각 집을 빨강 파랑 초록으로 칠하는 비용이 주어진다
바텀업 방식으로 풀이한다면

식을 만든다면
dp[0] = min(lst[0])
dp[1] = min(dp[0]+)
'''

from sys import stdin
input = stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
    
for i in range(1, N): 
    lst[i][0]= min(lst[i-1][1],lst[i-1][2]) + lst[i][0]
    lst[i][1]= min(lst[i-1][0],lst[i-1][2]) + lst[i][1]
    lst[i][2]= min(lst[i-1][0],lst[i-1][1]) + lst[i][2]

print(min(lst[N-1][0],lst[N-1][1],lst[N-1][2]))