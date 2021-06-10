# Programmers - 입국심사
# Level 3
# 이진탐색

def count_divisable(n, times):
    count = 0
    for i in times:
        count += n // i
    return count


def solution(n, times):
    start = 1
    end = min(times) * n
    check = False

    while start <= end:
        if check:
            mid -= 1
        else:
            mid = (start + end) // 2

        count = 0
        for i in times:
            count += mid // i

            if count >= n:
                end = mid - 1
                break

        if count < n:
            start = mid + 1

    if count_divisable(mid, times) < n:
        return mid + 1
    else:
        return mid