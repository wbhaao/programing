def solution(N, W):
    answer = []
    
    for i in range(N):
        WW = list(W)
        w = WW.pop(i)
        w_o = str(w)
        for j in range(N):
            isTrue = False
            for w2 in WW:
                if w[-1] == w2[0]:
                    w = str(w2)
                    WW.remove(w2)
                    isTrue = True
                    break
            if not isTrue and j%2==0:
                answer.append(w_o)
                break
            elif j%2==1:
                break
            
    return answer
print(solution(5, ["abc","chocolate","everyday","hi","essential"]))