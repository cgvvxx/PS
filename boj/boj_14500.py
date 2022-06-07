# solved: [14500] 테트로미노
# https://www.acmicpc.net/problem/14500
# backtracking, bruteforcing, dfs, graph-traversal
# 
# Gold 5
# dfs를 통해 4칸 만큼 나아갔을 때의 최댓값을 update하면서 나감
# 단, ㅗ 모양은 dfs를 통해 만들 수 없으므로 t_shape 함수를 이용하여 체크

import sys
input = sys.stdin.readline

def dfs(x, y, tet, cnt, visited):
    
    global ans

    if cnt == 3:
        ans = max(ans, tet)
        return 
    
    for dx, dy in dirs:
        
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
            
        if (nx, ny) in visited:
            continue
        
        dfs(nx, ny, tet+maps[nx][ny], cnt+1, visited | {(nx, ny)})

def is_crd(xy):
    
    x, y = xy
    
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    else:
        return True

def t_shape(x, y):
    
    shapes = [
        [(x, y), (x+1, y), (x+2, y), (x+1, y+1)],
        [(x, y), (x+1, y), (x+2, y), (x+1, y-1)],
        [(x, y), (x, y+1), (x, y+2), (x+1, y+1)],
        [(x, y), (x, y+1), (x, y+2), (x-1, y+1)],
        [(x, y), (x-1, y), (x-2, y), (x-1, y+1)],
        [(x, y), (x-1, y), (x-2, y), (x-1, y-1)],
        [(x, y), (x, y-1), (x, y-2), (x+1, y-1)],
        [(x, y), (x, y-1), (x, y-2), (x-1, y-1)],
    ]
    
    crds = []
    for s in shapes:
        check = all(map(is_crd, s))
        if check:
            crds.append(s)
            
    return crds


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

ans = 0
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for x in range(n):
    for y in range(m):
        dfs(x, y, maps[x][y], 0, {(x, y)})
        
        for t in t_shape(x, y):
            check = sum(map(lambda x:maps[x[0]][x[1]], t))
            ans = max(ans, check)
        
print(ans)
