# solved: [3584] 가장 가까운 공통 조상
# https://www.acmicpc.net/problem/3584
# dfs, lca, tree
#
# Gold 4
# 1. 주어진 노드 쌍으로 root node 찾기
# 2. root node에서 dfs로 parents[n][k] 배열 채우기
# 3. 주어진 두 노드의 깊이(depth)를 맞추고 조상 노드를 올라가면서 lca 찾기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(u, depth):
    visited[u] = True
    d[u] = depth
    for v in graphs[u]:
        if not visited[v]:
            parents[v][0] = u
            dfs(v, depth + 1)

def set_parent(root):
    
    dfs(root, 0)
    
    for j in range(1, k):
        for i in range(1, n+1):
            parents[i][j] = parents[parents[i][j-1]][j-1]

def lca(u, v):
    
    if d[u] > d[v]: 
        u, v = v, u

    diff = d[v] - d[u]
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


for _ in range(int(input())):

    n = int(input())
    graphs = [[] for _ in range(n+1)]
    is_tree = [True] * (n+1)

    for _ in range(n-1):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)
        is_tree[b] = False
    
    for i in range(1, n+1):
        if is_tree[i]:
            root = i
            break

    k = 16
    visited = [False] * (n+1)
    parents = [[0] * k for _ in range(n+1)]
    d = [0] * (n+1)
    
    set_parent(root)

    u, v = map(int, input().split())
    print(lca(u, v))
