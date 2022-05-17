# solved: [2665] 미로만들기
# https://www.acmicpc.net/problem/2665
# bfs, graph-traversal
#
# Gold 4
# 1261 알고스팟과 동일한 문제 > 0-1 bfs를 이용한 최단거리
# 벽이 없는 경우(1) deque에 앞단에 c를, 벽이 있는 경우(0) deque에 뒷단에 c+1을 삽입하며 bfs 진행

from collections import deque


def bfs(x, y, c):
    
    queue = deque()
    queue.append((x, y, c))
    visited[x][y] = True
    
    while queue:
        
        x, y, c = queue.popleft()
        
        if (x, y) == (n-1, n-1):
            return c
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if not visited[nx][ny]:
                
                visited[nx][ny] = True
                
                if graphs[nx][ny]:
                    queue.appendleft((nx, ny, c))
                else:
                    queue.append((nx, ny, c+1))

n = int(input())
graphs = [list(map(int, list(input()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False]*n for _ in range(n)]

print(bfs(0, 0, 0))
