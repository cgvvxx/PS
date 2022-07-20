# solved: [6549] 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549
# divide-and-conquer, recursion
# 
# Platinum 5
# boj 1725랑 같은 문제
# 입력이 조금 다르므로, while문으로 입력 받고 n과 hist를 나누어 분할정복(dq)를 통해 넓이를 구함
# n == 0인 경우 break

import sys
input = sys.stdin.readline

def dq(s, e):
    
    if s == e:
        return 0
    elif s+1 == e:
        return hist[s]
    
    mid = (s + e) // 2
    area = max(dq(s, mid), dq(mid, e))
    
    l, r = mid, mid
    w, h = 1, hist[mid]
    
    while r-l+1 < e-s:
        
        p = min(h, hist[l-1]) if l > s else -1
        q = min(h, hist[r+1]) if r < e-1 else -1
        
        if p >= q:
            h = p
            l -= 1
        else:
            h = q
            r += 1
        
        w += 1
        area = max(area, w*h)
    
    return area


while True:
    n, *hist = map(int, input().split())
    if not n:
        break
    else:
        print(dq(0, n))
