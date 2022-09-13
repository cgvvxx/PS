# solved: [2357] 최솟값과 최댓값
# https://www.acmicpc.net/problem/2357
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제 + 최소최대로 변형
# 세그먼트 트리의 각 노드에 해당 구간에 대한 [최솟값, 최댓값]을 리스트로 저장하면서 init

import sys
input = sys.stdin.readline


def init(node, start, end):
    
    if start == end:
        
        tree[node] = [arr[start], arr[start]]
        return tree[node]
    
    else:
        
        mid = (start + end) // 2
        a = init(2*node, start, mid)
        b = init(2*node+1, mid+1, end)
        
        tree[node][0] = min(a[0], b[0])
        tree[node][1] = max(a[1], b[1])
        
        return tree[node]
        
def query(node, start, end, left, right):
    
    if left > end or right < start:
        return [1000000001, 0]
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    a = query(2*node, start, mid, left, right)
    b = query(2*node+1, mid+1, end, left, right)
    
    return [min(a[0], b[0]), max(a[1], b[1])]


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [[1000000001, 0] for _ in range(4*n)]
init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*query(1, 0, n-1, a-1, b-1))
