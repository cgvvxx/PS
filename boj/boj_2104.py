# solved: [2104] 부분배열 고르기
# https://www.acmicpc.net/problem/2104
# divide-and-conquer, recursion
# 
# Platinum 5
# 히스토그램 내의 최대 직사각형의 크기를 구하는 문제(1725)와 비슷한 방식의 분할 정복 알고리즘을 활용
# 이 때, 가운데를 포함한 수열에 대해서 가로의 길이가 수열의 합, 세로의 길이가 각 수열의 값들의 최솟값으로 진행

def dq(s, e):
    
    if s == e:
        return 0
    elif s+1 == e:
        return arr[s] ** 2
    
    m = (s + e) // 2
    score = max(dq(s, m), dq(m, e))
    
    l, r = m, m
    a, b = arr[l], arr[l]
    
    while r-l+1 < e-s:
        
        p = min(b, arr[l-1]) if l > s else -1
        q = min(b, arr[r+1]) if r < e-1 else -1
        
        if p >= q:
            l -= 1
            a += arr[l]
            b = min(b, p)
        else:
            r += 1
            a += arr[r]
            b = min(b, q)
            
        score = max(score, a*b)
    
    return score


n = int(input())
arr = list(map(int, input().split()))
print(dq(0, n))
