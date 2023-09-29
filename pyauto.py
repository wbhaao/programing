def solution(N, W):
    lst = [0] * 26
    answer = []
    sss = ""
    for w in W:
        lst[ord(w[0])-97] += 1
        lst[ord(w[-1])-97] -= 1
    cnt = 0
    for i, l in enumerate(lst):
        if l == 1:
            sss = chr(i+97)
            break
    for w in W:
        if w[0] == sss:
            answer.append(w)
    return answer