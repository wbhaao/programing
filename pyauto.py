def solution(N, W):
    for i in range(N):
        lst = [0] * 26
        for j, w in enumerate(W):
            if i != j:
                lst[ord(w[0])-97] += 1
                lst[ord(w[-1])-97] -= 1
        cnt = 0
        for l in lst:
            if l != 0:
                cnt += abs(l)
        
        if cnt <= 3:
            return "Yes"
    return "No"
print(solution(6, ["apple","egg","graph","hi","busy","yield"]))