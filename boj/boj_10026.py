# solved: [10026] 적록색약
# https://www.acmicpc.net/problem/10026
# graph-traversal, bfs
#
# Gold 5
# BFS를 통해 구역을 체크
# 이 때 일반적인 경우 'R', 'G', 'B'를 서로 다른 구역으로 계산하지만
# 적록색약인 경우 'R, G'와 'B'만 서로 다른 구역으로 계산
# 이를 위해 general_colors / red_green_colors라는 dictionary 활용


from collections import deque


def get_district(colors):
    
    def bfs(x, y):

        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        c = graphs[x][y]

        while queue:

            x, y = queue.popleft()

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if not visited[nx][ny] and graphs[nx][ny] in colors[c]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return 1
    
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt += bfs(i, j)

    return cnt


n = int(input())
graphs = [list(input()) for _ in range(n)]

general_colors = {'R': 'R', 'G': 'G', 'B': 'B'}
red_green_colors = {'R': {'R', 'G'}, 'G': {'R', 'G'}, 'B': 'B'}

print(get_district(general_colors), get_district(red_green_colors))
