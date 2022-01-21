# Baekjoon 22856 - 트리 순회
# Gold 4
# DFS/BFS


import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

        
def dfs(v, d):
    
    for i in trees[v]:
        if i not in visited and i != -1:
            visited.add(i)
            depth[i] = d
            dfs(i, d+1)

            
def inorder(node):
    
    if node != -1:
        inorder(trees[node][0])
        route.append(node)
        inorder(trees[node][1])

         
n = int(input())
trees = [[] for _ in range(n+1)]

for _ in range(n):
    a, b, c = map(int, input().split())
    trees[a] = [b, c]
    
visited = set()
depth = {1: 0}
route = [1]

dfs(1, 1)
inorder(1)

dist = 0
for j in range(1, len(route)):
    dist += abs(depth[route[j]] - depth[route[j-1]])
print(dist)


# 재귀를 이용한 dfs + 트리의 중위 순회
# dfs로 depth의 각 node의 깊이를 구한 후
# 중위 순회로 나온 노드의 순서에 대해서 각 노드의 깊이 차이의 합을 return