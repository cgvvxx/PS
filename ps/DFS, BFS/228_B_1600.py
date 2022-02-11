# Baekjoon 1600 - 말이 되고픈 원숭이
# Gold 4
# BFS/DFS


from collections import deque


def bfs():
    
    queue = deque()
    queue.append((0, 0, k))
    visited[0][0][0] = 1
    
    while queue:
        
        x, y, z = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return visited[x][y][z]
        
        for dx, dy in walk:
            
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny][z] == 0 and graphs[nx][ny] == 0:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1
        
        if z:
            
            for dx, dy in horse:

                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                if visited[nx][ny][z-1] == 0 and graphs[nx][ny] == 0:
                    queue.append((nx, ny, z-1))
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    
    return -1


k = int(input())
m, n = map(int, input().split())
graphs = [list(map(int, list(input().split()))) for _ in range(n)]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
walk = [(0, 1), (1, 0), (0, -1), (-1, 0)]
horse = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

print(bfs())


# 2206 - 벽 부수고 이동하기와 비슷한 문제
# 이 때 벽 부수고 이동하기는 하나의 벽을 count해야 하기 때문에 z = 2지만
# 이 문제의 경우 k번의 말의 움직임을 할 수 있으므로 z = k+1
# visietd[x][y][z]는 말의 움직임을 z번 할 수 있을 때의 (x, y)로의 최단거리 