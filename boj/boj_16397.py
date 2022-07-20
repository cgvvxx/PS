# solved: [16397] 탈출
# https://www.acmicpc.net/problem/16397
# bfs
#
# Gold 4
# bfs를 통해 다음 숫자 방문하여 체크
# 이 때, 해당 숫자만큼 건너간 거리를 체크(visited]해서 t이상이면 break


from collections import deque


def bfs():
    
    queue = deque()
    queue.append(n)
    
    while queue:
        
        cur = queue.popleft()
        chk = visited[cur]
        
        if chk >= t:
            continue
        
        nxts = []
        if cur < 99999:
            nxts.append(cur+1)
        if 0 < cur < 50000:
            nxts.append(get_nxt(cur))
        
        for nxt in nxts:
            
            if nxt == g:
                return  chk + 1
            
            if visited[nxt] != -1:
                continue
            
            visited[nxt] = chk + 1
            queue.append(nxt)
    
    return "ANG"

def get_nxt(n):
    
    nxt = 2*n
    nxt = list(str(nxt))
    nxt[0] = str(int(nxt[0]) - 1)
    
    return int(''.join(nxt))


n, t, g = map(int, input().split())
visited = [-1] * 100000
visited[n] = 0
if n == g:
    print(0)
else:
    print(bfs())
