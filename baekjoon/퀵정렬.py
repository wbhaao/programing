numlist = [100, 9, 4, 45, 4, 10000, 123, 140, 9, 100]
count = [0] * 10001

# 누적합 구하기
for i in range(len(numlist)):
    count[numlist[i]] += 1

# 인덱스 데이터만 출력
for i in range(len(count)):
    for j in range(count[i]):
        print(i)