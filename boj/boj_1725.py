# solved: [1725] 히스토그램
# https://www.acmicpc.net/problem/1725
# divide-and-conquer, recursion
# 
# Platinum 5
# 분할 정복을 통해 히스토그램의 최대 직사각형 넓이를 구하는 문제
# 1. 왼쪽에서의 최댓값, 2. 오른쪽에서의 최댓값, 3. 걸쳐있는 사각형에 대한 최댓값들의 최댓값을 리턴
# 1, 2의 경우 단순 재귀함수를 통해 간단히 구할 수 있음
# 3의 경우 사각형의 왼쪽 인덱스 l, 오른쪽 인덱스 r을 가운데(mid)에서 시작하여 더 큰 높이를 가지는 방향으로
# 한 칸씩 전진하면서 사각형의 크기를 구해나가면서 최댓값을 구함

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


n = int(input())
hist = [int(input()) for _ in range(n)]
print(dq(0, n))
