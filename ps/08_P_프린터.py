# Level2
# 스택/큐

from collections import deque


def solution(priorities, location):
    queue = deque()
    for idx, i in enumerate(priorities):
        queue.append([idx, i])

    this_prior = queue.popleft()
    ans = []
    reset = False

    while queue:
        for item in queue:
            if this_prior[1] < item[1]:
                queue.append(this_prior)
                reset = True
                break
        if reset:
            reset = False
        else:
            ans.append(this_prior[0])
        this_prior = queue.popleft()

    ans.append(this_prior[0])

    return ans.index(location) + 1