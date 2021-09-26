# Baekjoon 14621 - 나만 안되는 연애
# Gold 3
# Tree - MST


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
        
v, e = map(int, input().split())
is_mw = list(input().split())
parent = list(range(v+1))

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if is_mw[a-1] == is_mw[b-1]:
        continue
    
    if find(a) != find(b):
        union(a, b)
        result += cost

check = find(1)
for i in range(2, v+1):
    if check != find(i):
        print(-1)
        break
else:
    print(result)
    
    
# MST + 노드의 종류가 2가지로 구분되어 있고 + 마지막에 spanning tree가 만들어지지 않는 case도 살펴봐야함
# 1. 노드는 항상 서로 다른 종류의 노드끼리만 이어져 있어야 하는 부분
# 2. spanning tree가 만들어지지 않는 case 체크하는 부분
# 1, 2만 추가함