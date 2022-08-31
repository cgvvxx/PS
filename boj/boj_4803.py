# solved: [4803] 트리
# https://www.acmicpc.net/problem/4803
# dfs, graph-traversal, tree
# 
# Gold 4
# 주어진 그래프에서 트리의 개수를 세는 문제
# dfs를 통해 주어진 노드를 찾아가면서 해당 node가 부모 노드 말고도 나오면 no_tree = True로 주어서 트리 체크 X
# 아닌 경우는 dfs 진행하면서 하나의 트리로 체크

import sys
input = sys.stdin.readline

def dfs(cur, bfr):
    
    global no_tree
    
    for nxt in graphs[cur]:
        if nxt != bfr:
            if visited[nxt]:
                no_tree = True
            else:
                visited[nxt] = True
                dfs(nxt, cur)


case = 0
while True:
    
    n, m = map(int, input().split())
    case += 1 
    
    if (n, m) == (0, 0):
        break
    
    graphs = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)
        
    cnt = 0
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            no_tree = False
            cnt += 1
            dfs(i, 0)
            if no_tree:
                cnt -= 1
    
    if cnt == 0:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')
