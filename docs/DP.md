# DP

## Dynamic Programming(DP; 동적 프로그래밍)

> 메모리를 적절히 사용하여 수행 시간 효율성을 향상시키는 방법



- 이미 계산된 결과를 메모리에 저장(Memoization)하여 반복하여 계산하지 않도록 하여 시간 효율성 향상
- 다음의 조건을 만족하는 경우 DP 활용
  1. 최적 부분 구조 : 큰 문제를 작은 문제로 나누어 푸는 구조
  2. 중복 구조 : 동일한 작은 문제를 반복적으로 푸는 구조
- 1. Top-Down (하향식) : 재귀적
  2. Bottom-Up (상향식) : DP Table 작성, 반복문
- DP vs. 분할 정복
  - 두 알고리즘 모두 주어진 문제가 최적 부분 구조를 가질 때 활용
  - 주어진 문제의 부분 문제가 중복되는 경우 => DP
  - 동일한 부분 문제가 반복적으로 계산되지 않는 경우 => 분할 정복



### Ex. 피보나치 수열

```python
# 일반적인 재귀함수 형태의 알고리즘
# 시간복잡도 ~ O(2^n)
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
```

```python
# DP ; Top-down 방식
# 시간복잡도 ~ O(n)
D = [0] * 100 ; 

def f(n):
    if n==1 or n==2:
        return 1
    if D[n] > 0:
        return D[n]
    D[n] = f(n-1) + f(n-2)
    
    return D[n]
```

```python
# DP ; Bottom-up 방식
# 시간복잡도 ~ O(n)
n = 100

D = [0] * (n+1)
D[1] = 1
D[2] = 1

for i in range(3, n+1):
    D[i] = D[i-1] + D[i-2]
    
D[n]
```



### 참고 문제

- Baekjoon #1463 - [1로 만들기] : [problem]([1463번: 1로 만들기 (acmicpc.net)](https://www.acmicpc.net/problem/1463)), [solution]()

- Baekjoon #11053 - [가장 긴 증가하는 부분수열(LIS)] : [problem]([11053번: 가장 긴 증가하는 부분 수열 (acmicpc.net)](https://www.acmicpc.net/problem/11053)), [solution]()

