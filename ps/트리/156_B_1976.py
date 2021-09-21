# Baekjoon 1976 - 여행 가자
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


n = int(input())
m = int(input())
parent = list(range(n))
i = 0

for _ in range(n):
    j = 0
    for k in map(int, input().split()):
        if k == 1:
            union(i, j)
        j += 1       
    i += 1
    
if len(set(map(lambda x:parent[x-1], map(int, input().split())))) == 1:
    print('YES')
else:
    print('NO')
    
    
# 주어진 그래프가 연결되어있는지 여부를 DFS나 BFS가 아닌 UnionFind로 해결
# 기본 UnionFind 구조에서의 함수 재활용