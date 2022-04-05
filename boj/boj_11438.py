# solved: [11438] LCA 2
# https://www.acmicpc.net/problem/11438
# dfs, lca, tree
# 
# Platinum 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))


def dfs(u, depth):
    visited[u] = True
    d[u] = depth
    for v in graphs[u]: # 그래프는 인접 리스트로 주어지는 경우
        if not visited[v]:
            parents[v][0] = u # 노드 v의 부모 노드는 parents[v][0]
            dfs(v, depth + 1)
    
def set_parent():
    
    dfs(1, 0) # 루트 노드는 1번으로 주어지는 경우
    
    for j in range(1, k): # 이 때 k는 log(n)의 올림 값
        for i in range(1, n+1):
            parents[i][j] = parents[parents[i][j-1]][j-1]
            
def lca(u, v):
    
    if d[u] > d[v]: 
        u, v = v, u # v의 깊이가 u의 깊이보다 깊도록 설정

    diff = d[v] - d[u]
    for i in range(k):
        if diff & 1:
            v = parents[v][i]
        diff >>= 1
            
    if u == v:
        return u

    for i in range(k-1, -1, -1):
        if parents[u][i] != parents[v][i]: # 두 노드의 2^i번째 조상이 다르면 u와 v를 각각 2^i번째 조상으로 업데이트
            u = parents[u][i]
            v = parents[v][i]

    return parents[u][0]


n = int(input())
graphs = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

k = 21
visited = [False] * (n+1) # n은 전체 노드의 개수, 각 노드는 1부터 n까지 번호로 주어지는 경우
parents = [[0] * k for _ in range(n+1)]
d = [0] * (n+1) # 각 노드의 깊이

set_parent()

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    print(lca(u, v))
