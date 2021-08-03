# Baekjoon 11000 - 강의실 배정
# Gold 5
# 그리디

import heapq
import sys
input = sys.stdin.readline

time_table = []
for _ in range(int(input())):
    time_table.append(tuple(map(int, input().split())))
time_table.sort()

heap = [] 
heapq.heappush(heap, time_table[0][1])  # heap에 첫 원소의 끝나는 시각 기록

for time in time_table[1:]:
    if heap[0] <= time[0]:  # 새로 들어온 시간표의 시작시간이 끝나는 시간 이후일 경우
        heapq.heappop(heap)  # 그 원소를 pop
    heapq.heappush(heap, time[1])  # 그리고 새로 들어온 시간표의 끝나는 시간 push

print(len(heap))  # heap에 들어온 원소의 개수가 강의실의 개수