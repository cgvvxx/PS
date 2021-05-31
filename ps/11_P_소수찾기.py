# Level2
# 완전탐색

from itertools import permutations


def is_prime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    count = 0
    use_li = []
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            if num not in use_li and is_prime(num):
                count += 1
            use_li.append(num)

    return count