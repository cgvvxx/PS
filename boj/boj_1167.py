# solved: [1167] 트리의 지름
# https://www.acmicpc.net/problem/1167
# dfs, graph-traversal, tree
# 
# Gold 2
# boj 1967 - 트리의 지름 참고
# 먼저 graphs에 각 노드에 연결된 노드와 길이의 정보를 tuple 형태로 저장
# 임의의 점에서 가장 멀리 떨어진 점을 구한 후, 그 점에서 다시 가장 멀리 떨어진 점까지의 거리를 한번 더 구하여 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(cur, dist):
    
    global max_dist, max_pos
    
    if dist > max_dist:
        max_dist = dist
        max_pos = cur
    
    for nxt, n_dist in graphs[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt, dist+n_dist)


n = int(input())
graphs = [[] for _ in range(n+1)]
for _ in range(n):
    
    v, *arrs = map(int, input().split())
    
    for i in range(0, len(arrs)-1, 2):
        nxt = arrs[i]
        dist = arrs[i+1]
        graphs[v].append((nxt, dist))

max_dist = 0
max_pos = 0

visited = [False] * (n+1)
visited[1] = True
dfs(1, 0)

visited = [False] * (n+1)
visited[max_pos] = True
dfs(max_pos, 0)

print(max_dist)
