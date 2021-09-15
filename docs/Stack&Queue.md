# Stack&Queue

## 자료구조(Data Structure)

> 컴퓨터에서 다루는 데이터를 구조적으로 표현하는 방식, 

<br>

### 1. 스택(Stack)

- 모든 원소의 삽입과 삭제가 리스트의 한쪽 끝(top)에서만 수행되는 제한 조건을 가진 선형 자료 구조
- 후입선출(LIFO ; Last-in First-out) 구조
- 기본 연산 : push, pop / top, isempty, isfull ~ O(1)
- stack이 가득 찬 상태에서 새로운 원소를 push할 경우 stack overflow, 반대로 stack이 빈 상태에서 pop 연산 수행시 stack underflow 발생

### 2. 큐(Queue)

- 한쪽(rear)으로 데이터가 삽입되고 반대(front) 방향으로 데이터가 삭제되는 선형 자료 구조

- 선입선출(FIFO ; First-in First-out) 구조

- 기본 연산 : enqueue, dequeue ~ O(1)

  #### - 원형 큐(Circular Queue)

  - <u>TBD</u>

  #### - 우선순위 큐(Priority Queue)

  - 들어간 순서와 상관없이 우선순위가 높은 데이터를 먼저 삭제하는 자료 구조
  - 힙(Heap) 이라는 자료구조로 구현
    - 완전 이진 트리
    - 모든 노드에 저장된 값(우선순위)는 자식 노드에 저장된 값(우선순위) 보다 크거나 같음(또는 작거나 같음)
  - Max heap은 root 노드가 가장 큰 값, Min heap은 root 노드가 가장 작은 값
  - 원소를 삽입 또는 삭제 할 때 마다 정렬이 필요한 경우
  - Python standard library : [heapq](https://docs.python.org/ko/3/library/heapq.html)

### 3. 덱(Deque)

- 삽입과 삭제가 리스트의 양쪽 끝에서 모두 발생할 수 있는 선형 자료 구조
- 스택과 큐의 기능을 모두 지원

- 파이썬에서는 collections 모듈의 deque 클래스로 활용

<br>

### Ex1. Queue

```python
from collections import deque

queue = deque()
queue.append(3)
queue.append(7)
queue.append(9)
print(queue.popleft())
print(queue)

>> 3
>> deque([7, 9])
```

### Ex2. Heap

```python
import heapq
# python에서의 heapq 모듈은 min heap

heap = []
heapq.heappush(heap, 10)
# max heap 구현하려면 heapq.heappush(heap, -10)
heapq.heappush(heap, 7)
heapq.heappush(heap, 23)
heapq.heappush(heap, 1)
print(heap)
print(heapq.heappop(heap))
print(heap)

>> [1, 7, 23, 10]
>> 1
>> [7, 10, 23]
```

<br>

### 참고 문제

- Baekjoon #1655 - [가운데를 말해요] : [problem](https://www.acmicpc.net/problem/1655), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/%EC%8A%A4%ED%83%9D%2C%20%ED%81%90/058_B_1655.py)
- Baekjoon #13334 - [철로] : [problem](https://www.acmicpc.net/problem/13334), [solution](https://github.com/cgvvxx/algorithm_study/blob/master/ps/스택%2C 큐/136_B_13334.py)

