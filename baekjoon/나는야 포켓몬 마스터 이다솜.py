from sys import stdin
def input():
    return stdin.readline().rstrip()

N, M = map(int, input().split())
by_id = {}
by_name = {}

for i in range(1, N + 1):
    pokemon = input()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(M):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])