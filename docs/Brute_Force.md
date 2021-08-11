# Brute Force

## 완전탐색

> 주어진 문제의 가능한 모든 경우를 확인하여 문제의 조건에 맞는 해를 구하는 방법

<br>

### 1. 완전 탐색 기법

- 대략적으로 약 총 연산수가 1억 회 이하인 경우 완전탐색 고려 가능
- 일반적으로 다음과 같은 방법을 활용함
  - 단순 반복문과 조건문을 활용해 모든 테스트 케이스를 확인하는 방법
  - 조합(Combination), 순열(Permutation) 등을 이용하여 모든 경우의 수를 나열하는 방법
    - 순열의 시간복잡도는 O(n!)
  - 재귀 함수
  - 비트마스크
    - 비트 연산을 통해 삽입, 삭제, 조회가 간단해짐
    - 코드가 간결해지고 빠른 연산 가능
    - 더 적은 메모리 사용량 => DP
    - 비트 연산 : & (and), | (or), ^ (xor), <<, >> (shift), ~ (not)
  - BFS 또는 DFS
  - 백트래킹



### 2. 백트래킹(Backtracking)

- 재귀적으로 문제를 풀어나가면서 현재 상태가 문제의 조건에 맞지 않으면 현재 상태를 제외하고 다음 단계를 탐색하는 방식
- 즉, 현재의 노드가 유망하지 않다고 판단되면 그 노드의 이전으로 돌아가 다음 자식 노드로 가는 가지치기(pruning)를 활용
- DFS의 재귀 함수 활용

<br>

### Ex1. 백트래킹

```python
# N과 M ; 1 부터 N까지의 자연수 중에서 중복 없이 M개를 고르는 수열

n, m = map(int, input().split())

l = []
def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, n+1):
        if i in l:
            continue
        l.append(i)
        dfs()
        l.pop()

dfs()
```

```python
# N-Queen ; NxN 크기의 체스판 위에서 N개의 퀸이 서로 공격할 수 없게 놓는 방법의 수

n = int(input())
board = []
ct = []

def is_diagonal(board, k):
    
    l = board + [k]
    if len(l) <= 1:
        return True
    idx_k = len(l)-1
    
    for i in range(len(l)-1):
        if abs(i - idx_k) == abs(l[i] - k):
             return False
            
    return True

def dfs_chess():
        
    if len(board) == n:
        ct.append(1)
        return
    
    for i in range(n):
        if i in board:
            continue
        
        if not is_diagonal(board, i):
            continue
            
        board.append(i)
        dfs_chess()
        board.pop()
            
dfs_chess()
print(sum(ct))
```

### Ex2. 비트연산자

```python
# 비트연산자를 이용한 부분집합 생성

arr = [1,2,3]
n = len(arr)

for i in range(1 << n):
    for j in range(n+1):
        if i & (1 << j):
            print(arr[j], end=' ')
    print('/ ', end='')
>> / 1 / 2 / 1 2 / 3 / 1 3 / 2 3 / 1 2 3 /   # 맨 앞은 공집합인 case
```



<br>

### 참고 문제

- Baekjoon #9663 - [N-Queen] : [problem](https://www.acmicpc.net/problem/9663), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%EC%99%84%EC%A0%84%ED%83%90%EC%83%89/074_P_N-Queen.py)
- Baekjoon #14888 - [연산자 끼워넣기] : [problem](https://www.acmicpc.net/problem/14888), [solution]()
- Baekjoon #2580 - [스도쿠] : [problem](https://www.acmicpc.net/problem/2580), [solution]()
