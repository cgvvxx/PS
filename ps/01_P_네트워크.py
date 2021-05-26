from collections import deque


def solution(n, computers):
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            visited[i] = True

            while queue:
                pop = queue.popleft()
                for j in range(len(computers[pop])):
                    if i != j and computers[pop][j] == 1 and not visited[j]:
                        queue.append(j)
                        visited[j] = True

            count += 1

    return count