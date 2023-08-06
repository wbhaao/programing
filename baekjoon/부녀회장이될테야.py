"""
dp 아님??
"""

import sys

sys.setrecursionlimit(10**6)
read = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(read())  # 층
    n = int(read())  # 호
    people = [i for i in range(1, n + 1)]
    for x in range(k):
        for y in range(1, n):
            people[y] += people[y - 1]
    print(people[-1])
