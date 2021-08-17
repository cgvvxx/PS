# Baekjoon 2178 - 미로 탐색
# Silver 1
# BFS/DFS


from collections import deque

def bfs():

    queue = deque()
    queue.append((0, 0))
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
                
            if not graphs[nx][ny]:
                continue
                
            if graphs[nx][ny] == 1:
                graphs[nx][ny] = graphs[x][y] + 1
                queue.append((nx, ny))
    
    
    return graphs[N-1][M-1]


N, M = map(int, input().split())
graphs = [list(map(int, input())) for _ in range(N)]

print(bfs())