# Baekjoon 11003 - 최솟값 찾기
# platinum 5
# 스택/큐 - 덱, 힙


#1. 
import heapq

n, l = map(int, input().split())
arr = map(int, input().split())

heap = []
for i, a in enumerate(arr):
    heapq.heappush(heap, (a, i))
    while True:
        if heap[0][1] <= i-l:
            heapq.heappop(heap)
        else:
            break
    
    print(heap[0][0], end=' ')
    
    
# 최소 힙을 이용한 풀이
# 힙에 인덱스와 그 때의 숫자를 넣고, 힙에서 인덱스가 현재 범위에 벗어날 때 pop
# 아닌 경우 최솟값을 print
# 이 경우 시간복잡도 O(nlogn)으로 pypy3으로만 통과 (8960ms)


#2. 
from collections import deque

n, l = map(int, input().split())
arr = map(int, input().split())
deq = deque()

for i, a in enumerate(arr):
    
    if i == 0:
        deq.append((a, i))
        print(deq[0][0], end=' ')
        continue
    
    if deq[0][1] <= i - l:
        deq.popleft()
        
    if not deq:
        deq.append((a, i))
    else:
        while True:
            if deq[-1][0] > a:
                deq.pop()
                if not deq:
                    deq.append((a, i))
                    break
            else:
                deq.append((a, i))
                break

    
    print(deq[0][0], end=' ')
    
    
# deque을 이용한 풀이
# 주어진 deque에 왼쪽부터 현재 범위의 수부터 오름차순으로 정렬되도록 함
# 맨 왼쪽(최솟값)의 인덱스가 범위에 벗어날 경우 pop
# 맨 오른쪽부터 현재 값보다 큰 값을 갖는 경우 모조리 pop하여 deque의 정렬을 유지함
# 시간복잡도는 O(n)으로 python3로도 통과 (9032ms), pypy3는 (6728ms)