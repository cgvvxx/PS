# Baekjoon 7576 - 토마토
# Silver 1
# DFS/BFS 

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
                
            if graph[nx][ny] == -1:
                continue
                
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                

def sol(arr):
    
    arr_max = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
            
            if arr_max < arr[i][j]:
                arr_max = arr[i][j]
    
    return arr_max - 1


M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))
            
bfs()
print(sol(graph))