# Baekjoon 1012
# Silver 2
# BFS/DFS

# 1. DFS > 재귀 깊이 늘려줘야함

import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return False

    if graph[y][x] == 1:
        graph[y][x] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False


T = int(input())

counts = []
for _ in range(T):
    M, N, K = map(int, input().split(' '))
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split(' '))
        graph[j][i] = 1

    ans = 0
    for x in range(M):
        for y in range(N):
            if dfs(x, y) == 1:
                ans += 1
    counts.append(ans)

for count in counts:
    print(count)

# 2. BFS
from collections import deque


def bfs(x, y):
    if check[y][x]:
        return 0
    else:
        queue = deque()
        queue.append((x, y))
        check[y][x] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if check[ny][nx]:
                continue
            if not check[ny][nx]:
                check[ny][nx] = True
                queue.append((nx, ny))

    return 1


T = int(input())

counts = []
for _ in range(T):
    M, N, K = map(int, input().split(' '))
    graph = [[0] * M for _ in range(N)]
    check = [[True] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split(' '))
        graph[j][i] = 1
        check[j][i] = False

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = 0
    for x in range(M):
        for y in range(N):
            cnt = bfs(x, y)
            if cnt == 1:
                ans += 1
    counts.append(ans)

for count in counts:
    print(count)