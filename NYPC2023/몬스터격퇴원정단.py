'''
몬스터랑 1ㄷ1로 대응된다..! (두둥!) ㄴ(0ㅁ0)ㄱ
'''
import copy
import sys

read = sys.stdin.readline
N, M = map(int, input().split())
monsters = []
heros = []
answer = ""
for i in range(N):
    monsters.append(list(map(int, input().split())))

monsters_temp = copy.deepcopy(monsters)

for i in range(M):
    heros.append(list(map(int, input().split())))

for i in range(M-N+1):
    monsters = copy.deepcopy(monsters_temp)
    for h in heros[i:i+N]:
        index = 0
        while True:
            deal = copy.deepcopy(h[1])
            if h[0] == monsters[index][0]:
                deal = int(deal/2)
            if monsters[index][1] - deal <= 0:
                del monsters[index]
                break
            else:
                index += 1
                if len(monsters) <= index:
                    break
    if len(monsters) == 0:
        answer += "1"
    else:
        answer += "0"
print(answer)