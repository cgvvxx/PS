# Baekjoon 1956 - 운동
# Gold 4
# 최단 거리 - 플로이드 워셜


INF = int(1e10)

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

ans = min([graph[i][i] for i in range(v+1)])
if ans < INF:
    print(ans)
else:
    print(-1)
    
    
# 노드의 수 = 400으로 Floyd-Warshall 활용
# 최소 사이클의 값을 출력해야 하므로 대각선의 최솟값을 출력