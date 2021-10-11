# Programmers - 배달
# Level 2


def solution(N, road, K):
    
    INF = int(1e9)
    graph = [[INF] * (N+1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        graph[i][i] = 0
    
    for a, b, c in road:
        if graph[a][b] > c:
            graph[a][b] = c
            graph[b][a] = c
        
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
    
    return sum(map(lambda x:x<=K, graph[1]))


# 한 노드에서 모든 노드까지의 거리가 K보다 작은 지점의 개수를 구하는 문제 => 플로이드 워셜
# 두 마을을 연결하는 도로가 여러 개 있을 수 있으므로 그 중 거리가 가장 작은 도로만 graph에 입력하는 부분만 조금 특이한 듯
# 그 외에는 기본적인 플로이드 워셜 알고리즘 적용