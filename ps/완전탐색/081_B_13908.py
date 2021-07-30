# Baekjoon 13908 - 비밀번호
# Gold 5
# 완전탐색

from itertools import product

n, m = map(int, input().split())
known = list(map(int, input().split()))

count = 0
for prod in product(range(10), repeat=n):
    for i in known:
        if i not in prod:
            break
    else:
        count += 1

print(count)