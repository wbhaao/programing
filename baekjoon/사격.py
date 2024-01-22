import sys
from bisect import bisect_right

n, m, a = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
s.sort()
left, right = 1, max(s)

while left < right:
    mid = (left + right) // 2
    idx = bisect_right(s, mid)
    if idx == n:
        total = sum(s) + (m-n)*s[-1]
    else:
        total = sum(s[idx:]) + (m-n+idx)*s[idx-1]
    if total >= a:
        right = mid
    else:
        left = mid + 1
print(left)
