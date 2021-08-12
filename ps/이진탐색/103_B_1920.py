# Baekjoon 1920 - 수 찾기
# Silver 4
# 이진탐색

import bisect

N = int(input())
Ns = list(map(int, input().split()))
M = int(input())
Ms = list(map(int, input().split()))

Ns.sort()

for m in Ms:
    print(1) if Ns[bisect.bisect_right(Ns, m)-1] == m else print(0)