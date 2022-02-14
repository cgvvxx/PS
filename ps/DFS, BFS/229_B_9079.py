# Baekjoon 9079 - 동전 게임
# Silver 4
# BFS/DFS


from collections import deque


def coin2num(c):
    
    if c == 'H':
        return 1
    else:
        return 0


def change_row(maps, n): # n번째 행
    
    n_maps = [[-1]*3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            if i == n:
                n_maps[i][j] = 1 - maps[i][j]
            else:
                n_maps[i][j] = maps[i][j]
    
    return n_maps


def change_col(maps, n): # n번째 열
    
    n_maps = [[-1]*3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            if j == n:
                n_maps[i][j] = 1 - maps[i][j]
            else:
                n_maps[i][j] = maps[i][j]
    
    return n_maps
        

def change_dig(maps, n): # 0 ; 우하향, 1 ; 우상향
    
    n_maps = [[-1]*3 for _ in range(3)]
    
    if n == 0:
        for i in range(3):
            for j in range(3):
                if i == j:
                    n_maps[i][j] = 1 - maps[i][j]
                else:
                    n_maps[i][j] = maps[i][j]
    else:
        for i in range(3):
            for j in range(3):
                if i == 2-j:
                    n_maps[i][j] = 1 - maps[i][j]
                else:
                    n_maps[i][j] = maps[i][j]
                    
    return n_maps


def maps2bin(maps):
    
    return int(''.join(map(str, sum(maps, []))), 2)


def is_valid(maps):
    
    if all(sum(maps, [])) or all(map(lambda x:1-x, sum(maps, []))):
        return True
    else:
        return False
    

def bfs(ms):
    
    if is_valid(ms):
        return 0
    
    queue = deque()
    queue.append((0, ms))
    
    while queue:
        
        cnt, ts = queue.popleft()
        
        for i in range(3):
            cs = change_row(ts, i)
            if not visited[maps2bin(cs)]:
                queue.append((cnt+1, cs))
                visited[maps2bin(cs)] = True
            if is_valid(cs):
                return cnt+1
            
        for j in range(3):
            cs = change_col(ts, j)
            if not visited[maps2bin(cs)]:
                queue.append((cnt+1, cs))
                visited[maps2bin(cs)] = True
            if is_valid(cs):
                return cnt+1
            
        for k in range(2):
            cs = change_dig(ts, k)
            if not visited[maps2bin(cs)]:
                queue.append((cnt+1, cs))
                visited[maps2bin(cs)] = True
            if is_valid(cs):
                return cnt+1
            
    return -1


for _ in range(int(input())):
    maps = [list(map(coin2num, input().split())) for _ in range(3)]
    visited = [False] * 2**9
    print(bfs(maps))


# 처음에 접근이 어려웠음
# 전체 경우의 수는 2**9이므로 단순히 완전탐색 + bfs로 시작
# bfs로 1. 행 바꾸는 경우, 2. 열 바꾸는 경우, 3 대각선 바꾸는 경우 총 8가지를 체크하면서 해도 사이즈가 충분히 작아 가능한 듯

# 체크해야할 반례 
# 1 
# H H H
# H H H
# H H H 
# >> 0