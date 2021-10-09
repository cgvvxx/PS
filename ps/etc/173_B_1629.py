# Baekjoon 1629 - 곱셉
# Silver 1
# Divide & Conquer


def pow(a, b, c):
        
    if b == 1:
        return a % c
    else:
        x = pow(a, b//2, c)
        if b % 2 == 0:
            return (x * x) % c
        else:
            return (x * x * a) % c

print(pow(*map(int, input().split())))


# 분할 정복 대표 문제
# 거듭 제곱을 O(n) => O(log n) 만큼 줄일 수 있음!