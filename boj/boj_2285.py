# solved: [2285] 우체국
# https://www.acmicpc.net/problem/2285
# greedy, sorting
# 
# Gold 4
# 모든 사람들의 합을 구한 후, 우체국의 위치에 대하여 sort했을 때
# 사람들의 합의 절반이 넘어가는 최초의 지점이 문제의 해

import sys
input = sys.stdin.readline

psum = 0
arr = []
for _ in range(int(input())):
    x, a = map(int, input().split())
    psum += a
    arr.append((x, a))

arr.sort()
half_psum = psum // 2
chk = 0
for x, a in arr:
    chk += a
    if chk > half_psum:
        print(x)
        break
