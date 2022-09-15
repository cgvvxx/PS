# solved: [1275] 커피숍2
# https://www.acmicpc.net/problem/1275
# segment-tree
# 
# Gold 1
# 세그먼트 트리 기본 문제 + 쿼리 합과 업데이트를 같이
# x > y일 때, y~x의 합을 구하는 부분 주의

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
        
def update(node, start, end, idx, value):
 
    if idx < start or idx > end :
        return
 
    tree[node] += value - arr[idx]
    
    if start != end :
        mid = (start + end) // 2
        update(node*2, start, mid, idx, value)
        update(node*2+1, mid+1, end, idx, value)
        
def query(node, start, end, left, right):
    
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    return query(2*node, start, mid, left, right) + query(2*node+1, mid+1, end, left, right)


n, q = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (4*n)
init(1, 0, n-1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(query(1, 0, n-1, x-1, y-1))
    update(1, 0, n-1, a-1, b)
    arr[a-1] = b
