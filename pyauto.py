def solution(N, W):
    answer = []
    for i in range(N):
        WW = list(W)
        w = WW.pop(i)
        while True:
            for w2 in WW:
                if w[-1] in w2:
                    w = str(w2)
                    WW.remove(w2)
                    break
            if w != w2:
            

    return answer
print(solution(5, ["abc","chocolate","everyday","hi","essential"]))