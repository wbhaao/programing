import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
def solution(N,tree):
	q = deque([1])
	parent = [0] * (N+1)
	global cnt
	while q:
		now = q.popleft()
		for i in tree[now]:
			if parent[i] == 0 and i != 1:
				cnt += 1
				parent[i] = now
				q.append(i)
	for i in range(2,N+1):
		print(parent[i])

if __name__ == "__main__":
	N = int(input())
	tree = dict()
	for i in range(1,N+1):
		tree[i] = []
	for _ in range(N-1):
		n1,n2 = map(int,input().split())
		tree[n1].append(n2)
		tree[n2].append(n1)
	solution(N,tree)