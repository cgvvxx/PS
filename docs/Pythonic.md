# Pythonic



## 1. 문자열

```python
import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)

>> abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
```



## 2. 리스트

```python
# 2차원 배열
arr = [[0]*2 for i in range(3)]
print(arr)
>> [[0, 0], [0, 0], [0, 0]

# 2차원 배열 > 1차원 배열
my_list = [[1, 4], [5, 6]]
print(sum(my_list, []))
>> [1, 4, 5, 6]
```

```python
# 1. *(asterisk) ; unpacking
_list = [1, 2, 3, 4, 5]
print(*_list)
>> 1 2 3 4 5

# 2. *(asterisk) ; 가변인자
N, *arr = map(int, input().split())
```



## 3. 기본 라이브러리

- Python standard library : [collections](https://docs.python.org/ko/3/library/collections.html), [itertools](https://docs.python.org/ko/3/library/itertools.html), [math](https://docs.python.org/ko/3/library/math.html)

### 1. collections

#### 1. Counter

```python
from collections import Counter

_string = 'onetwothree'
Counter(_string)
>> Counter({'o': 2, 'n': 1, 'e': 3, 't': 2, 'w': 1, 'h': 1, 'r': 1})

_list = [1, 2, 3, 1, 1, 4, 2, 5, 4, 4]
Counter(_list)
>> Counter({1: 3, 2: 2, 3: 1, 4: 3, 5: 1})
```

- Counter 객체끼리 +, -, &, | 연산 가능
- most_common(n), update(), elements() etc.

#### 2. defaultdict

```python
_string = 'hello World'
_string_dict = defaultdict(int)
for char in _string:
    _string_dict[char] += 1
print(_string_dict)
>> defaultdict(int, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}
```

- Dictionary에 값이 있으면 주어진 키로 접근, 값이 없으면 넘겨준 값을 default로 설정

#### 3. deque

- Stack&Queue 자료구조 참고

### 2. itertools

```python
# permutations, combinations, product, combinations_with_replacement
from itertools import ...
_list = [1, 2, 3]

print(*permutations(_list, 2))
print(*combinations(_list, 2))
print(*product(_list, repeat=2)
print(*combinations_with_replacement(_list, 2))

>> (1, 2) (1, 3) (2, 3)
(1, 2) (1, 3) (2, 1) (2, 3) (3, 1) (3, 2)
(1, 1) (1, 2) (1, 3) (2, 2) (2, 3) (3, 3)
(1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)
```

### 3. math

```python
import math
math.gcd(n, m) # n과 m의 최대공약수
math.lcm(n, m) # n과 m의 최소공배수
math.floor(r) # [r]
```

### 4. heapq

- Stack&Queue 자료구조 참고

### 5. bisect

- Binary Search 자료구조 참고



## 4. 기타

- 아스키코드 ; ord('char'), chr(num)
- 10진수 > 2, 8, 16진수 ; bin(n), oct(n), hex(n)
- n진수 > 10진수 ; int('n', base)

- 주어진 원소 값이 들어있는지 아닌지 찾을 때는 list보다는 set

```python
check_list = [4, 8, 9, 14]
for num in range(100):
    if num in check_list:
    	...

# Set은 hash table구조로 in 연산의 시간복잡도 O(1) (but, List의 경우 O(n)) 
check_list = [4, 8, 9, 14]
check_list_set = set(check_list) 
for num in range(100):
    if num in check_list_set:
        ...
```

