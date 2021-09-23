# Baekjoon 1197 - 최소 스패닝 트리
# Gold 4
# Tree - MST


#1. Kruskal algorithm
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = list(range(v+1))

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)


#2. Prim algorithm
from collections import defaultdict
import heapq


v, e = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (v+1)
mst = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, a, b))
    graph[b].append((cost, b, a))
    
start = 1
visited[start] = 1
candidate = graph[start]
heapq.heapify(candidate)

while candidate:
    cost, a, b = heapq.heappop(candidate)
    
    if visited[b] == 0:
        visited[b] = 1
        mst.append((a, b))
        result += cost
        
        for edge in graph[b]:
            if visited[edge[2]] == 0:
                heapq.heappush(candidate, edge)

print(result)


# 기본적인 MST 문제
# Kruskal과 Prim algorithm으로 풀어봄
# 이 문제의 경우는 kruskal로 푼게 prim으로 푼거 보다 빨랐음