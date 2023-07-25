'''
siuuuuuuuuuuuuuuuuuuuuu
백트래"킹"
'''

N, M = list(map(int,input().split()))

s = []
 
def dfs():
    # else되면 숫자 추가
    if len(s) == M:
        print(" ".join(map(str, s)))
        # 찾았으니 가지치기
        return
    # 추가할 숫자
    for i in range(1, N+1):
        # 안들어있으면
        s.append(i)
        # 추가 or 출력
        dfs()
        # 출력했으면 pop
        s.pop()
dfs() 