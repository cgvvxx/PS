# Baekjoon 14226 - 이모티콘
# Gold 5
# BFS/DFS


from collections import deque

def bfs(s):
    
    queue = deque()
    queue.append((1, 0, 0))
    visited = set()
    
    while queue:
        
        imo, clip, cnt = queue.popleft()
        
        if imo == s:
            return cnt
        
        if (imo, clip) in visited:
            continue
        
        visited.add((imo, clip))
        
        queue.append((imo, imo, cnt+1))
        queue.append((imo+clip, clip, cnt+1))
        queue.append((max(imo-1, 0), clip, cnt+1))
        
print(bfs(int(input())))
    
    
# 이모티콘을 만들 수 있는 동작 3개에 대하여 queue에 삽입하여 bfs로 진행
# 목표 수인 s에 도달하면 return 하여 몇 번의 bfs가 진행되었는지를 print
# dp로도 풀 수 있을것 같긴한데..

