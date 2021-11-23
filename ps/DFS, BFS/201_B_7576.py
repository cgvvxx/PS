# Baekjoon 7569 - 토마토
# Silver 1
# DFS/BFS


from collections import deque


def bfs():
    
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while queue:
        
        z, y, x = queue.popleft()
        
        for i in range(6):
            
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                continue
                
            if graph[nz][ny][nx] == -1:
                continue
                
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))
                

def sol(arr):
    
    arr_max = -1
    for i in range(M):
        for j in range(N):
            for k in range(H):
                if arr[k][j][i] == 0:
                    return -1
            
                if arr_max < arr[k][j][i]:
                    arr_max = arr[k][j][i]
    
    return arr_max - 1


M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

for i in range(M):
    for j in range(N):
        for k in range(H):
            if graph[k][j][i] == 1:
                queue.append((k, j, i))
            
bfs()
print(sol(graph))


# 7576 토마토의 3차원 버전
# 기본적인 로직은 7576 bfs와 같지만 graph가 3차원만 다름!
# 이 때 M, N, H로 for문을 i, j, h로 돌리면 graph[k][j][i] 순으로 graph를 input으로 받을 때 달라진다는 점 주의