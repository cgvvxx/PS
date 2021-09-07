# Baekjoon 14923 - 미로 탈출
# Gold 4
# BFS/DFS


from collections import deque


def bfs(sx, sy):
    
    queue = deque()
    queue.append((sx-1, sy-1, 0))
    visited[sx-1][sy-1][0] = 1
    
    while queue:
        
        x, y, z = queue.popleft()
        
        if (x, y) == (ex-1, ey-1):
            return visited[x][y][z] - 1
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny][z] == 0:
                
                if graphs[nx][ny] == 0:
                    queue.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    
                if z == 0 and graphs[nx][ny] == 1:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    
    return -1


n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

print(bfs(sx, sy))


# 출발지점이랑 도착지점이 다른걸 제외하면 2206 벽 부수고 이동하기과 거의 같은 문제