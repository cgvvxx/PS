# Disjoint Set

## 서로소 집합

> 공통 원소가 없는 집합

<br>

### 1. UnionFind

#### 1.1 Union

- x가 속한 집합과 y가 속한 집합을 합집합하는 연산
- 서로 연결된 두 노드 x, y의 루트 노드 x', y'을 찾고 x'을 y'의 부모 노드로 설정

#### 1.2 Find

- x가 속한 집합의 대푯값은 반환하는 연산, 일반적으로 트리를 이용해 구현하므로 루트 노드 번호를 반환
- 경로 압축을 통해 Find 함수 최적화
  - Find 함수를 재귀적으로 호출한 뒤 부모 테이블 값을 바로 갱신

### 2. Cycle 판별

- 서로소 집합을 이용하면 무방향 그래프 내에서의 사이클 판별 가능 (방향 그래프인 경우 DFS)
- 사이클 판별 알고리즘
  - 각 간선을 하나씩 확인하면서 두 노드의 루트 노드를 확인
    - 루트 노드가 다르면 두 노드에 대해 Union 연산 수행
    - 루트 노드가 같다면 사이클이 발생한 것
  - 그래프에 포함되어 있는 모든 간선에 대하여 1의 과정을 반복

<br>

### EX1. UnionFind

```python
# Union & Find 함수 

v = int(input())	# 간선의 개수
parent = list(range(v+1))	# 각 간선의 루트 노드

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
```

### EX2. Cycle

```python
# 무방향 그래프의 cycle 판별

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cycle = True
        break
    else:
        union(a, b)
```

<br>

### 참고 문제

- Baekjoon #1717 - [집합의 표현] : [problem](https://www.acmicpc.net/problem/1717), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%ED%8A%B8%EB%A6%AC/155_B_1717.py) 

