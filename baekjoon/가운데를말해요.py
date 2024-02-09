import heapq  # 힙(heap) 자료구조를 사용하기 위한 모듈을 불러옵니다.
import sys

input = sys.stdin.readline  # 입력을 빠르게 받기 위해 sys.stdin.readline을 사용합니다.

n = int(input())  # 입력받을 데이터의 개수를 받습니다.
left_heap = []  # 최대 힙을 사용하기 위한 리스트입니다.
right_heap = []  # 최소 힙을 사용하기 위한 리스트입니다.

for _ in range(n):  # n번의 데이터 입력을 받습니다.
    x = int(input())  # 데이터를 하나씩 입력받습니다.

    # 입력받은 데이터를 최대 힙과 최소 힙에 나누어 저장합니다.
    # 힙의 크기가 같다면 최대 힙에 데이터를 저장합니다.
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)  # 파이썬의 heapq 모듈은 기본적으로 최소 힙만 지원하므로, 최대 힙을 구현하기 위해 값을 음수로 변환하여 저장합니다.
    else:
        heapq.heappush(right_heap, x)  # 힙의 크기가 다르다면 최소 힙에 데이터를 저장합니다.

    # 만약 최대 힙의 최댓값이 최소 힙의 최솟값보다 크다면, 두 값을 교환합니다.
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)  # 최대 힙에서 최댓값을 제거하고 해당 값을 가져옵니다.
        min_value = heapq.heappop(right_heap)  # 최소 힙에서 최솟값을 제거하고 해당 값을 가져옵니다.
        
        heapq.heappush(left_heap, min_value * -1)  # 최댓값과 최솟값을 교환하여 다시 힙에 저장합니다.
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)  # 최대 힙의 루트 노드 값을 출력하면 중앙값을 구할 수 있습니다.
