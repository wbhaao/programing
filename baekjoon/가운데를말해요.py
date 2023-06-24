import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []

for _ in range(n):
    x = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    
    else:
        heapq.heappush(right_heap, x)
        
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)
        
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    print(left_heap[0] * -1)