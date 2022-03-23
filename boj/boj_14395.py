# solved: [14395] 4연산
# https://www.acmicpc.net/problem/14395
# bfs
#
# Gold 5
# * > + > - > / 순으로 연산을 하면서 그 값과, 연산의 순서를 queue에 append 하면서 bfs 진행
# 최대 10**9이므로 최악의 경우 약 30번 (2**30 ~ 10**9)만 체크하면 되므로 시간초과 X

from collections import deque


def bfs(a):
    
    if a == t:
        return 0
    
    queue = deque()
    queue.append((a, ''))
    visited.add(a)
    
    while queue:
        
        x, cal = queue.popleft()
        
        for nx, ncal in ((x**2, '*'), (2*x, '+'), (0, '-'), (1, '/')):
            
            if nx == t:
                return cal + ncal
            
            if nx > MAX or nx in visited:
                continue
                
            visited.add(nx)
            queue.append((nx, cal + ncal))
        
    return -1


s, t = map(int, input().split())
visited = set()
MAX = 10**9

print(bfs(s))
