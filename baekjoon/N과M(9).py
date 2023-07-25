'''
siuuuuuuuuuuuuuuuuuuuuu
백트래"킹"
'''

N, M = list(map(int,input().split()))
incList = list(map(int,input().split()))
incList.sort()
incList_temp = list(incList)
s = []
def dfs():
    # else되면 숫자 추가
    if len(s) == M:
        print(" ".join(map(str, s))) 
        return
        # 찾았으니 가지치기
    # 추가할 숫자
    for i in incList:
        # 안들어있으면
        if i in incList_temp:
            incList_temp.remove(i)
            s.append(i)
            # 추가 or 출력
            dfs()
            # 출력했으면 pop
            incList_temp.append(s.pop())
dfs() 