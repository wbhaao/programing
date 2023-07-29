'''
이것도 for문을 쓸 수 있다

아니 정답이랑 진짜 비슷한데
\안아ㅑㅐㅁㄴ0[ㅇ마내ㅔ암내ㅔ아
이중 for문 써볼껄러러러럭ㅇ러]

답지 슬쩍 보긴 했는데 암튼 품
어케풀었지
경우의수 메모이제이션으로 저장해서 품
'''
N = int(input())
lst = list(map(int, input().split()))
dp = [0] * 100001
for i in range(1, N+1):
    dp[i] = lst[i-1]
for i in range(2, N+1):
    for j in range(1, i):
        dp[i] = max(dp[j]+dp[i-j], dp[i])
print(dp[N])














