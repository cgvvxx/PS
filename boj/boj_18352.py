# solved: [18352] 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352
# bfs, graph-traversal
#
# Silver 2
# queue에 현재 노드 n과 노드 까지의 거리 d를 append 해나가면서 d == k인 경우 ans에 append
# ans가 존재하면 sort후 return, 아니면 -1 return

from collections import deque
import sys
input = sys.stdin.readline

def bfs(a, d):
    
    queue = deque()
    queue.append((a, d))
    ans = []
    
    while queue:
        
        n, d = queue.popleft()
        
        if d == k:
            ans.append(n)
    
        for m in graphs[n]:   
            if not visited[m]:
                visited[m] = True
                queue.append((m, d+1))

    return ans
                
        
n, m, k, x = map(int, input().split())
graphs = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    
visited = [False] * (n+1)
visited[x] = True
ans = bfs(x, 0)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)

