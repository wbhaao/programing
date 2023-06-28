A = int(input())

for i in range(A):
    top = 0
    B = list(map(int, input().split()))
    del B[0] # 1번째는 순서라 삭제
    for i in B:
        if i > sum(B) / len(B):
          top += 1
    print("{0}%".format(format(round(top / len(B) * 100, 3), '.3f')))