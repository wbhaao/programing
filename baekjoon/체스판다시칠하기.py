n, m = map(int, input().split())
ground = []
result = []
 
for i in range(n):
    ground.append(input())
# 완전탐색
for i in range(n-7):
    for j in range(m-7):
        caseB = 0
        caseW = 0 
        # B를 색칠할 경우
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 격자로 탐색1
                if (a + b) % 2 == 0:
                    # B로 시작하는 격자
                    if ground[a][b] != 'B':
                        caseB += 1
                    # W로 시작하는 격자
                    if ground[a][b] != 'W':
                        caseW += 1
                # 격자로 탐색2
                else:
                    # W로 시작하는 격자
                    if ground[a][b] != 'W':
                        caseB += 1
                    # B로 시작하는 격자
                    if ground[a][b] != 'B':
                        caseW += 1

        result.append(caseB)
        result.append(caseW)
 
print(min(result))