# Baekjoon 14425 - 문자열 집합
# Silver 3

import sys

N, M = map(int, input().split())

check_set = set()
count = 0

for _ in range(N):
    check_set.add(sys.stdin.readline().strip())
for _ in range(M):
    if sys.stdin.readline().strip() in check_set: 
        count += 1
print(count)