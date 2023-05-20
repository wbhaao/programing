import sys

# 탑의 수
n = int(sys.stdin.readline())
# 탑의 높이
arr = [0] + list(map(int, sys.stdin.readline().split()))
# 결과 배열
result = [0] * (n+1)

# 스택 초기화 (높이, 위치)
stack = []

for i in range(1, n+1):

    # Stack에 탑의 정보가 남아있다면
    while stack:
        # 현재 탐색하고 있는 탑의 높이가 Stack TOP의 높이보다 크다면
        if (arr[i] > stack[-1][0]):
            # Stack TOP 제거
            stack.pop()
        # 현재 탐색하고 있는 탑의 높이가 Stack TOP의 높이보다 작다면
        else:
            # 현재 탐색하고 있는 탑의 레이저를 수신 받을 수 있는 탑의 위치를 저장
            result[i] = stack[-1][1]
            break
    # 현재 탑의 정보를 Stack에 삽입
    stack.append((arr[i], i))

# 결과 출력
for i in range(1, n+1):
    print(result[i])