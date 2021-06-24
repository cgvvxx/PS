# Baekjoon 1463 - 1로 만들기
# Silver 3
# DP

# 1.

N = int(input())

if N == 1:
    print(0)
elif N <= 3:
    print(1)
else:
    D = [0] * (N + 1)
    D[2], D[3] = 1, 1

    for n in range(3, N + 1):
        if n % 6 == 0:
            D[n] = min(D[n // 3], D[n // 2], D[n - 1]) + 1
        elif n % 2 == 0:
            D[n] = min(D[n // 2], D[n - 1]) + 1
        elif n % 3 == 0:
            D[n] = min(D[n // 3], D[n - 1]) + 1
        else:
            D[n] = D[n - 1] + 1

    print(D[N])

# 2. if문 없이 코드 간단히
N = int(input())

D = [0] * (10 ** 6 + 1)

for i in range(2, N + 1):
    D[i] = D[i - 1] + 1
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)

print(D[N])