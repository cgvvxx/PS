# Baekjoon 1717 - 집합의 표현
# Gold 4
# Tree - UnionFind


import sys
sys.setrecursionlimit(100000)


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
parent = list(range(n+1))

for _ in range(m):
    cat, a, b = map(int, input().split())
    if cat == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
            

# 기본적인 UnionFind 문제
# Find함수와 Union함수 구조 기억해 둘것! 
# 다만 이 문제의 경우 find의 재귀함수 구조 때문에 재귀 깊이를 늘려야 했음