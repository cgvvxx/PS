# Baekjoon 1260
# Silver 2
# BFS/DFS

from collections import deque

N, M, V = map(int, input().split())

graph_dict = dict()
for i in range(N):
    graph_dict[i + 1] = []

for _ in range(M):
    n, m = map(int, input().split())
    graph_dict[n].append(m)
    graph_dict[m].append(n)

graph = [[]]
for i in graph_dict:
    graph.append(sorted(graph_dict[i]))


def dfs(graph, v):
    visited = [False] * len(graph)
    stack = []
    ans = []

    stack.append(v)
    ans.append(v)

    while stack:
        n = stack[-1]

        if not graph[n]:
            pop = stack.pop()

        for i in graph[n]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                ans.append(i)
                break
            if i == graph[n][-1]:
                pop = stack.pop()

        visited[n] = True

    return ans


def bfs(graph, v):
    visited = [False] * len(graph)
    queue = deque()
    ans = []

    queue.append(v)

    while queue:
        n = queue.popleft()
        ans.append(n)
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

        visited[n] = True

    return ans


print(' '.join(map(str, dfs(graph, V))))
print(' '.join(map(str, bfs(graph, V))))