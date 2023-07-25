'''
siuuuuuuuuuuuuuuuuuuuuu
백트래"킹"
'''

N, M = list(map(int,input().split()))
incList = list(map(int,input().split()))
s = []
incList.sort()
def dfs():
    # else되면 숫자 추가
    if len(s) == M:
        print(" ".join(map(str, s))) 
        return
        # 찾았으니 가지치기
    # 추가할 숫자
    for i in incList:
        if i not in s:
            if s:
                if s[-1] < i:
                    s.append(i)
                    dfs()
                    s.pop()
            else:
                s.append(i)
                dfs()
                s.pop()
dfs() 