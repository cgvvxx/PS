# Programmers - 게임 맵 최단거리
# Level 2
# DFS/BFS


from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    queue = deque()
    queue.append((0, 0))

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while queue:

        x, y = queue.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    last = maps[-1][-1]
    
    return -1 if last == 1 else last