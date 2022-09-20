# solved: [16935] 배열 돌리기3
# https://www.acmicpc.net/problem/16935
# implementation
# 
# Silver 1
# 문제에서 요구하는대로 잘 구현할 것
# 여러 가지 경우의 배열 돌리기에 대해서 체크 (상하반전, 좌우반전, 오른쪽90도회전, 왼쪽90도회전 + a)
# [17470] 배열 돌리기5 도 참고할 것

import sys
input = sys.stdin.readline

def rotate_arr(arr, t):
    
    global n, m
    
    if t == 1:    # 상하반전
        return arr[::-1]
    
    elif t == 2:    # 좌우반전
        return [l[::-1] for l in arr]
    
    elif t == 3:    # 오른쪽으로 90도 회전
        n, m = m, n
        return list(zip(*arr[::-1]))
    
    elif t == 4:    # 왼쪽으로 90도 회전
        n, m = m, n
        return list(zip(*[l[::-1] for l in arr]))
    
    elif t == 5:
        
        new_arr = [[0 for _ in range(m)] for _ in range(n)]
        
        r = n//2
        c = m//2
        
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i][j] = arr[i+r][j]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i][j+c] = arr[i][j]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i+r][j] = arr[i+r][j+c]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i+r][j+c] = arr[i][j+c]
                
        return new_arr
        
    elif t == 6:
        
        new_arr = [[0 for _ in range(m)] for _ in range(n)]
        
        r = n//2
        c = m//2
        
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i][j] = arr[i][j+c]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i][j+c] = arr[i+r][j+c]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i+r][j] = arr[i][j]
                
        for i in range(n//2):
            for j in range(m//2):
                new_arr[i+r][j+c] = arr[i+r][j]
                
        return new_arr

        
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for t in map(int, input().split()):
    arr = rotate_arr(arr, t)

for l in arr:
    print(*l)
