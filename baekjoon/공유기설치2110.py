n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start = 1
end = array[-1] - array[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    current = array[0]
    # cnt = 설치된 라우터
    cnt = 1

    for i in range(1, len(array)):
        # mid이상으로 떨어진 거리에 route가 있나
        if array[i] >= current + mid:
            # 그쪽에 설치하고 current 바꿈
            cnt += 1
            current = array[i]
    # 다 설치 했다면 
    if cnt >= c:
        start = mid + 1
        answer = mid
    # mid가 너무 크다면
    else:
        end = mid - 1
print(answer)