# solved: [1707] 이분 그래프
# https://www.acmicpc.net/problem/1707
# bfs, graph-traversal
# 
# Gold 4
# 이분 그래프(Bipartite Graph) : 그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있는 그래프
# bfs를 통해 현재 노드의 check값을 1, 다음 노드의 check값은 0(1 - check)를 주면서 진행
# 내 옆의 노드가 check 값이 일치하면 False를 return, 아니면 True를 return
# 이 때 분할되어 있는 그래프가 주어지는 경우 체크 해야함
# ex)
# 1
# 5 4
# 1 2
# 3 4
# 3 5
# 4 5

from queue import deque
import sys
input = sys.stdin.readline


def bfs(x):
    
    queue = deque()
    queue.append((x, 1))
    
    visited[x] = True
    checks[x] = 1
    
    while queue:
        
        y, check = queue.popleft()
        
        for z in graphs[y]:
            if not visited[z]:
                queue.append((z, 1-check))
                visited[z] = True
                checks[z] = 1 - check
            else:
                if checks[z] == check:
                    return False
    
    return True


for _ in range(int(input())):
    
    n, k = map(int, input().split())
    graphs = [[] for _ in range(n+1)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graphs[a].append(b)
        graphs[b].append(a)
        
    visited = [False] * (n+1)
    checks = [-1] * (n+1)
    
    for i in range(1, n+1):
        if not visited[i]:
            if not bfs(i):
                print('NO')
                break
    else:
        print('YES')
