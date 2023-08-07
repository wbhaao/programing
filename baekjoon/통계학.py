import math
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

print(round(sum(lst) / len(lst)))
print(lst[len(lst) // 2])

temp = Counter(lst).most_common()
if len(lst) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

print(max(lst) - min(lst))
