'''
순열 사이클이란 정렬된 배열과 비정렬된 배열이 
함수로서(f(x)) 순환될 때 순환 사이클이라 한다

3, 2, 7, 8, 1, 4, 5, 6을 예로 들 때
배열은
1, 2, 3, 4, 5, 6, 7, 8
3, 2, 7, 8, 1, 4, 5, 6
일것이다

1. 그래프 탐색을 통해 1과 같은 인덱스인 아래 배열의 3을 찾고 위의 배열에서 3을 찾는다. 
2. 위 배열의 3과 같은 인덱스 7을 찾고 위의 배열에서 7을 찾는다 
3. 7과 같은 인덱스에 있는 아래 배열의 5를 찾고 위의 배열에 5을 찾으니 5와 같은 인덱스의 값이 1이 나와 순환하게 된다.
'''
from sys import stdin
T = int(stdin.readline())

def find_cycle(start, flag, lst):
    if numbers[flag] == start and len(lst)>0:
        return lst
    else:
        lst.add(numbers[flag])
        return find_cycle(start, numbers[flag]-1, lst)

for i in range(T):
    N = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))

    visited = set([])
    cnt = 0

    for i in range(N):
        if i+1 not in visited:
            cnt += 1
            visited |= find_cycle(i+1, i, set([i+1]))
    
    print(cnt)
