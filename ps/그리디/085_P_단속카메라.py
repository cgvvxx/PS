# Programmers - 단속카메라
# Level 3
# 그리디

from collections import deque

def solution(routes):

    routes.sort()
    queue = deque(routes)
    count = 1
    start, end = queue.popleft()

    while queue:

        if end < queue[0][0]:
            start, end = queue.popleft()
            count += 1
            continue
            
        if end > queue[0][1]:
            end = queue[0][1]

        queue.popleft()

    return count