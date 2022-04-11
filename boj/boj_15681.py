# solved: [15681] 트리와 쿼리
# https://www.acmicpc.net/problem/15681
# dfs, dp, tree, tree-dp
#
# Gold 5
# 트리 dp 기본 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(n):
    
    visited[n] = True
    
    for m in graphs[n]:
        if not visited[m]:
            dfs(m)
            dp[n] += dp[m]
            

n, r, q = map(int, input().split())

graphs = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

visited = [False] * (n+1)
dp = [1] * (n+1)

dfs(r)

for _ in range(q):
    print(dp[int(input())])
