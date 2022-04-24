# solved: [11659] 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
# prefix-sum
# 
# Silver 3
# 누적 합 기본 문제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0] + list(map(int, input().split()))
psum = [0]

for i in range(1, n+1):
    psum.append(nums[i] + psum[i-1])

for _ in range(m):
    i, j = map(int, input().split())
    print(psum[j] - psum[i-1])
