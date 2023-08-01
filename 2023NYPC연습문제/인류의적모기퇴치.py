'''
컷!!!!!!!!!!!
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
answer = 0

def findMosOfNum(y, x, _arr):
    try:
        if y < 0 or x < 0:
            return 0
        return _arr[y][x]
    except:
        return 0
for i in range(N):
    arr[i] = list(map(int, input().split()))
# [i//N][i%N]
for i in range(N**2):
    pos = [i//N, i%N]
    cross = arr[pos[0]][pos[1]]
    straight = arr[pos[0]][pos[1]]
    for j in range(-M, M+1):
        if j==0:
            continue
        straight += findMosOfNum(pos[0]+j, pos[1], arr)
        straight += findMosOfNum(pos[0], pos[1]+j, arr)
        cross += findMosOfNum(pos[0]+j, pos[1]+j, arr)
        cross += findMosOfNum(pos[0]-j, pos[1]+j, arr)
    cross = max(cross, straight)
    answer = max(cross, answer)
print(answer)

