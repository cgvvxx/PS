# solved: [1525] 퍼즐
# https://www.acmicpc.net/problem/1525
# bfs
#
# Gold 2
# bfs를 통해서 현재 퍼즐에서 갈 수 있는 퍼즐로 이동하여 이동한 거리를 체크
# visited는 set을 이용하여 해당 퍼즐의 숫자의 나열(ex. "123456780")을 add하여 체크
# 현재 퍼즐에서 갈 수 있는 위치는 0의 위치가 -1, 1, -3, 3이 되는 경우
# 이 때 0의 위치가 -1, 1이 되는 경우는 같은 줄에만 있어야 함


from collections import deque


def bfs():
    
    queue = deque()
    visited = set()
    
    queue.append(s)
    visited.add(s)
    chk = 0
    
    while queue:
        
        for _ in range(len(queue)):
            
            cur = queue.popleft()
            
            for nxt in get_nxt(cur):
                
                if nxt == "123456780":
                    return chk+1
                
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
                    
        chk += 1
    
    return -1

def get_nxt(s):
    
    i = s.find('0')
    nxt = []
    
    for d in [-1, 1, -3, 3]:
        
        j = i + d
        
        if j < 0 or j >= 9:
            continue
            
        if d == -1 or d == 1:
            if i // 3 != j // 3:
                continue
                
        nxt.append(change(s, i, j))
            
    return nxt
        
def change(s, i, j):
    
    l = list(s)
    l[i], l[j] = l[j], l[i]
    
    return ''.join(l)


s = ''
for _ in range(3):
    s += ''.join(map(str, input().split()))

if s == "123456780":
    print(0)
else:
    print(bfs())
