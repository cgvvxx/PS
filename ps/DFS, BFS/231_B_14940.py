# Baekjoon 14940 - 쉬운 최단거리
# Gold 5
# BFS/DFS


from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    
    queue = deque()
    queue.append(start)
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
                
            if graph[nx][ny] == 0:
                continue
                
            if graph[nx][ny] == 1 and ans[nx][ny] < 0:
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx, ny))


m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

ans = [[-1] * n for _ in range(m) ]
for i in range(m):
    for j in range(n):
        if graph[i][j] == 2:
            start = (i, j)
            ans[i][j] = 0
        
        if graph[i][j] == 0:
            ans[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()

for row in ans:
    print(*row)


# 가장 기본적인 bfs
# ans라는 새로운 2차원 리스트를 만든 후 벽은 0 나머지는 -1로 초기화
# bfs를 돌면서 ans에 +1 씩