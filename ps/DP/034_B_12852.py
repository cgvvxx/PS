# Baekjoon 12852 - 1로 만들기 2
# Silver 1
# DP

N = int(input())

maximum = 10 ** 6 + 1
D = [0] * (N + 1)
roots = ['1'] * (N + 1)

for n in range(2, N + 1):
    if n % 6 == 0:
        check = [D[n // 3], D[n // 2], D[n - 1]]
        check2 = ['a', 'b', 'c']
    elif n % 2 == 0:
        check = [D[n // 2], D[n - 1]]
        check2 = ['b', 'c']
    elif n % 3 == 0:
        check = [D[n // 3], D[n - 1]]
        check2 = ['a', 'c']
    else:
        check = [D[n - 1]]
        check2 = 'c'

    min_check = min(check)
    idx = check.index(min_check)
    D[n] = min_check + 1
    check_idx = check2[idx]

    if check_idx == 'a':
        roots[n] = str(n) + ' ' + roots[n // 3]
    elif check_idx == 'b':
        roots[n] = str(n) + ' ' + roots[n // 2]
    else:
        roots[n] = str(n) + ' ' + roots[n - 1]

print(str(D[N]))
print(roots[N])