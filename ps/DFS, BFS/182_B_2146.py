# Baekjoon 2146 - 다리 만들기
# Gold 3
# BFS/DFS


from collections import deque

def bfs(x, y):
    
    queue = deque()
    queue.append((x, y))
    lands = {(x, y)}
    
    while queue:
        
        x, y = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
                
            if visited[nx][ny]:
                continue
                
            if graphs[nx][ny] == 1:
                lands.add((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True
    
    return lands


def taxi_dist(x, y):
    
    return abs(x[0]-y[0])+abs(x[1]-y[1])-1


def get_shortest_dist(l1, l2):
    
    dist = 10**6
    
    for i in range(len(l1)):
        for j in range(len(l2)):
            ij_dist = taxi_dist(l1[i], l2[j])
            if ij_dist < dist:
                dist = ij_dist
    
    return dist


def is_shore(x, y):
    
    if x - 1 >= 0 and graphs[x-1][y] == 0:
        return True
    elif x + 1 < n and graphs[x+1][y] == 0:
        return True
    elif y - 1 >= 0 and graphs[x][y-1] == 0:
        return True
    elif y + 1 < n and graphs[x][y+1] == 0:
        return True
    else:
        return False
    

def get_shore(l):
    
    new_l = []
    
    while l:
        
        check = l.pop()
        
        if is_shore(*check):
            new_l.append(check)
            
    return new_l


n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
lands = []

for i in range(n):
    for j in range(n):
        if graphs[i][j] == 1 and not visited[i][j]:
            land = bfs(i, j)
            if land:
                lands.append(get_shore(land))
            
dist = 10**6
for i in range(len(lands)):
    for j in range(i+1, len(lands)):
        ij_dist = get_shortest_dist(lands[i], lands[j])
        if ij_dist < dist:
            dist = ij_dist
            
print(dist)


# 먼저 육지(1)의 좌표로된 set의 리스트를 구한 후 해안가와 맞닿아 있는 육지의 좌표에 대하여
# 다른 육지와의 택시거리가 가장 짧은 값을 완전탐색으로 구함  >>  pypy로만 통과
# 각 육지에 대해서 bfs로 다른 육지와의 거리를 구하는게 일반적인듯.. 시간도 더 빠르고..