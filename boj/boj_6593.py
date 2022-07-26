# solved: [6593] 상범 빌딩
# https://www.acmicpc.net/problem/6593
# bfs, graph-traversal
#
# Gold 5
# 기본적인 3차원 bfs 문제
# 특별한 아이디어는 없고, x, y, z 방향 주의할 것


from collections import deque

def bfs(aa, bb, cc):
    
    queue = deque()
    queue.append((aa, bb, cc))
    visited[aa][bb][cc] = 1
    
    while queue:
        
        x, y, z = queue.popleft()
        
        for i in range(6):
            
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if nx < 0 or ny < 0 or nz < 0 or nx >= l or ny >= r or nz >= c:
                continue
            
            if visited[nx][ny][nz]:
                continue
                
            if graphs[nx][ny][nz] == 'E':
                return True, visited[x][y][z]
            
            if graphs[nx][ny][nz] == '.':
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))
    
    return False, ''


def get_ans():
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graphs[i][j][k] == 'S':
                    tf, ck = bfs(i, j, k)
                    if tf:
                        print(f"Escaped in {ck} minutes(s).")
                    else:
                        print("Trapped!")
                    return


dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

while True:
    
    l, r, c = map(int, input().split())
    
    if l == r == c == 0:
        break
        
    graphs = [[list(input()) for _ in range(r+1)] for _ in range(l)]
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    
    get_ans()
