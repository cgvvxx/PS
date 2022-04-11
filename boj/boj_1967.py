# solved: [1967] 트리의 지름
# https://www.acmicpc.net/problem/1967
# dfs, graph-traversal, tree
# 
# Gold 4
# leaf node에서 시작해서 leaf node까지의 거리 중 최댓값을 dfs를 이용해 구함
# 이 때 root node의 자식이 1인 경우, root node가 끝 점일 수 있으므로 n == 1인 경우의 거리의 최댓값도 같이 저장
# 중복되는 node나 edge 중복체크를 하지 않아서 시간은 굉장히 느림..

from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(n, d, visited):
    
    global ans
    
    if not parents[n] and not visited[n]:
        ans = max(ans, d)
        return
    
    if n == 1:
        ans = max(ans, d)
    
    visited[n] = True
    
    for nn, nd in trees[n]:
        if visited[nn]:
            continue
        dfs(nn, d + nd, visited)
        
        
n = int(input())
parents = [False] * (n+1)
trees = defaultdict(list)
for _ in range(n-1):
    p, c, d = map(int, input().split())
    if not parents[p]:
        parents[p] = True
    trees[p].append((c, d))
    trees[c].append((p, d))

ans = 0
for i in range(1, n+1):
    if not parents[i]:
        visited = [False]*(n+1)
        visited[i] = True
        dfs(i, 0, visited)
print(ans)
