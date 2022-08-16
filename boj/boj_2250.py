# solved: [2250] 트리의 높이와 너비
# https://www.acmicpc.net/problem/2250
# dfs, graph-traversal, tree
# 
# Gold 2
# 중위 순회를 통해 탐색하였을 때 나오는 노드의 순서가 각 노드의 x좌표가 된다
# 각 깊이(depth) 별로 처음 나오는 x의 위치와 가장 마지막에 나오는 x의 위치를 저장
# 각 깊이 별로 가장 마지막에 나오는 x의 위치 - 가장 처음 나오는 x의 위치의 차이가 가장 큰 경우를 출력
# 이 때, 루트 노드는 1이 아님을 주의

import sys
input = sys.stdin.readline

def dfs(cur, depth):
    
    global x
    
    if cur == -1:
        x += 1
        return 1
    
    dfs(graphs[cur][0], depth+1)
    if not left[depth]:
        left[depth] = x
    right[depth] = x
    dfs(graphs[cur][1], depth+1)

    return x


n = int(input())

is_root = [True] * (n+1)
is_root[0] = False
graphs = [[] for _ in range(n+1)]
for _ in range(n):
    m, l, r = map(int, input().split())
    if l != -1:
        is_root[l] = False
    if r != -1:
        is_root[r] = False
    graphs[m] += [l, r]
    
root = is_root.index(True)

x = 0
left = [0] * (n+1)
right = [0] * (n+1)
dfs(root, 1)

max_width = -1
max_level = -1
for i in range(1, n+1):
    
    if (left[i], right[i]) == (0, 0):
        break
    
    width = right[i] - left[i] + 1
    if max_width < width:
        max_width = width
        max_level = i
        
print(max_level, max_width)
