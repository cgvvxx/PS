# solved: [10451] 순열 사이클
# https://www.acmicpc.net/problem/10451
# dfs, graph-traversal
#
# Silver 2
# 1부터 n까지 돌면서 이미 방문하지 않았다면 방문체크 하고 cnt += 1, stack에 push
# stack에 넣어진 경우 dfs를 통해 전체 사이클 방문체크

def count_cycle(n, arr):
    
    visited = [False] * (n+1)
    stack = []
    cnt = 0
    
    for i in range(1, n+1):
        
        if not visited[i]:
            stack.append(i)
            cnt += 1
        
        while stack:

            v = stack.pop()
            visited[v] = True
            
            nv = arr[v]
            if not visited[nv]:
                stack.append(nv)
               
    return cnt


for _ in range(int(input())):
    
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    
    print(count_cycle(n, arr))
