# Baekjoon 18513 - 샘터
# Gold 5
# BFS/DFS


from collections import deque


def bfs():
    
    queue = deque()
    for p in ponds:
        queue.append((p, 1))
        visited.add(p)
    ans = 0
    cnt = 0
    
    while queue:
        
        x, d = queue.popleft()
        
        for i in range(2):
            
            nx = x + dx[i]
            
            if nx in visited:
                continue
                
            visited.add(nx)
            queue.append((nx, d+1))
            ans += d
            cnt += 1
            if cnt == k:
                return ans


n, k = map(int, input().split())
ponds = list(map(int, input().split()))

dx = [-1, 1]
visited = set()

print(bfs())


# 수직선 상에서 간단한 bfs