# solved: [1761] 정점들의 거리
# https://www.acmicpc.net/problem/1761
# dfs, lca, tree
# 
# Platinum 5
# lca를 이용한 두 노드의 최단거리 구하기
# 루트에서 각 노드까지의 거리를 dists를 구하면 u와 v의 거리 = dists[u] + dists[v] - 2 * dists[lca(u, v)]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(u, depth):
    visited[u] = True
    depths[u] = depth
    for v, d in graphs[u]:
        if not visited[v]:
            parents[v][0] = u
            dists[v] = d + dists[u]
            dfs(v, depth + 1)

def set_parent(root):
    
    dfs(root, 0)
    
    for j in range(1, k):
        for i in range(1, n+1):
            parents[i][j] = parents[parents[i][j-1]][j-1]

def lca(u, v):
    
    if depths[u] > depths[v]:
        u, v = v, u

    diff = depths[v] - depths[u]
    for i in range(k):
        if diff & 1:
            v = parents[v][i]
        diff >>= 1
            
    if u == v:
        return u

    for i in range(k-1, -1, -1):
        if parents[u][i] != parents[v][i]:
            u = parents[u][i]
            v = parents[v][i]

    return parents[u][0]

def get_dist(u, v):
    
    w = lca(u, v)
    
    return dists[u] + dists[v] - 2 * dists[w]


n = int(input())
graphs = [[] for _ in range(n+1)]
dists = [0] * (n+1)

for _ in range(n-1):
    a, b, d = map(int, input().split())
    graphs[a].append((b, d))
    graphs[b].append((a, d))

k = 16
visited = [False] * (n+1)
parents = [[0] * k for _ in range(n+1)]
depths = [0] * (n+1)

set_parent(1)

for _ in range(int(input())):
    u, v = map(int, input().split())
    print(get_dist(u, v))
