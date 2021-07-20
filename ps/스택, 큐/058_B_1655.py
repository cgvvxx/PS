# Baekjoon 1655 - 가운데를 말해요
# Gold 2
# 스택/큐 - 힙 

import sys
import heapq

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
    
max_heap = []
min_heap = []
for i in nums:
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-i, i))
    else:
        heapq.heappush(min_heap, (i, i))
    if len(min_heap) >= 1 and max_heap[0][1] > min_heap[0][1]:
        bigger = heapq.heappop(max_heap)[1]
        smaller = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-smaller, smaller))
        heapq.heappush(min_heap, (bigger, bigger))
    print(max_heap[0][1])                  