# solved: [1926] 그림
# https://www.acmicpc.net/problem/1926
# graph-traversal, bfs
#
# Silver 1
# bfs 기본 문제
# 주어진 그래프에서 1의 영역의 개수, 최대 영역의 크기


from collections import deque

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    area = 1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if visited[nx][ny]:
                continue
                
            if graph[nx][ny]:
                visited[nx][ny] = True
                area += 1
                queue.append((nx, ny))
    
    return area


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            ans = max(ans, bfs(i, j))
            
print(cnt)
print(ans)
