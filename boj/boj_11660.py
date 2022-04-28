# solved: [11600] 구간 합 구하기 5
# https://www.acmicpc.net/problem/11600
# prefix-sum
# 
# Silver 1
# 이차원 누적 합 기본 문제 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [list(map(int, input().split())) for _ in range(n)]
psum = [[0] * (n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        psum[i+1][j+1] = nums[i][j] + psum[i+1][j] + psum[i][j+1] - psum[i][j]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(psum[x2][y2]-psum[x1-1][y2]-psum[x2][y1-1]+psum[x1-1][y1-1])
