# Baekjoon 16928 - 뱀과 사다리 게임
# Silver 1
# BFS/DFS


from collections import deque

def bfs():
    
    queue = deque()
    queue.append((1, 0))
    visited[1] = 0
    
    while queue:
        
        x, cnt = queue.popleft()
        
        for i in range(1, 7):
            
            nx = x + i
            
            if visited[nx] != 999:
                continue
            
            if nx == 100:
                return cnt+1
            
            if nx in ladders:
                nx = ladders[nx]
            
            if nx <= 0 or nx > 100:
                continue
            
            m_cnt = min(visited[nx], cnt+1)
            visited[nx] = m_cnt
            queue.append((nx, m_cnt))


visited = [999] * 101
n, m = map(int, input().split())
ladders = dict()

for _ in range(n+m):
    a, b = map(int, input().split())
    ladders[a] = b

print(bfs())


# visited ; i번째까지 가는데에 걸리는 최소 경우의 수
# 1부터 시작하여 +1 ~ +6 까지 visited를 업데이트 하면서 bfs 시작
# ladders에 숫자가 있는 경우 그 숫자만큼 이동