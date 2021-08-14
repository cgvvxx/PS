# Baekjoon 2573 - 빙산
# Gold 4
# DFS/BFS


from collections import deque
import sys
input = sys.stdin.readline


def is_splited(graph, ice):        

    def bfs(x, y):
        
        queue = deque()
        queue.append((x, y))
        
        while queue:
            
            x, y = queue.popleft()
            
            for i in range(4):
                
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                    
                if visited[nx][ny]:
                    continue
                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[True for _ in range(M)] for _ in range(N)]
    split_count = 0
    
    for ice_row, ice_col in ice:
        if graph[ice_row][ice_col] > 0:
            visited[ice_row][ice_col] = False
    
    for ice_row, ice_col in ice:
        if not visited[ice_row][ice_col]:
            bfs(ice_row, ice_col)
            split_count += 1
            if split_count >= 2:
                return True
    
    return False


def melt(graph, ice):
    
    def count_zero(x, y):
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        count = 0
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            
            if graphs[nx][ny] == 0:
                count += 1
        
        return count
    
    melted = []
    for ice_row, ice_col in ice:
        melted.append(count_zero(ice_row, ice_col))
    
    new_ice = []
    for idx in range(len(ice)):
        
        after = graph[ice[idx][0]][ice[idx][1]] - melted[idx]
        if after < 0:
            after = 0
        else:
            new_ice.append(ice[idx])
        graph[ice[idx][0]][ice[idx][1]] = after
    
    return graph, new_ice


def all_zero(graph, ice):
    
    for ice_row, ice_col in ice:
        if graph[ice_row][ice_col] != 0:
            return False
    
    return True


graphs = []
ices = []
N, M = map(int, input().split())
for row in range(N):
    this = list(map(int, input().split()))
    graphs.append(this)
    for col in range(len(this)):
        if this[col] != 0:
            ices.append((row, col))        

count = 0
while True:

    if all_zero(graphs, ices):
        print(0)
        break
    
    if is_splited(graphs, ices):
        print(count)
        break
    else:
        graphs, ices = melt(graphs, ices)
        count += 1
        