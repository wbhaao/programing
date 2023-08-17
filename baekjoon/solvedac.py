import sys

input = sys.stdin.readline


def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
if not n:
    print(0)
else:
    diff = [int(input()) for _ in range(n)]
    diff.sort()
    expt = my_round(n * 0.15)

    if expt != 0:
        diff = diff[expt:-expt]
    cnt = n - 2 * expt
    result = sum(diff)
    print(my_round(result / cnt))
