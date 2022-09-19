# solved: [24479] 알고리즘 수업 - 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479
# dfs, graph-traversal, sorting
# 
# Silver 2
# dfs 기본 문제
# 방문한 순서의 노드를 출력하는게 아니라 해당 노드 방문 순서를 출력하는 부분 주의
# recursion 200000 보다 크게 해야 재귀 오류 안남

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)

def dfs(r):
    
    global c
    
    visited[r] = True
    order[r] = c
    c += 1
    
    for w in sorted(graphs[r]):
        if not visited[w]:
            dfs(w)


n, m, r = map(int, input().split())
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
    
visited = [False] * (n+1)
order = [0] * (n+1)
c = 1
dfs(r)

for i in range(1, n+1):
    print(order[i])
