# Baekjoon 16234 - 인구 이동
# Gold 5
# BFS/DFS


from collections import deque


def bfs(sx, sy):
    
    global flag
    
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True
    pop_crds = set([(sx, sy)])
    pop_sum = graph[sx][sy]
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if visited[nx][ny]:
                continue
                
            if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                pop_sum += graph[nx][ny]
                pop_crds.add((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if len(pop_crds) >= 2:
        
        flag = True
        pops = pop_sum // len(pop_crds)
        while pop_crds:
            x, y = pop_crds.pop()
            graph[x][y] = pops


n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
flag = False
visited = [[False] * n for _ in range(n)]

while True:
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
    
    if flag:
        ans += 1
        visited = [[False] * n for _ in range(n)]
        flag = False
    else:
        break
        
print(ans)


# 주어진 격자에서 상하좌우로 l이상 r이하의 인구차이가 나는 좌표값을 pop_crds에 저장
# 각 격자들 방문체크하고 pop_crds에 저장된 인구수의 합의 평균을 저장된 좌표값들에 대해 할당
# 한번이라도 bfs()가 돌아가면 flag에 체크하여 반복
# flag가 false인 경우 while break
# 시간초과가 나서 pypy로 .. > 시간을 어떻게 줄이지?