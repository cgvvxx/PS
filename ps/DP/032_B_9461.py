# Baekjoon 9461 - 파도반 수열
# Silver 3
# DP

N = int(input())
inputs = [int(input()) for _ in range(N)]

D = [1] * (max(inputs) + 1)


def f(n):
    if n <= 3:
        return 1
    if D[n] > 1:
        return D[n]
    D[n] = f(n - 2) + f(n - 3)

    return D[n]


for i in inputs:
    print(f(i))