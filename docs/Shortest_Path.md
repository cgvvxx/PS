

# Shortest Path

## 최단 경로

> 가중치가 주어진 그래프에 대해 주어진 두 정점을 연결하는 경로 중 최단 경로(가중치의 합이 최소)를 찾는 문제

<br>

### 1. 최단 경로 문제

- 최단 경로 문제 종류 
  - 단일 쌍 최단 경로 : 주어진 두 개의 노드 u와 v에 대해 u에서 v까지의 최단 경로를 찾는 문제
  - 전체 쌍 최단 경로 : 그래프 내 모든 노드 쌍들 사이의 최단 경로를 찾는 문제
  - 단일 출발 최단 경로(또는 단일 도착 최단 경로) : 단일 노드 u에서 출발하여 그래프 내의 다른 노드에 도착하는 경로 중 최단 경로를 찾는 문제 (또는 그래프 내의 임의의 노드에서 단일 노드 v에 도착하는 최단 경로를 찾는 문제)
- DFS : 가중치가 없거나 모든 가중치가 동일한 그래프에서 활용
- Dijkstra Algorithm : 음의 가중치가 없는 그래프에서 단일 쌍, 단일 출발(도착) 최단 경로 문제에서 활용
- Bellman-Ford-Moore Algorithm : 음의 가중치를 포함하는 그래프에서 단일 쌍, 단일 출발(도착) 최단 경로 문제에서 활용
- Floyd-Warshall Algorithm : 전체 쌍 최단 경로 문제에서 활용

### 2. 다익스트라(Dijkstra) 알고리즘

- V개의 정점과 음이 아닌 가중치를 가진 E개의 간선으로 이루어진 그래프에서 특정 출발점(S)에서 다른 모든 정점까지의 최단 경로를 구하는 알고리즘

- 각 정점을 최대 한 번씩 방문하여 최단거리를 정하므로 시간복잡도는 O(V^2)
- 힙을 활용하여 시간복잡도를 O(VlogV)로 줄일 수 있음
- "최단 경로의 부분 경로 또한 최단 경로이다"라는 정리를 활용

### 3. 플로이드-워셜(Floyd-Warshall) 알고리즘

- 모든 정점 사이의 최단 경로를 구하는 알고리즘 (음의 가중치를 가진 그래프도 가능)
- 모든 정점에서 모든 정점으로 갈 때 모든 가능한 경유지를 살펴보아야 하므로 시간복잡도는 O(V^3)

### 4. 0-1 BFS

- 가중치가 0 또는 1(혹은 x)로 주어진 그래프에서 최단 경로를 구하는 알고리즘
- 일반적인 BFS 탐색과 동일하지만, 가중치가 0인 정점이 존재하므로 정점의 방문횟수가 많더라도 가중치가 더 낮은 경우가 존재
  - 가중치가 0인 경우 deque의 앞으로, 가중치가 1인 경우 deque에 뒤로 삽입
- 다익스트라 알고리즘보다도 시간복잡도를 O(V+E)로 줄일 수 있음

<br>

### Ex1. Dijkstra

```python
# 기본적인 Dijkstar algortithm 

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
        
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for j in graph[start]:
        distance[j[0]] = j[1]
        
    for k in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        for l in graph[now]:
            cost = distance[now] + l[1]
            if cost < distance[l[0]]:
                distance[l[0]] = cost    


INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

```python
# 우선순위 큐(힙) 구조를 이용한 Dijkstra algorithm

import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

### Ex2. Floyd-Warshall

```python
# 기본적인 Floyd-Warshall algortithm 

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 2차원 배열 초기화 
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 2차원 배열 초기화 - 간선에 대한 정보 업데이트
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# Floyd-Warshall Algorithm
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

# 2차원 배열 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
```

<br>

### 참고 문제

- Baekjoon #1753 - [최단경로] : [problem](https://www.acmicpc.net/problem/1753), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC/146_B_1753.py)

- Baekjoon #11404 - [플로이드] : [problem](https://www.acmicpc.net/problem/11404), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%EC%B5%9C%EB%8B%A8%EA%B1%B0%EB%A6%AC/147_B_11404.py)


- Baekjoon #1261 - [알고스팟] : [problem](https://www.acmicpc.net/problem/1261), [solution]()
