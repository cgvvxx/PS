# solved: [4179] 불!
# https://www.acmicpc.net/problem/4179
# bfs, graph-traversal
#
# Gold 4
# 지훈이의 위치를 저장하는 큐(j_queue)와 불의 위치를 저장하는 큐(f_queue)를 동시에 bfs 진행
# 불 진행 > 지훈이 진행 순서로 bfs
# 시간초과 때문에 import sys; input = sys.stdin.readline 추가
# 주의해야할 반례 - J가 외곽에 있는 경우
# ex)
# 2 2
# JF
# FF
# >> 1

from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    
    def is_okay(cx, cy):
        
        if cx < 0 or cy < 0 or cx >= r or cy >= c or graph[cx][cy] == -1:
            return False
        else:
            return True
    
    j_queue = deque()
    j_queue.append(j_start[0])
    
    f_queue = deque()
    f_queue.extend(f_start)

    d = -1

    print(graph, 'first')
    
    while j_queue:

        for _ in range(len(f_queue)):

            fx, fy = f_queue.popleft()
        
            for i in range(4):
                
                nfx = fx + dx[i]
                nfy = fy + dy[i]
                
                if not is_okay(nfx, nfy):
                    continue
                    
                if not visited[nfx][nfy]:
                    graph[nfx][nfy] = -1
                    f_queue.append((nfx, nfy))
                    visited[nfx][nfy] = True

        d += 1
        
        for _ in range(len(j_queue)):

            jx, jy = j_queue.popleft()

            if jx == 0 or jy == 0 or jx == r-1 or jy == c-1:
                return 1
        
            for i in range(4):
                    
                njx = jx + dx[i]
                njy = jy + dy[i]
                
                if not is_okay(njx, njy):
                    continue
                    
                if graph[njx][njy] == 0:
                    graph[njx][njy] = d + 1
                    j_queue.append((njx, njy))

                if njx == 0 or njy == 0 or njx == r-1 or njy == c-1:
                    return graph[njx][njy] + 1

        print(graph)
        
    return False


r, c = map(int, input().split())
graph_input = [list(input()) for _ in range(r)]

graph = [[0] * c for _ in range(r)]
visited = [[False] * c for _ in range(r)]
j_start = []
f_start = []
for i in range(r):
    for j in range(c):
        if graph_input[i][j] == '#':
            graph[i][j] = -1
        
        if graph_input[i][j] == 'J':
            j_start.append((i, j))
            graph[i][j] = 1
            
        if graph_input[i][j] == 'F':
            f_start.append((i, j))
            graph[i][j] = -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = bfs()
if ans:
    print(ans)
else:
    print('IMPOSSIBLE')
