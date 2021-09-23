# Tree

## 트리

> 부모가 없는 루트 노드에서 시작하여 각 노드를 부모-자식 관계로 정의하고, 부모에서 자식으로 간선이 이어져 있는 유향 그래프

<br>

### 1. Tree

#### 1.1 정의

- 트리(Tree) : 계층적인 자료를 표현하는 데 이용되는 비선형 자료 구조, 부모-자식 관계의 노드들로 이루어짐, 한 개 이상의 노드로 이루어진 유한 집합
- 노드(Node) : 트리의 구성요소 
- 간선(Edge) : 노드와 노드를 연결하는 선
- 루트 노드(Root Node) : 트리 구조에서 가장 상위 노드
- 리프 노드(Leaf Node) : 자식 노드가 없는 노드
- 레벨(Level) : 각 층별로 숫자를 매기며,  루트 노드의 레벨은 1
- 높이(Height) : 트리의 최고 레벨

![tree](./IMAGE/tree.png)

#### 1.2 종류

- 이진 트리(Binary Tree) : 모든 노드가 이진 트리인 두 개의 서브 트리를 가지는 트리. 즉 서브 트리의 모든 서브 트리도 이진 트리
  - n개의 노드를 가진 이진 트리는 n-1개의 간선을 가짐
  - 높이가 h인 이진 트리는 최소 h개의 노드를 가지며 최대 2^h-1개의 노드를 가짐
  - n개의 노드를 가지는 이진트리의 높이는 최대 n이거나 최소 log2(n+1)임
- 포화 이진 트리(Full Binary Tree) : 모든 레벨이 꽉 찬 이진 트리
- 완전 이진 트리(Complete Binary Tree) : 왼쪽 부터 빈틈없이 노드가 채워진 이진 트리
- 이진 탐색 트리(Binary Search Tree) : 이진 트리 기반의 탐색을 위한 자료 구조
  - 왼쪽 서브트리 키들은 루트 키보다 작고, 오른쪽 서브트리 키들은 루트 키보다 큼
  - 왼쪽과 오른쪽 서브트리도 모두 이진 탐색 트리
  - 이진 탐색 트리에서 탐색, 삽입, 삭제 연산의 시간복잡도는 O(h) (h : 트리의 높의), 즉 트리가 극단적으로 편향(skew)되어 있는 경우 최악의 시간복잡도는 O(n)

#### 1.3 트리의 순회

- 전위 순회(Preorder) : 루트 노드 > 왼쪽 노드 > 오른쪽 노드 순으로 방문
- 중위 순회(Inorder) : 왼쪽 노드 > 루트 노드 > 오른쪽 노드 순으로 방문
- 후위 순회(Postorder) : 왼쪽 노드 > 오른쪽 노드 > 루트 노드 순으로 방문
- 레벨 순회(Levelorder) : 각 노드를 레벨 순서대로 방문

### 2. MST(Minimum Spanning Tree)

#### 2.1 정의

- 신장트리(Spanning Tree) ; 그래프 내의 모든 정점을 포함하는 트리
  - spanning tree는 그래프의 최소 연결 부분 그래프
  - spanning tree는 그래프에 있는 V개의 정점을 V-1개의 간선으로 연결
  - 모든 정점들이 연결되어 있어야 하고 사이클을 포함해서는 안됨
- 최소신장트리(MST) ; 간선들의 가중치의 합이 최소인 신장 트리

#### 2.2 크루스칼(Kruskal) 알고리즘

- 간선의 가중치가 작은 순서대로 Greedy하게 선택함으로써 간선들의 가중치의 합이 최소인 MST를 구하는 알고리즘
- 동작 원리
  - 모든 간선들의 가중치를 오름차순으로 정렬
  - 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택하여 현재 MST의 집합에 추가
    - 이 때 사이클의 여부는 UnionFind DisjoinSet을 이용하여 O(1)에 확인
  - 위의 과정을 MST 집합이 V-1개의 간선을 가질 때까지 반복
- 시간복잡도 ; 간선의 정렬 O(ElogE) + 정렬된 간선의 순회 O(1) * E = O(ElogV)

#### 2.3 프림(Prim) 알고리즘

- 시작 정점을 기준으로 가장 작은 간선과 연결된 정점을 선택하며 신장 트리를 확장 시키는 알고리즘
- 동작원리
  - 임의의 정점을 선택하여 MST 집합(Priority Queue)에 추가
  - MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장
  - 위의 과정을 MST 집합이 V개의 정점을 가질 때까지 반복
- 시간복잡도 ; 각 간선이 한번씩 Priority Queue에 삽입되고 제거 O(ElogE) = O(ElogV)

### 3. Tree DP

- TBD

<br>

### EX1. Traversal

```python
# Tree의 순회 ; 전위순회, 중위순회, 후위순회

def preorder(node):
    
    if node != 0:
        yield node
        preorder(trees[node][0])
        preorder(trees[node][1])


def inorder(node):
    
    if node != 0:
        inorder(trees[node][0])
        yield node
        inorder(trees[node][1])
    

def postorder(node):
    
    if node != 0:
        postorder(trees[node][0])
        postorder(trees[node][1])
        yield node
```

### Ex2. Kruskal

```python
# kruskal algortithm w/ UnionFind

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = list(range(v+1))

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)
```

### Ex3. Prim

```python
# prim algorhitm w/ heap

from collections import defaultdict
import heapq


v, e = map(int, input().split())
graph = defaultdict(list)
visited = [0] * (v+1)
mst = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, a, b))
    graph[b].append((cost, b, a))
    
start = 1
visited[start] = 1
candidate = graph[start]
heapq.heapify(candidate)

while candidate:
    cost, a, b = heapq.heappop(candidate)
    
    if visited[b] == 0:
        visited[b] = 1
        mst.append((a, b))
        result += cost
        
        for edge in graph[b]:
            if visited[edge[2]] == 0:
                heapq.heappush(candidate, edge)

print(result)
```

<br>

### 참고 문제

- Baekjoon #1991 - [트리 순회] : [problem](https://www.acmicpc.net/problem/1991), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%ED%8A%B8%EB%A6%AC/122_B_1991.py)

- Baekjoon #1197 - [최소 스패닝 트리] : [problem](https://www.acmicpc.net/problem/1197), [solution]()

  

