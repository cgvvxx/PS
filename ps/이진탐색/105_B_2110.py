# Baekjoon 2110 - 공유기 설치
# Silver 1
# 이진탐색


import sys
input = sys.stdin.readline

def is_okay(dist):
    
    this = houses[0]
    count = 1
    
    for h in houses[1:]:
        if h - this >= dist:
            count += 1
            this = h
            
    if count >= C:
        return True
    else:
        return False        


N, C = map(int, input().split())

start = int(input())
min_x, max_x = start, start
houses = [start]

for _ in range(N-1):
    
    xi = int(input())
    houses.append(xi)
    
    if min_x > xi:
        min_x = xi
        continue
    
    if max_x < xi:
        max_x = xi
        continue 

houses.sort()
max_dist = (max_x - min_x) // (C-1)
min_dist = 1

while min_dist <= max_dist:
    
    mid = (min_dist + max_dist) // 2
    
    if is_okay(mid):
        min_dist = mid + 1
    else:
        max_dist = mid - 1
    
if is_okay(max_dist):
    print(max_dist)
else:
    print(mid)
