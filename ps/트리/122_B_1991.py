# Baekjoon 1991 - 트리 순회
# Silver 1
# 그래프 - 트리

import sys
input = sys.stdin.readline


def preorder(node):
    
    if node == '.':
        return
    
    pre_t.append(node)
    preorder(trees[node][0])
    preorder(trees[node][1])


def inorder(node):
    
    if node == '.':
        return
    
    inorder(trees[node][0])
    in_t.append(node)
    inorder(trees[node][1])
    

def postorder(node):
    
    if node == '.':
        return
    
    postorder(trees[node][0])
    postorder(trees[node][1])
    post_t.append(node)
    

n = int(input())

trees = dict()
for _ in range(n):
    p, lc, rc = input().split()
    trees[p] = [lc, rc]
    
    
node = 'A'
pre_t = []
in_t = []
post_t = []

preorder(node)
inorder(node)
postorder(node)

print(''.join(pre_t))
print(''.join(in_t))
print(''.join(post_t))

# 기본적인 트리 순회 - 전위순회, 중위순회, 후위순회
# recursive하게 순서만 잘 정해주면 됨