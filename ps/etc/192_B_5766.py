# Baekjoon 5766 - 할아버지는 유명해!
# Silver 4


from collections import Counter


def second_max(iters):
    
    iters = sorted(iters, reverse=True)
    is_max = iters[0]
    
    for n in iters[1:]:
        if n != is_max:
            return n
    else:
        return is_max
    
    
while True:
    n, m = map(int, input().split())

    if (n, m) == (0, 0):
        break
    
    nums = []
    for _ in range(n):
        nums += list(map(int, input().split()))

    grades = Counter(nums)
    smax = second_max(grades.values())
    ans = []
    for k, v in grades.items():
        if v == smax:
            ans.append(k)
    ans.sort()
    print(*ans)


# 나오는 개수를 세는 문제라 Counter 활용
# 두 번째로 많이 counting된 원소를 print하는 문제