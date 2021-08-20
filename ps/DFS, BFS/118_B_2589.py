# Baekjoon 2589 - 보물섬
# Gold 5
# BFS/DFS


from collections import deque


def bfs(sx, sy, visited):    
    
    queue = deque()
    queue.append((sx, sy))
    max_route = 0
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if not visited[nx][ny]:
                continue

            if visited[nx][ny] == 1 and (nx, ny) != (sx, sy):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
                if visited[nx][ny] > max_route:
                    max_route = visited[nx][ny]
    
    return max_route - 1


def check_land(x, y):
    
    count = 0
    
    for i in range(4):
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
        if graphs[nx][ny] == 'L':
            count += 1
    
    return count


n, m = map(int, input().split())
graphs = [list(input()) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
max_list = []
is_max = 0

for i in range(n):
    for j in range(m):
        visited = [[0 if graphs[x][y] == 'W' else 1 for y in range(m)] for x in range(n)]
        if visited[i][j] == 1 and check_land(x, y) <= 2:
            result = bfs(i, j, visited)
            if is_max < result:
                is_max = result

print(is_max)


# try1 ; 처음 나오는 L을 기준으로 가장 먼 거리의 있는 L을 체크하고 그 L에 대해서 다시 bfs로 가장 먼 길이 체크
# 가장 먼 거리에 있는 L이 최장거리가 아닐 수 있음
# 반례 > 
# WLLLLLW
# LWLWLWW
# LLLWLWW
# LWWWLWW
# LLLLLWW
# LWWWWWW
# try2 ; 그냥 모든 L에 대해서 bfs를 돌리고 최장거리를 체크해서 그 중의 max값을 return
# python3 로 돌리면 시간초과나서 pypy로 돌려보니 통과는 함 (840 ms)
# try3 ; 각각의 L에 대해서 주위의 있는(상하좌우) L의 개수가 2개 이하일 때만 bfs를 돌리고 최장거리르 체크
# python3 로도 통과 (2380 ms)
# (3개 이하로도 통과는함 4068ms)

# 단순 brute force와 pypy로 풀리는게 조금 허무함..
# brute force가 아닌 방법으로 풀기위해서 고민하는 시간이 길었음
