# Baekjoon 13565 - 침투
# Silver 2
# DFS/BFS


from collections import deque

def bfs():
    
    queue = deque()
    
    for j in range(n):
        if graphs[0][j] == 0:
            queue.append((0, j))
            graphs[0][j] = 1
    
    while queue:
        
        x, y = queue.popleft()
        
        for dx, dy in dirs:
            
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            if graphs[nx][ny] == 0:
                queue.append((nx, ny))
                graphs[nx][ny] = 1
                
                if nx == m-1:
                    return 'YES'
    
    return 'NO'


m, n = map(int, input().split())
graphs = [list(map(int, list(input()))) for _ in range(m)]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
print(bfs())
    

# x = 0인 곳에서 시작, x = m인 곳에서 끝날 수 있으면 YES 아니면 NO
# 사실 dfs로 짜면 더 빠를듯..