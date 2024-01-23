'''
트리
트라이 알고리즘 : 
https://twpower.github.io/187-trie-concept-and-basic-problem
차례대로 그래프를 만듦
DFS로 탐색해서 출력
ㅈㄴ 이지
'''

def add(dict, arr):
    if len(arr) == 0:
        return

    if arr[0] not in dict:
        dict[arr[0]] = {}
    add(dict[arr[0]], arr[1:])

def answer(dict, leng):
    for i in sorted(dict.keys()):
        print("--"*leng+i)
        answer(dict[i],leng+1)

N = int(input())
lst = [list(input().split()[1:]) for _ in range(N)]
dict = {}

for i in lst:
    add(dict, i)

answer(dict, 0)