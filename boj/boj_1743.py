# solved: [1743] 음식물 피하기
# https://www.acmicpc.net/problem/1743
# dfs, graph-traversal
#
# Silver 1
# 주어진 그래프에서 이어져있는 가장 큰 영역의 크기를 찾는 문제
# 간단히 dfs를 이용해서 방문하지 않은 곳만 체크하면서 area += 1

def dfs(x, y):
    
    visited[x][y] = True
    stack = [(x, y)]
    area = 1
    
    while stack:
        
        x, y = stack.pop()
    
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n or ny > m:
                continue

            if visited[nx][ny]:
                continue

            if graphs[nx][ny]:

                visited[nx][ny] = True
                stack.append((nx, ny))
                area += 1
            
    return area


n, m, k = map(int, input().split())

graphs = [[0] * (m+1) for _ in range(n+1)]
for _ in range(k):
    r, c = map(int, input().split())
    graphs[r][c] = 1
    
visited  = [[False] * (m+1) for _ in range(n+1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 0
for i in range(n+1):
    for j in range(m+1):
        if graphs[i][j] and not visited[i][j]:
            ans = max(ans, dfs(i, j))
print(ans)
