# solved: [12837] 가계부 (Hard)
# https://www.acmicpc.net/problem/12837
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제
# 반복문을 이요한 세그먼트 트리 + 초기 init이 없이 update만 + update시 해당 값을 더하기(해당 값으로 바꾸기 X)

import sys
from math import ceil, log
input = sys.stdin.readline


def update(i, diff):
    i += size
    value = tree[i] + diff
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
    

n, q = map(int,input().split())

size = 2**ceil(log(n,2))
tree = [0]*(2*size)

for _ in range(q):
    a, b, c = map(int,input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(query(1, 0, size-1, b-1, c-1))
