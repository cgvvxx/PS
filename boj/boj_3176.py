# solved: [3176] 도로 네트워크
# https://www.acmicpc.net/problem/3176
# dfs, lca, tree
#
# Platinum 4
# lca 응용
# parents와 같이 parents_min, parents_max를 정의
# 예를 들어, parents_min[n][k]는 노드 n에서 2^k 조상노드 까지의 거리 중 최솟값
# 조상 노드를 찾는 과정을 parents_min, parents_max도 같이 진행
# 이 때, 순서 주의!! 노드를 업데이트 하기 전에 dist_min, dist_max 값 업데이트 해야함

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(u, depth):
    visited[u] = True
    depths[u] = depth
    for v, d in graphs[u]:
        if not visited[v]:
            parents[v][0] = u
            parents_min[v][0] = d
            parents_max[v][0] = d
            dfs(v, depth + 1)

def set_parent(root):
    
    dfs(root, 0)
    
    for j in range(1, k):
        for i in range(1, n+1):
            parents[i][j] = parents[parents[i][j-1]][j-1]
            parents_min[i][j] = min(parents_min[i][j-1], parents_min[parents[i][j-1]][j-1])
            parents_max[i][j] = max(parents_max[i][j-1], parents_max[parents[i][j-1]][j-1])

def lca(u, v):
    
    dist_min, dist_max = DMAX, 0
    
    if depths[u] > depths[v]:
        u, v = v, u

    for i in range(k-1, -1, -1):
        if depths[v] - depths[u] >= (1 << i):
            dist_min = min(dist_min, parents_min[v][i])
            dist_max = max(dist_max, parents_max[v][i])
            v = parents[v][i]

    if u == v:
        print(dist_min, dist_max)
        return

    for i in range(k-1, -1, -1):
        if parents[u][i] and parents[v][i] and parents[u][i] != parents[v][i]:
            dist_min = min(dist_min, parents_min[u][i], parents_min[v][i])
            dist_max = max(dist_max, parents_max[u][i], parents_max[v][i])
            u = parents[u][i]
            v = parents[v][i]
    
    dist_min = min(dist_min, parents_min[u][0], parents_min[v][0])
    dist_max = max(dist_max, parents_max[u][0], parents_max[v][0])
    print(dist_min, dist_max)
    return


DMAX = 10 ** 6 + 1
n = int(input())
graphs = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, d = map(int, input().split())
    graphs[a].append((b, d))
    graphs[b].append((a, d))

k = 17
visited = [False] * (n+1)
parents = [[0] * k for _ in range(n+1)]
parents_min = [[DMAX] * k for _ in range(n+1)]
parents_max = [[0] * k for _ in range(n+1)]
depths = [0] * (n+1)

set_parent(1)

for _ in range(int(input())):
    u, v = map(int, input().split())
    lca(u, v)
