# Baekjoon 13305
# Silver 4
# 그리디

n = int(input())
d = [*map(int, input().split())]
p = [*map(int, input().split())]

price, cost = p[0], 0

for i in range(n - 1):
    if price > p[i]: price = p[i]
    cost += d[i] * price

print(cost)