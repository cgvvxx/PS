# Baekjoon 2638 - 치즈
# Gold 4
# BFS/DFS


def dfs(x, y):
    
    visited[x][y] = True
    
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if visited[nx][ny]:
            continue
            
        if arr[nx][ny] == 1:
            contacted[nx][ny] += 1
            continue
            
        if arr[nx][ny] == 0:
            visited[nx][ny] = True
            dfs(nx, ny)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

times = 0
while True:
    
    count = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    contacted = [[0 for _ in range(m)] for _ in range(n)]
    dfs(0, 0)
    is_empty = True

    for i in range(n):
        for j in range(m):
            if contacted[i][j] >= 2:
                is_empty = False
                arr[i][j] = 0

    if is_empty:
        break
        
    times += 1

print(times)

# 2636의 연장선, 이 문제는 접촉면이 두 개 이상일 때만 녹는다는 조건이 추가된거라
# contacted라는 배열을 추가하여 외부 공기와 접촉 횟수를 체크하고 2보다 클 때 없어지도록 함
# 마찬가지로 재귀함수 형태로 풀어서 재귀 깊이 설정을 해야함