'''
siuuuuuuuuuuuuuuuuuuuuu
백트래"킹"
'''

n,m = list(map(int,input().split()))

s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    for i in range(1, n+1):
        if s:
            if s[-1] <= i:
                s.append(i)
                dfs()
                s.pop()
        else:
            s.append(i)
            dfs()
            s.pop()

dfs()