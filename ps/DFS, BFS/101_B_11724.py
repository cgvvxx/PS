# Baekjoon 11724 - 연결 요소의 개수
# Silver 2
# DFS/BFS 


import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
    
def dfs(start):
    
    visited[start] = True
    
    for i in graphs[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

count = 0
for idx, is_visited in enumerate(visited):
    
    if idx == 0:
        continue
    
    if not is_visited:
        dfs(idx)
        count += 1

print(count)