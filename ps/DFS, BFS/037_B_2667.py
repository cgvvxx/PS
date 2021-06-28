# Baekjoon 2667 - 단지번호붙이기
# Silver 1
# BFS/DFS

from collections import Counter


def dfs(i, j):
    if i < 0 or j < 0 or i >= n or j >= n:
        return False

    if graph[i][j] == -1:
        graph[i][j] = result + 1
        dfs(i - 1, j)
        dfs(i, j - 1)
        dfs(i + 1, j)
        dfs(i, j + 1)
        return True

    return False


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = -1

result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1

print(result)

count = Counter(sum(graph, []))
if len(count) == 1:
    print(count[1])
else:
    ans = []
    for key in range(1, len(count)):
        ans.append(count[key])
    ans.sort()
    for an in ans:
        print(an)