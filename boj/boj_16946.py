# solved: [16946] 벽 부수고 이동하기 4
# https://www.acmicpc.net/problem/16946
# bfs, graph-traversal
# 
# Gold 2
# 벽이 아닌 공간(0)이 차지하는 공간의 개수를 counts에 기록
# 이 때 서로 다른 counts를 구분하기 위해 (공간의 개수, id)로 저장
# 벽인 곳에서 상하좌우에 있는 서로 다른 counts의 개수의 합을 print


from collections import deque


def bfs(x, y, ids):
    
    queue = deque()
    queue.append((x, y))
    crds = {(x, y)}
    visited[x][y] = True
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if not graph[nx][ny] and not visited[nx][ny]:
                crds.add((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))

    cnt = len(crds)
    for i, j in crds:
        counts[i][j] = (cnt, ids)

def count_moves(x, y):
    
    if visited[x][y]:
        return 0
    
    ans = 1
    cats = set()
    
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
            
        if visited[nx][ny]:
            
            pop, cat = counts[nx][ny]
            
            if cat not in cats:
                ans += pop
                cats.add(cat)
            
    return ans % 10


n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
counts = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ids = 0
for i in range(n):
    for j in range(m):
        if not graph[i][j] and not visited[i][j]:
            bfs(i, j, ids)
            ids += 1

for i in range(n):
    for j in range(m):
        print(count_moves(i, j), end='')
    print(' ')
