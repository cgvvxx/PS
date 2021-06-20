# Baekjoon 1904 - 01타일
# Silver 3
# DP

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    D = [0] * (N+1)
    D[1] = 1
    D[2] = 2
    for i in range(3, N+1):
        D[i] = (D[i-1] + D[i-2]) % 15746
    print(D[N])