# Baekjoon 14502 - 연구소
# Gold 5
# DFS/BFS


from collections import deque
from itertools import combinations

def bfs(virus, visited):
    
    global count
    
    queue = deque()
    for x, y in virus:
        queue.append((x, y))
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graphs[nx][ny] == 1:
                continue

            if not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    

def count_virus(walls, virus):
    
    visited = [[False] * m for _ in range(n)]
    for i, j in walls:
        visited[i][j] = True
    for i, j in virus:
        visited[i][j] = True
        
    bfs(virus, visited)


n, m = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]

zero_walls = []
one_count = 0
two_virus = []
for i in range(n):
    for j in range(m):
        if graphs[i][j] == 0:
            zero_walls.append((i, j))
        elif graphs[i][j] == 1:
            one_count += 1
        else:
            two_virus.append((i, j))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
answer = 100
for walls in combinations(zero_walls, 3):
    count = len(two_virus)
    count_virus(walls, two_virus)
    if count < answer:
        answer = count
        
print(n*m - answer - one_count - 3)


# 맵의 크기가 최대 8*8=64이므로 단순히 BFS와 완전탐색으로 해결
# 1이 될수 있는(0인 칸)에서 3개의 모든 경우의 수에 대해서 2의 최대 크기를 구하고
# 2의 크기가 가장 작을 때가 0의 크기가 가장 큰 케이스가 됨
# 2의 크기를 기준으로 BFS함수를 정의했기 때문에 마지막에 0의 개수를 구하기 위해서 전체에서 2의 칸의 개수와 1의 칸의 개수를 뺌
# 조금 더 코드를 간결하게 수정할 수 있을 거 같긴 하지만 pass...
# python으로 3320 ms, pypy로 452 ms