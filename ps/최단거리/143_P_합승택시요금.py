# Programmers - 합승 택시 요금
# Level 3
# 최단 거리 - 플로이드 워셜


def solution(n, s, a, b, fares):
    
    INF = 10**9
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
        
    for i, j, fare in fares:
        graph[i][j] = fare
        graph[j][i] = fare

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

    

    answer = graph[s][a]+graph[s][b]

    for l in range(1, n+1):
        answer = min(answer, graph[s][l]+graph[l][a]+graph[l][b])
        
    return answer


# 노드의 개수 <= 200이라 Floyd-Warshall 활용
# (i, i)의 값은 0으로 초기화
# s부터 중간지점, 중간지점부터 a, b로의 거리의 최솟값을 구함
# 이 때 최댓값 INF를 충분히 크게 해야 코드가 잘 돌아감 > 10**6 정도만 해도 틀리는 경우가 존재..