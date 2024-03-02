'''
아 그 뭐 하는 법

3:
0, 1, 2

4:
0, 1, 2
0, 1, 3
0, 2, 3

5:
0, 1, 2
0, 1, 3
0, 1, 4
0, 2, 3
0, 2, 4
0, 3, 4
'''

import itertools

def generate_combinations(n):
    arr = list(range(n)) # 0부터 n-1까지의 숫자를 생성
    result = []

    for combination in itertools.combinations(arr, 3): # 모든 가능한 3개의 조합을 생성
        result.append(list(combination))
    return result
n = int(input("값을 입력하세요: "))
print(generate_combinations(n))