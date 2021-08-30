# Baekjoon 1697 - 숨바꼭질
# Silver 1
# BFS/DFS


from collections import deque


def bfs(x):
    
    queue = deque()
    queue.append(x)
    
    while queue:
        
        x = queue.popleft()
        next_x = [x-1, x+1, x*2]
        
        for i in next_x:
            
            if i > 10**5 or i < 0:
                continue
                
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1
                if i == k:
                    return 

                
n, k = map(int, input().split())
visited = [0] * (10**5 + 1)

if n == k:
    print(0)
else:
    bfs(n)
    print(visited[k])
    
    
# BFS 이용하여 최대 거리만큼 visited 배열 만들고 visited에 최소 시간 입력하여 업데이트