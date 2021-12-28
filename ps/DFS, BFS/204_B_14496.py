# Baekjoon 14496 - 그대, 그머가 되어
# Silver 1
# DFS/BFS


from collections import defaultdict, deque


def bfs(x):
    
    queue = deque()
    queue.append(x)
    visited[x] = 0
    
    while queue:
        
        nx = queue.popleft()

        if nx == b:
            return visited[nx]
        
        for ny in graphs[nx]:
            
            if visited[ny] == -1:
                visited[ny] = visited[x] + 1
                queue.append(ny)
            
    return -1


a, b = map(int, input().split())
n, m = map(int, input().split())

visited = [-1] * (n+1)
graphs = defaultdict(set)
for _ in range(m):
    _from, _to = map(int, input().split())
    graphs[_from].add(_to)
    graphs[_to].add(_from)

if a == b:
    print(0)
else:
    print(bfs(a))
    

# 가중치가 1인 양방향 그래프의 최단거리 찾기 => bfs
# 1. 양방향 그래프라는 정보가 문제에 주어져 있지 않음
# 2. 출발 노드와 도착 노드가 같은 경우 체크해야함
# 1, 2만 주의하면 단순한 bfs