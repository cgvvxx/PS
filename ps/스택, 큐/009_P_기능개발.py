# Programmers - 기능개발
# Level 2
# 스택/큐

from collections import deque


def RoundUp(n):
    if n == int(n):
        return int(n)
    else:
        return int(n) + 1


def solution(progresses, speeds):
    left_days = [RoundUp((100 - p) / s) for p, s in zip(progresses, speeds)]

    queue = deque()
    answer = []
    count = 0

    queue.append(left_days[0])

    for i in left_days[1:]:
        if queue[0] >= i:
            queue.append(i)
        else:
            while queue:
                queue.popleft()
                count += 1
            answer.append(count)
            count = 0
            queue.append(i)

    while queue:
        queue.popleft()
        count += 1
    answer.append(count)

    return answer
