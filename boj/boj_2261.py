# solved: [2261] 가장 가까운 두 점
# https://www.acmicpc.net/problem/2261
# divide-and-conquer, geometry
# 
# Platinum 2
# n이 최대 100000개이므로 분할정복을 이용한 O(nlogn)의 풀이
# 1. 왼쪽 점들, 오른쪽 점들의 최솟값 + 2. 가운데 band 구간에서의 점들의 최솟값
# 1의 경우 단순히 2개 또는 3개 일때의 점들의 최솟값을 분기로 재귀적으로 구현
# 2의 경우, 1에서 구한 거리의 최솟값에 해당하는 밴드안에서의 점들을 이용하여 최솟값 구하기
# line 46의 break 없으면 시간초과..

import sys
input = sys.stdin.readline

def dist(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2


def brute(s, e):
    
    min_dst = 10**7
    for i in range(s, e):
        for j in range(i+1, e+1):
            min_dst = min(min_dst, dist(points[i], points[j]))
    return min_dst
        
    
def middle(s, m, e, min_dst):
    
    mid_x = points[m][0]
    chks = []
    for i in range(s, e+1):
        del_x = mid_x - points[i][0]
        if del_x**2 < min_dst:
            chks.append(points[i])
            
    chks.sort(key=lambda x:x[1])
    l = len(chks)
    
    for i in range(l-1):
        for j in range(i+1, l):
            del_y = chks[i][1] - chks[j][1]
            if del_y ** 2 < min_dst:
                min_dst = min(min_dst, dist(chks[i], chks[j]))
            else:
                break
    
    return min_dst
    

def dq(s, e):
    
    if e - s < 3:
        return brute(s, e)
    
    m = (e + s) // 2
    
    l = dq(s, m)
    r = dq(m+1, e)
    
    min_dst = min(l, r)
    min_middle = middle(s, m, e, min_dst)
    
    return min(min_dst, min_middle)


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()

print(dq(0, n-1))
