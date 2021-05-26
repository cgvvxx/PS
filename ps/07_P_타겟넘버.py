# Level2
# DFS/BFS

from itertools import combinations


def solution(numbers, target):
    count = 0
    li_sum = sum(numbers)
    for i in range(1, len(numbers)):
        for j in combinations(numbers, i):
            if li_sum - 2 * sum(j) == target:
                count += 1

    return count