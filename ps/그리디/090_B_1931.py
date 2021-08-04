# Baekjoon 1931 - 회의실 배정
# Silver 2
# 그리디

import sys
input = sys.stdin.readline

meeting = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    meeting.append((a, b, b-a))
meeting.sort(key=lambda x:(x[1], x[0], x[2]))

ans = 1
start, end = meeting[0][:2]

for meet in meeting[1:]:
    
    if end <= meet[0]:
        ans += 1
        end = meet[1]
        continue
        
    if start >= meet[1]:
        ans += 1
        start = meet[0]
        continue

print(ans)