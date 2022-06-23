# solved: [17142] 연구소 3
# https://www.acmicpc.net/problem/17142
# bfs, bruteforcing, graph-traversal
# 
# Gold 4
# m개의 바이러스의 모든 조합을 bfs를 통해 체크
# bfs로 전진할 때(빈 공간 & 바이러스 공간), 빈 공간인 경우 전체 cnt -= 1하면서 빈 공간이 없어졌을 때 bfs 종료
# t는 해당 칸에 전진할 때의 시간

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(vi, cnt):

    queue = deque(vi)
    v = [[False if graphs[i][j] == 0 or graphs[i][j] == 2 else True for j in range(n)] for i in range(n)]

    while queue:
        
        x, y, t = queue.popleft()
        
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if v[nx][ny]:
                continue
            
            v[nx][ny] = True
            queue.append((nx, ny, t+1))
            if graphs[nx][ny] == 0:
                cnt -= 1

            if not cnt:
                return t

    return 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(n)]

virus = set()
cnt = 0
for i in range(n):
    for j in range(n):
        if graphs[i][j] == 0:
            cnt += 1
        elif graphs[i][j] == 2:
            virus.add((i, j, 1))

if cnt == 0:
    print(0)
else:
    ans = []
    for comb in combinations(virus, m):
        chk = bfs(comb, cnt)
        if chk:
            ans.append(chk)

    if ans:
        print(min(ans))
    else:
        print(-1)
