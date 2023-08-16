import sys


def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
    # == return int(num) + (1 if num - int(num) >= 0.5 else 0)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if not n:
        print(0)
    else:
        difficulty = [int(sys.stdin.readline()) for _ in range(n)]
        difficulty.sort()
        exception = my_round(n * 0.15)

        if exception != 0:
            difficulty = difficulty[exception:-exception]
        cnt = n - 2 * exception
        result = sum(difficulty)
        print(my_round(result / cnt))
