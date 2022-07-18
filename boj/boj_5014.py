# solved: [5014] 스타트링크
# https://www.acmicpc.net/problem/5014
# bfs
#
# Gold 5
# 
# 현재 위치에서 +u, -d 위치를 bfs를 통해서 방문하여 해당 층의 방문까지 필요한 버튼의 수를 visited에 기록
# s == g인 경우, 예외처리


from collections import deque


def bfs():
    
    queue = deque()
    queue.append(s)
    
    while queue:
        
        cur = queue.popleft()
        
        for n in [u, -d]:
            
            nxt = cur + n
            
            if nxt <= 0 or nxt > f:
                continue
            
            if visited[nxt] != -1:
                continue
                
            if nxt == g:
                return visited[cur] + 1
            
            visited[nxt] = visited[cur] + 1
            queue.append(nxt)
    
    return "use the stairs"


f, s, g, u, d = map(int, input().split())
visited = [-1] * (f+1)
visited[s] = 0
if s == g:
    print(0)
else:
    print(bfs())
