# solved: [2583] 영역 구하기
# https://www.acmicpc.net/problem/2503
# bfs, graph-traversal

# Silver 2
# 직사각형에 해당하는 부분 1로 채우기 > 1로 구분되어지는 영역 bfs로 count

from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x, y))
    cnt = 1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny]:
                continue
                
            graph[nx][ny] = 1
            cnt += 1
            queue.append((nx, ny))
    
    return cnt


m, n, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            graph[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            graph[i][j] = 1
            ans.append(bfs(i, j))
ans.sort()

print(len(ans))
print(*ans)
