import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
result = [0] * (n+1)

# 스택 초기화 (높이, 위치)
stack = []

for i in range(1, n+1):

    # Stack이 남았으면
    while stack:
        # 앞에 있는게 나보다 작다면
        if (arr[i] > stack[-1][0]):
            # Stack TOP 제거
            stack.pop()
        # 앞에있는게 나보다 크다면
        else:
            # 앞에서 주소 넣기
            result[i] = stack[-1][1]
            break
    # 현재 탑 정보 넣기
    stack.append((arr[i], i))

# 결과 출력
for i in range(1, n+1):
    print(result[i])