# solved: [16437] 양 구출 작전
# https://www.acmicpc.net/problem/16437
# dfs, graph-traversal, tree
# 
# Gold 3
# dfs를 통해 재귀적으로 트리 탐색
# 이 때, 리프 노드에서 현재 노드까지의 양의 수(늑대라면 -)를 양수 일 떄만 return
# 참고) 늑대는 일생동안 최대 한 마리의 양만 잡아먹는다
# 7
# W 10 1
# W 40 2
# W 10 2
# S 100 3
# S 50 3
# S 20 4
# 답> 110


import sys
sys.setrecursionlimit(130000)
input = sys.stdin.readline

def dfs(n):
    
    a = animals[n]
    for c in graphs[n]:
        if not visited[c]:
            visited[c] = True
            a += dfs(c)

    return a if a > 0 else 0


n = int(input())
graphs = [[] for _ in range(n+1)]

animals = [0] * (n+1)
for i in range(n-1):
    
    t, a, p = input().split()
    if t == 'W':
        animals[i+2] = -int(a)
    else:
        animals[i+2] = int(a)
        
    graphs[i+2].append(int(p))
    graphs[int(p)].append(i+2)

visited = [False] * (n+1)
visited[1] = True
print(dfs(1))
