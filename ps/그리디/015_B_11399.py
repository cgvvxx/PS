# Baekjoon 11399
# Silver 3
# 그리디

n = int(input())
time_arr = [*map(int, input().split())]

res = 0
for i, t in enumerate(sorted(time_arr)): res += t * (len(time_arr) - i)

print(res)