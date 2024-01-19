'''
(깊이 우선 탐색)
입력이 엄청 많다..
두 노드의 가장 가까운 조상을 찾으면 된다
![2024-01-19-14-00-59.png]
15와 11을 모두 자손으로 갖는 노드는 4와 8이 있고,
그 중 가장 깊이가 깊은 노드는 4이다

테스트케이스
노드 수
간선 정보가 주어짐

어떻게 할까요?????
하나의 노드를 정한 다음
부모로 차례차례 올라가면서
다른 하나 노드를 찾아야함
or
두 노드를 한칸씩 올림
공통 부모를 찾기
부모 리스트 2개 만들기

'''
from sys import stdin
from collections import deque
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    # 1부터 시작
    graph = [None for _ in range(N+1)]
    for _ in range(1, N):
        # graph[부모] = [자식들]
        # 역순 탐색만 가능하게
        # graph[B].append(A)로 만듦
        A, B = map(int, stdin.readline().split())
        graph[B] = A

    C, D = map(int, stdin.readline().split())
    c_parent_list = deque([C, graph[C]])
    d_parent_list = deque([D, graph[D]])
    while True:
        # 공통된 부분이 있다면 탈주
        a = set(c_parent_list) & set(d_parent_list)
        if a != set([]):
            print(list(a)[0])
            break
        if c_parent_list != deque([]) and graph[c_parent_list[-1]] != None:
            c_parent_list.append(graph[c_parent_list[-1]])
        if d_parent_list != deque([]) and graph[d_parent_list[-1]] != None:
            d_parent_list.append(graph[d_parent_list[-1]])

