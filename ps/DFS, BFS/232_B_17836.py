# Baekjoon 17836 - 공주님을 구해라!
# Gold 5
# BFS/DFS


from collections import deque


def bfs(start):
    
    global sword
    
    queue = deque()
    queue.append(start)
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny] or graph[nx][ny] == 1:
                continue
                
            if graph[nx][ny] == 2:
                sword = abs(nx-n+1) + abs(ny-m+1) + graph[x][y] + 1
                
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))
            
    return graph[n-1][m-1]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

sword = 10**5
walk = bfs((0, 0))
if not visited[n-1][m-1]:
    walk = 10**5

if walk <= t or sword <= t:
    print(min(walk, sword))
else:
    print('Fail')


# 기본적인 격자 형태의 graph에 대한 bfs
# 이 때 검(2)을 만나면 sword에 현재 위치와 마지막 위치 (n-1, m-1) 까지의 택시 거리를 저장
# 미로를 걸어서 가는 경우와 sword를 만나서 가는 경우의 최솟값을 print
# 둘 다 불가능한 경우 Fail

# 마지막 위치 (n-1, m-1)가 벽인 경우 walk는 존재하지 않으므로 visited인지 체크
# ex)
# 4 4 100
# 0 1 1 1
# 0 1 2 0
# 0 0 0 0
# 1 1 1 1