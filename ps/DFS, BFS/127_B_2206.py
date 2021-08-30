# Baekjoon 2206 - 벽 부수고 이동하기
# Gold 4
# BFS/DFS


from collections import deque


# def p(v):
    
#     for x in range(n):
#         a = [v[x][y][0] for y in range(m)]
#         b = [v[x][y][1] for y in range(m)]
#         print(a, '  ', b)
        

def bfs():
    
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while queue:
        
        x, y, z = queue.popleft()
        
#         print(x, y, z)
#         p(visited)
        
        if (x, y) == (n-1, m-1):
            return visited[x][y][z]
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            if visited[nx][ny][z] == 0:
                
                if graphs[nx][ny] == 0:
                    queue.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    
                if z == 0 and graphs[nx][ny] == 1:
                    queue.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][z] + 1
                    
    return -1


n, m = map(int, input().split())
graphs = [list(map(int, list(input()))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

print(bfs())


# bfs 문제에 벽을 하나 부술 수 있다는 조건이 추가되어서 어려워진 문제
# 벽을 뚫었는지 여부를 주는 boolean 변수를 이용하여 풀려고 했지만 실패
# visited를 3차원 배열로 만들어서 벽을 뚫지 않고 온 경우의 최단경로횟수와
# 벽을 뚫고 온 경우의 최딘경로횟수를 각각 저장해서 풀어야 하는듯
# p함수를 이용해서 각 단계별로 visited에 어떻게 저장되는지 확인할 수 있음
# 참고 할 만한 반례1)
# 0000
# 0100
# 0000
# 1111
# 0000