# solved: [2268] 수들의 합 7
# https://www.acmicpc.net/problem/2268
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제
# 초기화 X + 재귀보다는 반복문 형태의 세그먼트 트리로 시간 단축 (pypy3로 해야 통과)

import sys
from math import ceil, log
input = sys.stdin.readline


def update(i, value):
    i += size
    tree[i] = value
    while i > 1:
        i //= 2
        tree[i] = tree[2*i] + tree[2*i+1]

def query(node, start, end, left, right):
    
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    return query(2*node, start, mid, left, right) + query(2*node+1, mid+1, end, left, right)
    
    
n, m = map(int,input().split())

size = 2**ceil(log(n,2))
tree = [0]*(2*size)

for _ in range(m):
    a, b, c = map(int,input().split())
    if a == 1:
        update(b-1, c)
    else:
        if b > c:
            b, c = c, b
        print(query(1, 0, size-1, b-1, c-1))
