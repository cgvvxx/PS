# Baekjoon 11123 - 양 한마리... 양 두마리...
# Silver 1
# BFS/DFS


from collections import deque


def dfs(x, y, graphs):
    
    queue = deque()            
    queue.append((x, y))
    
    while queue:
        
        x, y = queue.popleft()
        graphs[x][y] = '.'
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                    
            if graphs[nx][ny] == '.':
                continue
                
            if graphs[nx][ny] == '#':
                graphs[nx][ny] = '.'
                queue.append((nx, ny))


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    graphs = [list(input()) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graphs[i][j] == '#':
                dfs(i, j, graphs)
                count += 1
    print(count)