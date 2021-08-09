# Baekjoon 2075 - N번째 큰 수
# Gold 5
# 스택/큐 - 힙


import heapq

n = int(input())
heap = []

for _ in range(n):
    arr = map(int, input().split())
    for num in arr:
        heapq.heappush(heap, num)
    while len(heap) > n:
        heapq.heappop(heap)
        
print(heap[0])