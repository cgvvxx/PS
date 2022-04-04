# solved: [20058] 마법사 상어와 파이어스톰
# https://www.acmicpc.net/problem/20058
# implementation
# 
# Gold 4
# 문제 조건에 맞게 차분히 구현..
# rotate_xy ; 좌상단 모서리 좌표, 우하단 모서리 좌표의 직사각형을 90도 회전하는 함수
# spell ; l을 매개변수로 받아 주어진 회전을 시행 후, 얼음을 제거
# count_maximum ; bfs를 통해 가장 큰 얼음조각 찾기

from queue import deque


def rotate_90(arrs):
    
    return [list(r[::-1]) for r in zip(*arrs)]

def rotate_xy(lx, ly, rx, ry):
    
    arrs = [graphs[r][ly:ry+1] for r in range(lx, rx+1)]
    rot_arrs = rotate_90(arrs)
    
    for i in range(rx-lx+1):
        for j in range(ry-ly+1):
            graphs[i+lx][j+ly] = rot_arrs[i][j]

def spell(l):
    
    def decrease():
        
        crds = set()
        for i in range(nn):
            for j in range(nn):
                if graphs[i][j] and not count(i, j):
                    crds.add((i, j))
                    
        for i, j in crds:
            graphs[i][j] -= 1
    
    def count(x, y):
        
        cnt = 0
        
        for dx, dy in dirs:
            
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx >= nn or ny >= nn:
                continue
            
            if graphs[nx][ny]:
                cnt += 1
                
        return True if cnt >= 3 else False
    
    
    ll = 2**l
    for i in range(0, nn, ll):
        for j in range(0, nn, ll):
            rotate_xy(i, j, i+ll-1, j+ll-1)
    
    decrease()

def count_maximum():
    
    def bfs(x, y):

        queue = deque()
        queue.append((x, y))
        visited[x][y] = True
        cnt = 1

        while queue:

            x, y = queue.popleft()

            for dx, dy in dirs:

                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx >= nn or ny >= nn:
                    continue
                    
                if not visited[nx][ny] and graphs[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
        return cnt
                    
    
    visited = [[False] * (nn) for _ in range(nn)]
    ans = 0
    
    for i in range(nn):
        for j in range(nn):
            if not visited[i][j] and graphs[i][j]:
                ans = max(ans, bfs(i, j))
                
                
    return ans


n, q = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(2**n)]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
nn = 2**n

for l in map(int, input().split()):
    spell(l)

print(sum(sum(graphs, [])))
print(count_maximum())
