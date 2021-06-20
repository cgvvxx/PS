# Baekjoon 1003 - 피보나치 함수
# Silver 3
# DP

def f(n):
    if n == 0 or n == 1:
        return 1
    if D[n] > 0:
        return D[n]
    D[n] = f(n - 1) + f(n - 2)

    return D[n]


def fibo_return(x):
    if x == 0:
        print('1 0')
    elif x == 1:
        print('0 1')
    else:
        print(f'{f(x - 2)} {f(x - 1)}')


N = int(input())
inputs = []

for _ in range(N):
    inputs.append(int(input()))

D = [0] * (max(inputs) + 1);

for i in inputs:
    fibo_return(i)