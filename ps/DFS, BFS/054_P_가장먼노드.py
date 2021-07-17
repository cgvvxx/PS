# Programmers - 가장 먼 노드
# Level 3
# BFS/DFS

from collections import deque


def bfs(graph):
    queue = deque()
    visited = [False] * (len(graph) + 1)
    dist = [0] * (len(graph) + 1)

    queue.append(1)
    visited[1] = True

    while queue:
        v = queue.popleft()
        for _ in range(len(graph[v])):
            for j in graph[v]:
                if not visited[j]:
                    queue.append(j)
                    visited[j] = True
                    dist[j] = dist[v] + 1

    return dist

def solution(n, edge):
    graph = dict()
    for i in range(1, n + 1):
        graph[i] = []
    for j, k in edge:
        graph[j].append(k)
        graph[k].append(j)

    dist = bfs(graph)

    max_dist = max(dist)
    count = 0
    for i in dist:
        if max_dist == i:
            count += 1

    return count