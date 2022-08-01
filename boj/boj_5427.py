# solved: [5427] 불
# https://www.acmicpc.net/problem/5427
# graph-traversal, bfs
#
# Gold 4
# 상근이의 위치와 불의 위치를 각각 bfs를 통해 진행해나가면서 상근이가 빌딩 밖으로 나갈 수 있는지 체크
# 상근이의 위치는 visited, 불의 위치는 impossible에 저장해나가면서 상근이가 갈 수 있는 위치 체크
# 현재 상근이의 위치에 불이 덮쳐서 못나가는 경우 체크
# 반례)
# 1
# 3 3
# ###
# #@.
# ##*

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, impossible, visited, f_queue):
    
    p_queue = deque()
    p_queue.append((x, y))
    s = 0
    
    while p_queue:
        
        s += 1
        for _ in range(len(p_queue)):
            
            x, y = p_queue.popleft()

            if impossible[x][y]:
                continue
            
            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    return s

                if impossible[nx][ny] or visited[nx][ny]:
                    continue

                if graph[nx][ny] == '.':

                    visited[nx][ny] = True
                    p_queue.append((nx, ny))
        
        if not p_queue:
            return 'IMPOSSIBLE'
        
        for _ in range(len(f_queue)):
            
            x, y = f_queue.popleft()

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue

                if impossible[nx][ny]:
                    continue

                if graph[nx][ny] == '.':
                    impossible[nx][ny] = True
                    f_queue.append((nx, ny))
    
    return 'IMPOSSIBLE'


def is_possible(n, m, graph):
    
    f_queue = deque()
    impossible = [[False] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if graph[i][j] == '@':
                start = (i, j)
                visited[i][j] = True
            elif graph[i][j] == '*':
                f_queue.append((i, j))
                impossible[i][j] = True
            elif graph[i][j] == '#':
                impossible[i][j] = True

    print(bfs(*start, impossible, visited, f_queue))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(m)]
    is_possible(n, m, graph)
