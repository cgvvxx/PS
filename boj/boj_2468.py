# solved: [2468] 안전 영역
# https://www.acmicpc.net/problem/2468
# dfs, graph-traversal
#
# Silver 1
# 주어진 그래프에서 h에 따른 떨어져 있는 영역의 개수 최댓값을 찾는 문제
# 가능한 모든 h에 대하여 dfs를 통해 떨어지지 않는 영역의 개수 count

def get_area(h):
    
    def dfs(x, y, h):
    
        visited[x][y] = True
        stack = [(x, y)]

        while stack:

            x, y = stack.pop()

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if visited[nx][ny]:
                    continue

                if graphs[nx][ny] > h:

                    visited[nx][ny] = True
                    stack.append((nx, ny))

        return 1
        
    visited  = [[False] * (n+1) for _ in range(n+1)]
    area = 0
    
    for i in range(n):
        for j in range(n):
            if graphs[i][j] > h and not visited[i][j]:
                area += dfs(i, j, h)
                
    return area


n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_h = max(sum(graphs, []))
ans = 1

for h in range(1, max_h):
    ans = max(ans, get_area(h))

print(ans)
