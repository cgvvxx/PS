# Baekjoon 7562 - 나이트의 이동
# Silver 2
# DFS/BFS


from collections import deque

def bfs(pos, tar):
    
    if pos == tar:
        return 0
    
    dirs = [
        (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)
    ]
    queue = deque()
    
    maps[pos[0]][pos[1]] = 1
    queue.append(pos)
    
    while queue:
        
        x, y = queue.popleft()
        
        for dx, dy in dirs:
            
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            
            if maps[nx][ny] == 0:
                
                if (nx, ny) == tar:
                    return maps[x][y]
                
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

                
for _ in range(int(input())):
    l = int(input())
    pos = tuple(map(int, input().split()))
    tar = tuple(map(int, input().split()))
    
    maps = [[0] * l for _ in range(l)]
    print(bfs(pos, tar))
    
    
# 기본적인 bfs에서 방향이 나이트와 같이 (2, !) ~ (-2, -1)로 총 8가지를 가짐
# 주어진 maps를 돌면서 그 위치에 갈 수 있는 최소 칸의 수를 기록