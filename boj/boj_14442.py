# solved: [14442] 벽 부수고 이동하기 2
# https://www.acmicpc.net/problem/14442
# bfs, graph-traversal
#
# Gold 3
# 1. 3차원 배열을 이용하는 경우 n * m * k 차원의 배열을 만든 후
# k만큼 벽을 뚫는 경우 visited[k][x][y]에 그 값을 기록
# pypy3로 해야만 6632 ms로 겨우 통과
# 이 때 visited 체크를 잘 해줘야지 시간 초과가 안남..
#
# 2. 2차원 배열을 이용하는 경우 visited를 큰 값(9999)로 초기화 한후
# 각 좌표에 도착할 때의 k값의 최솟값을 visited에 기록하고
# 새로운 좌표를 방문할 때마다 t += 1을 하여 주어진 좌표에 도달하는 t를 return

#1. 3차원 배열 이용

from collections import deque
from sys import stdin
input = stdin.readline


def bfs():
    
    queue = deque()
    queue.append((0, 0, 0))
    
    while queue:
        
        x, y, z = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return visited[x][y][z]
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if graphs[nx][ny] == '0' and not visited[nx][ny][z]:
                queue.append((nx, ny, z))
                visited[nx][ny][z] = visited[x][y][z] + 1

            if graphs[nx][ny] == '1' and z < k and not visited[nx][ny][z+1]:
                queue.append((nx, ny, z+1))
                visited[nx][ny][z+1] = visited[x][y][z] + 1
                    
    return -1


n, m, k = map(int, input().split())
graphs = [list(input()) for _ in range(n)]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1] * (k+1)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(bfs())


#2. 2차원 배열 이용

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    
    if n == m == 1:
        return 1
    
    queue = deque()
    visited = [[9999 for _ in range(m)] for _ in range(n)]
    queue.append((0, 0, 1))
    visited[0][0] = 0
    
    while queue:
        
        x, y, t = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx, ny) == (n-1, m-1):
                return t+1
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            check = graphs[nx][ny] + visited[x][y]
            
            if check < visited[nx][ny] and check <= k:
                visited[nx][ny] = check
                queue.append((nx, ny, t+1))
                
    return -1


n, m, k = map(int, input().split())
graphs = [list(map(int, list(input().strip()))) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(bfs())
