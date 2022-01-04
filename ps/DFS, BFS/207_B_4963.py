# Baekjoon 4963 - 섬의 개수
# Silver 2
# DFS/BFS


from collections import deque


def count_lands(graphs):
    
    def bfs(x, y):
    
        queue = deque()
        queue.append((x, y))
        visited[x][y] = True

        while queue:

            x, y = queue.popleft()

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy
                
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                    
                if visited[nx][ny]:
                    continue

                if graphs[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    
        return 1
    
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            
            if graphs[i][j] == 1 and not visited[i][j]:
                cnt += bfs(i, j)
                
    return cnt


while True:

    ans = 0
    w, h = map(int, input().split())

    if w == h == 0:
        break

    graphs = [list(map(int, input().split())) for _ in range(h)]
    
    print(count_lands(graphs))
    


# BFS를 통해 떨어져 있는 땅의 개수 찾기
# 이 때 대각선 방향도 하나의 땅으로 간주하는 것만 제외하면 기본적인 BFS