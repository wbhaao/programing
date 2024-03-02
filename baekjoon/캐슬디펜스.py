'''
브루트포스 문제이다
BFS 써서 풀면 될듯
N + 1 행에는 모든 칸에 성이 있음

0 0 0
0 0 0
0 0 0
성성성

성을 지키기 위해 궁수 3명 배치
궁수는 성이 있는 칸에 배치 할 수 있음
각각의 턴마다 궁수는 적 하나를 공격할 수 있다
모든 궁수는 동시에 공격한다
궁수가 공격하는 적은 거리가 D 이하인 적 중 가장 가까운 적이다
그런 적이 여럿일 경우 가장 왼쪽에 있는 적을 공격한다
같은 적이 여러 궁수에게 공격당할 수 있다
공격받은 적은 게임에서 제외된다
궁수의 공격이 끝나면 적이 이동한다
적은 아래로 한칸 이동하며 성이 있는 칸으로 이동한 경우에는
게임에서 제외된다.
모든 적이 격자판에서 제외되면 게임이 끝난다
궁수의 공격으로 제거할 수 있는 적의 최대 수
격자판 거리 계산은 (r1, c1), (r2, c2) 일 떄 |r1-r2| + |c1-c2|

How to 
for문으로 1칸씩 전진 
    for문으로 쏠 수 있는 애 찾기
'''
import itertools
import copy
N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst_temp = copy.deepcopy(lst)
isFind = False
n = int(N)
def generate_combinations(n):
    arr = list(range(n)) # 0부터 n-1까지의 숫자를 생성
    result = []

    for combination in itertools.combinations(arr, 3): # 모든 가능한 3개의 조합을 생성
        result.append(list(combination))
    return result

answer2 = 0
for h in generate_combinations(M):
    n = int(N)
    answer = 0
    for i in range(N):
        for k in h:
            isFind = False
            q = []
            visited = [[0]*(M+1) for _ in range(n+1)]
            q.append([n, k])
            visited[n][k] = 1
            try:
                if D>1:
                    for j in range(D):
                        if isFind:
                            break
                        posy, posx = q.pop(0)
                        for yy, xx in [[posy, posx-1], [posy-1, posx], [posy, posx+1]]:
                            if 0<=xx<M and 0<=yy<n and visited[yy][xx] == 0:
                                if lst[yy][xx] == 1:
                                    lst[yy][xx] = 0
                                    answer += 1
                                    isFind = True
                                    break
                                else:
                                    q.append([yy, xx])
                else:
                    sum_list = []
                    for j in range(M):
                        sum_ = 0
                        for i in range(N):
                            sum_ += lst[i][j]
                        sum_list.append(sum_)
                    sum_list.sort(reverse=True)
                    exit()
            except:
                pass
        n -= 1  
    answer2 = max(answer, answer2) 
    lst = lst_temp
