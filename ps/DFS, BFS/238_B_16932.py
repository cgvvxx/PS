# Baekjoon 16932 - 모양 만들기
# Gold 4
# BFS/DFS


from collections import deque


def bfs(sx, sy, cat):
    
    queue = deque()
    queue.append((sx, sy))
    crds = set()
    crds.add((sx, sy))
    visited[sx][sy] = True
    cnt = 1
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny]:
                continue
                
            if graph[nx][ny] == 1:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
                crds.add((nx, ny))
    
    cat_dict[cat] = cnt
    
    while crds:
        x, y = crds.pop()
        graph[x][y] = cat


def sum_ones(x, y):
    
    cnt_sum = 0
    cat_set = set()
    
    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
            
        if graph[nx][ny] > 0 and graph[nx][ny] not in cat_set:
            cnt_sum += cat_dict[graph[nx][ny]]
            cat_set.add(graph[nx][ny])
            
    return cnt_sum


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
cnt_crds = [[], [], [], [], []]
cat_dict = dict()
cat = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] > 0 and not visited[i][j]:
            bfs(i, j, cat)
            cat += 1

ans = 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            ans = max(ans, sum_ones(i, j)+1)
print(ans)


# 각 1의 위치를 bfs로 cat으로 분류(1, 2, 3, ...)
# 각 cat에 해당하는 1의 개수를 cat_dict에 저장
# 모든 i, j를 돌면서 0인 경우 상하좌우의 cat에 대해 cat_dict을 활용하여 1의 개수의 합 계산