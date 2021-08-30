# Baekjoon 12851 - 숨바꼭질2
# Gold 5
# BFS/DFS


from collections import deque


def bfs(x):
    
    queue = deque()
    queue.append(x)
    visited[x] = [0, 1]
    cnt = 0
    is_break = False
    exit = -5
    
    while queue:
        
        x = queue.popleft()
        next_x = [x-1, x+1, x*2]
        
        if x == k:
            return cnt
        
        for i in next_x:
            
            if i > n_max or i < 0:
                continue
                
            if i == k:
                if not is_break:
                    exit = visited[x][0] + 1
                    is_break = True
                cnt += 1
                
            if visited[i][0] == -1:
                queue.append(i)
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = visited[x][1]
            elif visited[i][0] == visited[x][0] + 1:
                visited[i][1] += visited[x][1]
                
                
n, k = map(int, input().split())
n_max = 10**5
visited = [[-1, 0] for _ in range(n_max + 1)]

if n == k:
    print(0)
    print(1)
else:
    bfs(n)
    for idx in range(2):
        print(visited[k][idx])
        
        
# 1697 숨바꼭질 문제의 업그레이드
# 단순 방문 뿐만 아니라 그 방문지점에의 가지수까지 체크해야 하므로 visited를 두 개의 값을 갖는 리스트로 만듬
# visited의 첫번째 원소는 최단시간, 두번째 원소는 가짓 수 업데이트
# i == k인 경우가 나오면, 이 때의 최단시간이 k와 같은 것까지만 queue에서 pop하고 끝내도록 하기위해서
# exit과 is_break라는 변수 도입 >> 이 부분이 조금 오래걸림