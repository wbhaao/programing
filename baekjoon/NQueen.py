import sys
input = sys.stdin.readline
N = int(input())

result = 0
lst = [0] * N

def is_promising(x):
    for i in range(x):
        # 가로에 같은게 있는지, 대각선에 같은게 있는지
        if lst[x] == lst[i] or abs(lst[x] - lst[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global result
    if x == N:
        result += 1
        return
    else:
        for i in range(N):
            # [x, i]에 퀸을 놓겠다.
            lst[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(result)