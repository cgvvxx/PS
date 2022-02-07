# Baekjoon 16973 - 직사각형 탈출
# Gold 4
# BFS/DFS


from collections import deque


def get_area(x, y):
    
    area = set()
    
    for i in range(-h+1, 1):
        for j in range(-w+1, 1):
            
            nx = x + i
            ny = y + j
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            area.add((nx, ny))
            
    return area


def bfs(sx, sy):
                
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny] or (nx, ny) in check:
                continue
                
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                
                if (nx, ny) == (fr-1, fc-1):
                    return True


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h, w, sr, sc, fr, fc = map(int, input().split())

blocks = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            blocks.append((i, j))

check = set()
for bi, bj in blocks:
    check |= get_area(bi, bj)

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

if bfs(sr-1, sc-1):
    print(graph[fr-1][fc-1])
else:
    print(-1)


# 장애물이 있는 1의 위치에 대해 상하좌우 h, w 높이의 정사각형이 들어갈 수 없는 좌표값들을 check 저장
# (sr, sc)에서 bfs를 시작하여 check를 제외한 좌표값들에 대해 (fr, fc)까지 최단거리 계산

# 초기의 check에 대해 맨 하단과 가장 우측에 대해 h, w에 대해 직사각형이 갈 수 없는 위치 초기화 해주어야 함
# ex)
# 4 5
# 0 0 0 0 0
# 0 0 1 0 0 
# 0 0 1 0 0
# 0 0 0 0 0
# 2 2 1 1 1 4
# >> -1