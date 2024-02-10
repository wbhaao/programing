T = int(input())

for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int,input().split()))

    s_lst = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        s_lst[i] = s_lst[i-1] + lst[i]
    # print('s_lst',s_lst)

    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(2, N+1):
        for j in range(1, N+2-i):
            # 여러 조합중 하나
            # j 는 공통으로 들어감
            dp[j][j+i-1] = min([dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)]) 
            dp[j][j+i-1] += (s_lst[j+i-1] - s_lst[j-1])

            # print('--------------------')
            # print('test :' , [dp[j][j+q] + dp[j+q+1][j+i-1] for q in range(i-1)])
            # print('i :' ,i,'j :',j)
            # print('s_lst : ',s_lst)
            #for x in dp:
            #    print(x)

    print(dp[1][N])