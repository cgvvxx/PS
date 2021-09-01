# Baekjoon 13549 - 숨바꼭질3
# Gold 5
# BFS/DFS


from collections import deque


def bfs(x):
    
    queue = deque()
    queue.append(x)
    visited[x] = 0
    
    while queue:
        
        x = queue.popleft()
        next_x = [2*x, x-1, x+1]
        
        if x == k:
            return visited[x]
        
        for idx, num in enumerate(next_x):
            
            if num > n_max or num < 0:
                continue
                
            if visited[num] == -1:
        
                if idx == 0:
                    queue.appendleft(num)
                    visited[num] = visited[x]
                else:
                    queue.append(num)
                    visited[num] = visited[x] + 1
                
        
n, k = map(int, input().split())
n_max = 10**5

check = [False] * (n_max + 1)
visited = [-1] * (n_max + 1)

if n == k:
    print(0)
else:
    print(bfs(n))
        
    
# 1697 숨바꼭질 문제의 업그레이드
# 내 위치의 배수가 되는 곳은 cost가 없으므로 먼저 처리해줘야함
# 따라서 내 위치의 배수인 경우 주어진 queue에서 왼쪽에서 삽입해서 먼저 처리