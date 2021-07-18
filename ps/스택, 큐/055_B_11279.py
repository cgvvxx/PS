# Baekjoon 11279 - 최대 힙
# Silver 2
# 스택/큐 - 힙 

import sys
import heapq

N = int(input())
nums = []
heap = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))
    
for i in nums:
    if i == 0:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
    else:
        heapq.heappush(heap, (-i, i))    
        