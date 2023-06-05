import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))

# x[2] 기준으로 정렬
Elist.sort(key=lambda x: x[2])
 
 
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
# s: 노드1, e: 노드2, w: 가중치
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        # 간선 연결
        if sRoot < eRoot:
            # sRoot는 eRoot와 연결되어있다
            Vroot[sRoot] = eRoot
        else:
            # eRoot는 sRoot와 연결되어있다
            Vroot[eRoot] = sRoot
        # 가중치 더하기
        answer += w
 
print(answer)