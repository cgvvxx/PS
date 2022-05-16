# solved: [2644] 촌수계산
# https://www.acmicpc.net/problem/2644
# dfs, graph-traversal
#
# Silver 2
# 시작노드 부터 dfs를 통해 타겟노드가 나올 때까지 dfs
# 타겟노드가 존재하면 flag = True, 해당 노드 print후 return
# 타겟노드가 존재하지 않으면 -1 print

def dfs(n, d):

    global flag
    
    for m in graph[n]:
        if m == b:
            flag = True
            print(d)
            return

        if not visited[m]:
            visited[m] = True
            dfs(m, d+1)


n = int(input())
a, b = map(int, input().split())
graph =[[] for _ in range(n+1)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  
            
visited = [False] * (n+1)
flag = False
dfs(a, 1)
if not flag:
    print(-1)
