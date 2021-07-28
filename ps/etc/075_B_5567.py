# Baekjoon 5567 - 결혼식
# Silver 1

import sys

n = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n+1)]
check = [False] * (n+1)

for _ in range(int(sys.stdin.readline().strip())):
    n, m = map(int, sys.stdin.readline().strip().split())
    graph[n].append(m)
    graph[m].append(n)
    
if graph[1]:
    fr = graph[1]
    new_fr = []
    for i in graph[1]:
        new_fr.extend(graph[i])
    print(len(set(new_fr) | set(fr+[1]))-1)
else:
    print(0)