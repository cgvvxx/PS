# Baekjoon 1922 - 네트워크 연결
# Gold 4
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


n = int(input())
m = int(input())
parent = list(range(n+1))

edges = []
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)


# 기본적인 MST 유형의 문제랑 똑같음
# 기존에 활용했던 kruskal 코드 재활용