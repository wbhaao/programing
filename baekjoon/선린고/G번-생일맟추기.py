import sys
input = sys.stdin.readline
N = int(input())
cal = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(N):
    cnt = 0
    lst = list(map(int, input().split()))
    # 12월 i:월을 나타냄
    for i in range(1, 13):
        isPass = True
        # 12월 중 포함된게 있는지 k:월 letter
        for k in str(i):
            if lst[int(k)]==1:
                isPass = False
        if isPass:
            # j : 일
            for j in range(1, cal[i-1]+1):
                # s: 일 letter
                plus = 1
                for s in str(j):
                    if lst[int(s)]==1 :
                        plus = 0
                        break
                cnt += plus
    print(cnt)