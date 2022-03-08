# Baekjoon 6087 - 레이저 통신
# Gold 4
# 최단 거리 - 0-1 BFS


from collections import deque


def bfs(x, y):
    
    queue = deque()
    queue.append((x, y, -1, -1))
    visited[x][y] = 1
    
    while queue:
        
        x, y, c, d = queue.popleft()
        
        if (x, y) == (tx, ty):
            return c
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
                
            if graphs[nx][ny] == '*':
                continue
            
            if not visited[nx][ny] or c <= visited[nx][ny]:
                
                visited[nx][ny] = c
                
                if d == i:
                    queue.appendleft((nx, ny, c, i))
                else:
                    queue.append((nx, ny, c+1, i))                


w, h = map(int, input().split())
graphs = [list(input()) for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*w for _ in range(h)]

tars = []
for i in range(h):
    for j in range(w):
        if graphs[i][j] == 'C':
            tars.append((i, j))
            
x, y = tars[0]
tx, ty = tars[1]

print(bfs(x, y))


# 0-1 bfs를 이용한 최단거리
# queue에는 현재 위치 nx, ny, 꺾은 횟수 c, 현재 방향 d를 append함
# 이 때 visited에는 각 위치에 도달하는 경우의 최소 꺾은 횟수를 기록
# 방문하지 않았거나(visited == 0) 또는 그 위치에 최소로 방문하는 경우(visited <= c) 
# 현재 진행방향과 같으면 (d==i) (nx, ny, c, i)를 deque에 앞단에 현재 진행방향과 다르면 (d != i) (nx, ny, c+1, i)를 deque에 뒷단에 삽입하면서 bfs 진행