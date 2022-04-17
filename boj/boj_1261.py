# solved: [1261] 알고스팟
# https://www.acmicpc.net/problem/1261
# bfs, graph-traversal
#
# Gold 4
# 0-1 bfs를 이용한 최단거리
# 벽이 없는 경우(0) deque에 앞단에 c를, 벽이 있는 경우(1) deque에 뒷단에 c+1을 삽입하며 bfs 진행

from collections import deque


def bfs(x, y, c):
    
    queue = deque()
    queue.append((x, y, c))
    visited[x][y] = True
    
    while queue:
        
        x, y, c = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return c
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if not visited[nx][ny]:
                
                visited[nx][ny] = True
                
                if graphs[nx][ny]:
                    queue.append((nx, ny, c+1))
                else:
                    queue.appendleft((nx, ny, c))


m, n = map(int, input().split())
graphs = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*m for _ in range(n)]

print(bfs(0, 0, 0))
