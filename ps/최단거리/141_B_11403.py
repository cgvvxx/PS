# Baekjoon 11403 - 경로 찾기
# Silver 1
# 최단 거리 - 플로이드 워셜


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = any([graph[j][k], graph[j][i]&graph[i][k]])
            
for i in graph:
    print(*map(int, i))
    
    
# n <= 100이므로 Floyd-Warshall 활용
# 이 때 경로가 존재하기만 하면 되므로 any 함수와 & 활용해서 graph를 업데이트