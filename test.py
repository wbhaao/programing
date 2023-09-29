def solution(X, H, Y):
    cnt = 0
    week = X-1 # 0 ~ 6
    HH = [0] * 1000000
    pay = []
    nopay = []
    lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index, i in enumerate(H):
        HH[index] += i[1] - lst[i[0]-1]
        for j in range(i[0]):
            HH[index] += lst[j]
    for i in range(1, 366):
        week = (week)%7
        if week == 5 or week == 6:
            cnt += 1
            nopay.append(i)
        if i in HH:
            cnt += 1
            nopay.append(i)
        week += 1
    may = 0
    for i in range(12):
        iflst = []
        for j in range(1, Y+1):
            j += sum(lst[0:i])
            if j not in nopay:
                may = j-sum(lst[0:i])
                iflst.append(may)
        if may != 0:
            for k in range(Y+1, Y+1+(Y-may)): 
                k += sum(lst[0:i])    
                if k not in nopay:
                    may = k-sum(lst[0:i])    
                    iflst.append(may)
        for j in range(Y+1, lst[i]+1): 
            j += sum(lst[0:i])    
            if j not in nopay:
                may = j-sum(lst[0:i])
                iflst.append(j)
        if iflst:
            min_ = 100
            for i in iflst:
                if abs(min_-Y) > abs(i-Y):
                    min_ = i
            pay.append(min_)
        else:
            pay.append(Y)
    return pay
print(solution(7, [[1,1],[1,21],[1,22],[1,23],[3,1],[5,5],[5,27],[6,6],[8,15],[9,28],[9,29],[9,30],[10,3],[10,9],[12,25]], 5))