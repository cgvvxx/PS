# solved: [2042] 구간 합 구하기
# https://www.acmicpc.net/problem/2042
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제
# 주어진 리스트에서 특정 인덱스 업데이트 및 구간 합 구하기

import sys
input = sys.stdin.readline


def init(node, start, end):
    
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(2*node, start, mid) + init(2*node+1, mid+1, end)
        return tree[node]
        
def update(node, start, end, idx, diff):
 
    if idx < start or idx > end :
        return
 
    tree[node] += diff
    
    if start != end :
        mid = (start + end) // 2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)
        
def query(node, start, end, left, right):
    
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    return query(2*node, start, mid, left, right) + query(2*node+1, mid+1, end, left, right)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0] * (4*n)
init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, n-1, b-1, diff)
    else:
        print(query(1, 0, n-1, b-1, c-1))
