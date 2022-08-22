# solved: [2263] 트리의 순회
# https://www.acmicpc.net/problem/2263
# divide-and-conquer, tree
# 
# Gold 2
# 후위 순회의 마지막 수는 항상 루트 노드이므로 분할정복을 이용하여 루트 노드를 기점으로 
# 왼쪽 트리, 오른쪽 트리의 전위 순회 결과를 출력하도록 함
# 먼저 중위 순회의 인덱스를 담는 pos를 저장
# 분할정복에서는 왼쪽 트리, 오른쪽 트리의 인덱스를 넘기면서 재귀적으로 구현(리스트를 넘기면 메모리초과)
# 중위 순회에서 왼쪽 트리, 오른쪽 트리는 루트 노드를 기준으로 구분되지만
# 후위 순회에서 왼쪽 트리, 오른쪽 트리는 중위 순회에서 구한 왼쪽 트리의 개수 만큼 띄어서 넘겨주어야 함

import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def dq(i_s, i_e, p_s, p_e):
    
    if i_s >= i_e - 1:
        if i_s == i_e - 1:
            print(inorder[i_s], end=' ')
        return
    
    root = postorder[p_e-1]
    i_root = pos[root]
    
    print(root, end=' ')
    dq(i_s, i_root, p_s, p_s + i_root - i_s)
    dq(i_root+1, i_e, p_s + i_root - i_s, p_e-1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i
dq(0, n, 0, n)
