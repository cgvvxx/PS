# Baekjoon 15900 - 나무 탈출
# Silver 1
# DFS/BFS


def dfs():
    
    count = 0
    stack = [(1, 0)]
    visited[1] = True
    
    while stack:
        
        v, d = stack.pop()        
        
        for i in graphs[v]:
            if not visited[i]:
                stack.append((i, d+1))
                visited[i] = True
                if len(graphs[i]) == 1:
                    count += d + 1
                
    return count


n = int(input())
nodes = [0] * (n+1)
visited = [False] * (n+1)
graphs = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

count = dfs()
print('No') if count % 2 == 0 else print('Yes')


# 루트 노드에서 모든 리프 노드까지의 거리의 합이 짝수인 경우 No, 홀수인 경우 Yes
# dfs를 이용해서 모든 리프 노드까지의 거리를 구함
# 이 때 stack에 단순히 노드 값 뿐만 아니라 노드의 깊이 까지 추가하여 리프 노드까지의 거리를 계산