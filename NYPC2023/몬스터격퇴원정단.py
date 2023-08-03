'''
몬스터랑 1ㄷ1로 대응된다..! (두둥!) ㄴ(0ㅁ0)ㄱ
'''
import copy
from collections import deque
import sys

read = sys.stdin.readline

N, M = map(int, input().split())

monsters = []
heros = []
for i in range(N):
    monsters.append(list(map(int, input().split())))
monsters.sort(key = lambda x :(x, x[1]))
monsters_temp = monsters.copy()
for i in range(M):
    heros.append(list(map(int, input().split())))

for i in range(M-N+1):
    monsters = monsters_temp.copy()
    for h in heros[i:i+N]:
        index = 0
        while True:
            deal = int(h[1])
            if h[0] == monsters[index][0]:
                deal /= 2
            if monsters[index][1] <= deal:
                del monsters[index]
                break
            else:
                index += 1
                if len(monsters) <= index:
                    break
    if len(monsters) == 0:
        print("1", end="")
    else:
        print("0", end="")