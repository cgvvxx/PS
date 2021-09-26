# Baekjoon 20040 - 사이클 게임
# Gold 4
# Tree - UnionFind


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        

n, m = map(int, input().split())
parent = list(range(n))
visited = [False] * n

for i in range(m):
    a, b = map(int, input().split())
    if visited[a] + visited[b] and find(a) == find(b):
        print(i+1)
        break
    else:
        union(a, b)
        visited[a] = True
        visited[b] = True
else:  
    print(0)
    
    
# UnionFind를 이용해서 간선이 추가될 때마다 사이클이 되는지 체크하고 최초로 사이클이 될 때 break
# input을 받으면서 사이클이 만들어질 때 break를 해야되는 걸 몰라서 해맸음
# 기본적인 코드는 UnionFind 에서 크게 벗어나지 않음
# 다만 visited를 추가해서 이전에 방문했던 노드인 경우 parent를 확인해서 사이클인지 확인하는 부분을 추가