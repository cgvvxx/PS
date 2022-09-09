# solved: [11505] 구간 곱 구하기
# https://www.acmicpc.net/problem/11505
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제 + 곱하기로 변형
# 2042(구간 합 구하기)의 반복문 형태의 세그먼트 트리를 * 구조로만 변경
# 1000000007로 나눈 나머지 주의

import sys
from math import ceil, log
input = sys.stdin.readline


def init():
    for i in range(size-1, 0, -1):
        tree[i] = tree[2*i] * tree[2*i+1] % 1000000007

def update(i, value):
    i += size
    tree[i] = value
    while i > 1:
        i //= 2
        tree[i] = tree[2*i] * tree[2*i+1] % 1000000007

def query(node, start, end, left, right):
    
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    return query(2*node, start, mid, left, right) * query(2*node+1, mid+1, end, left, right)  % 1000000007
    
    
n, m, k = map(int,input().split())

size = 2**ceil(log(n,2))
tree = [0]*(2*size)

for i in range(n):
    tree[size+i] = int(input())
init()

for _ in range(m+k):
    a, b, c = map(int,input().split())
    if a == 1:
        update(b-1, c)
    else:
        print(query(1, 0, size-1, b-1, c-1))
