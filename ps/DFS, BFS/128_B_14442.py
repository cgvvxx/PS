# Baekjoon 14442 - 벽 부수고 이동하기2
# Gold 3
# BFS/DFS


from collections import deque
import sys


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
            
            
            if visited[nx][ny][z] == 0:
                
                if graphs[nx][ny] == 0:
                    queue.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    
                if z < k and graphs[nx][ny] == 1:
                    queue.append((nx, ny, z+1))
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    
    return -1


n, m, k = map(int, sys.stdin.readline().split())
graphs = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

visited = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1] * (k+1)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(bfs())


# 2206 벽부수고 이동하기의 두 번째 버전
# 부술 수 있는 벽의 개수가 1개 > k개로 바뀜
# 아이디어는 벽부수고 이동하기와 똑같이 활용하였고 벽의 1개에서 k개로 바뀌었으므로
# 배열도 3차원 배열에서 k+2차원 배열로 바꾸어 각각 벽이 뚫린 개수에 해당하는 visited를 생성
# pypy여야지만 시간초과가 뜨지 않음