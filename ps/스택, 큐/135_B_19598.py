# Baekjoon 19598 - 최소 회의실 개수
# Gold 5
# 스택/큐


import heapq

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))
    
meetings.sort()
heap = []
max_meet = 1
for i in meetings:
    if not heap:
        heapq.heappush(heap, i[1])
        continue
        
    if i[0] < heap[0]:
        heapq.heappush(heap, i[1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, i[1])
    
    if len(heap) > max_meet:
        max_meet = len(heap)
        
print(max_meet)


# heap에는 회의의 끝나는 시각 기록
# 회의의 시작시간을 기준으로 정렬 후 각 회의에 대해 시작시간이 heap에 기록된 끝나는 시각 보다 작으면
# heap에 push, 아니면 pop하고 push하여 heap의 길이가 가장 클 때 = 최대 회의실 개수