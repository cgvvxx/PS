# Baekjoon 2805 - 나무 자르기
# Silver 3
# 이진탐색

import bisect

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.append(0)
trees.sort(reverse=True)

left_h = []
partial_sum = 0
tree_max = trees[0]
for i in range(len(trees)):
    left_h.append(partial_sum - trees[i]*i)
    partial_sum += trees[i]

idx = bisect.bisect_left(left_h, M)
print(trees[idx] + (left_h[idx] - M) // idx)