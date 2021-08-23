# Baekjoon 11725 - 트리의 부모 찾기
# Silver 2
# 그래프 - 트리

#1. recursive function 이용한 dfs
#이 경우 재귀 깊이 제한을 건드려야함
#아이디어는 단순히 dfs를 이용하여 시작노드(1)부터 검색하고 시작노드가 다음 노드의 부모가 되도록 설정
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


def dfs(node):
    
    visited[node] = True
    
    for i in graphs[node]:
        if not visited[i]:
            parents[i] = node
            dfs(i)
            

n = int(input())

graphs = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)
    
parents = [0] * (n+1)
visited = [False] * (n+1)

dfs(1)

for i in parents[2:]:
    print(i)



#2. stack 이용한 dfs
# def dfs():
    
#     stack = [1]
#     visited[1] = True
    
#     while stack:
#         node = stack.pop()
#         for i in graphs[node]:
#             if not visited[i]:
#                 visited[i] = True
#                 parents[i] = node
#                 stack.append(i)
                           

# n = int(input())

# graphs = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b = map(int, input().split())
#     graphs[a].append(b)
#     graphs[b].append(a)
    
# parents = [0] * (n+1)
# visited = [False] * (n+1)

# dfs()

# for i in parents[2:]:
#     print(i)