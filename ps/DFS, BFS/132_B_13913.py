# Baekjoon 13913 - 숨바꼭질4
# Gold 4
# BFS/DFS


from collections import deque


def bfs(x):
    
    queue = deque()
    queue.append(x)
    visited[x] = [0, 1]
    
    while queue:
        
        x = queue.popleft()
        next_x = [x-1, x+1, x*2]
        
        if x == k:
            return
        
        for i in next_x:
            
            if i > n_max or i < 0:
                continue
                
            if visited[i][0] == -1:
                queue.append(i)
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = x
                if i == k:
                    return
                
                
n, k = map(int, input().split())
n_max = 10**5
visited = [[-1, 0] for _ in range(n_max + 1)]

if n == k:
    print(0)
    print(n)
else:
    bfs(n)

    ans = [k]
    i = k
    while True:
        ans.append(visited[i][1])
        i = visited[i][1]
        if i == n:
            break

    print(visited[k][0])
    print(*ans[::-1])
    

# 1697 숨바꼭질 문제의 업그레이드
# 차라리 12851 숨바꼭질2 문제랑 더 비슷한듯 하긴함
# visited의 두번째 원소를 이전 노드의 값으로 정해서 현재 루트까지의 최단거리 경로를 구할 수 있음