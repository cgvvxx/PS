# solved: [18405] 경쟁적 전염
# https://www.acmicpc.net/problem/18405
# bfs, graph-traversal
#
# Gold 5
# queue에 현재 위치 nx, ny와 시작 위치부터의 거리 t를 append
# target 위치에서부터 bfs를 시작하여 거리가 t가 s 이하 일때만 체크
# 이 때, graph[nx][ny]가 0이 아닌 값을 만나면 s = t로 업데이트하여 해당 거리까지의 모든 좌표 확인

from collections import deque

def bfs(x, y, t):
    
    global s

    queue = deque()
    queue.append((x, y, t))
    ans = []
    
    while queue:
        
        x, y, t = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                
            if visited[nx][ny]:
                continue
                
            if t > s:
                continue
                
            visited[nx][ny] = True
               
            if graph[nx][ny] == 0:
                queue.append((nx, ny, t+1))
                continue
                
            s = t
            ans.append(graph[nx][ny])
    
    return ans
                

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

visited = [[False] * n for _ in range(n)]
visited[x-1][y-1] = True
if graph[x-1][y-1]:
    print(graph[x-1][y-1])
else:
    ans = bfs(x-1, y-1, 1)
    if ans:
        print(min(ans))
    else:
        print(0)
