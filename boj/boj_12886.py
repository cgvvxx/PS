# solved: [12886] 돌 그룹
# https://www.acmicpc.net/problem/12886
# bfs, graph-traversal
# 
# Gold 4
# 돌의 개수를 정렬해서 x, y, z라고 하면
# (x, y), (y, z), (x, z) 만큼의 돌 이동을 한 경우를 bfs를 통해 탐색
# 이 때 visited는 set에 (x, y, z) 원소를 넣어서 체크
# 실제로 z = s - a - b이므로 (a, b)만으로 bfs를 진행해도 문제 없을듯

from queue import deque


def bfs(x, y, z):
    
    queue = deque()
    queue.append((x, y, z))
    
    while queue:
        
        x, y, z = queue.popleft()
        nums = [x, y, z]
        
        if len(set(nums)) == 1:
            return 1
        
        if (x, y, z) in visited:
            continue
            
        visited.add((x, y, z))
        
        x1, y1 = change(x, y)
        x2, z1 = change(x, z)
        y2, z2 = change(y, z)
        
        c1 = tuple(sorted([x1, y1, z]))
        c2 = tuple(sorted([x2, y, z1]))
        c3 = tuple(sorted([x, y2, z2]))
    
        if c1 not in visited:
            queue.append(c1)
        if c2 not in visited:
            queue.append(c2)
        if c3 not in visited:
            queue.append(c3)
        
    return 0

def change(x, y):
    
    if x == y:
        return x, y
    
    y -= x
    x *= 2
    
    return x, y


a, b, c = map(int, input().split())

visited = set()
s = a + b + c
if s % 3 == 0:
    print(bfs(*sorted([a, b, c])))
else:
    print(0)
