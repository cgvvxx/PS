# solved: [4256] 트리
# https://www.acmicpc.net/problem/4256
# divide-and-conquer, tree
# 
# Gold 2
# 이진 트리에서 전위 순회, 중위 순회한 결과가 주어질 때 후위 순회한 결과를 출력하는 문제
# (boj 2263 - 트리의 순회) 참고
# 이 때, 이 문제는 여러 케이스를 출력해야하므로, 정답을 ans에 저장 후 출력해야함
# (바로 print와 end=' '로 출력하면 '출력 형식이 잘못되었습니다')

import sys
input = sys.stdin.readline

def dq(i_s, i_e, p_s, p_e):
    
    if i_s >= i_e - 1:
        if i_s == i_e - 1:
            ans.append(inorder[i_s])
        return
    
    root = preorder[p_s]
    i_root = pos[root]
    
    dq(i_s, i_root, p_s + 1, p_s + i_root - i_s + 1)
    dq(i_root+1, i_e, p_s + i_root - i_s + 1, p_e)
    ans.append(root)


for _ in range(int(input())):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    
    pos = [0]*(n+1)
    for i in range(n):
        pos[inorder[i]] = i
        
    ans = []
    dq(0, n, 0, n)
    print(*ans, sep=' ')
