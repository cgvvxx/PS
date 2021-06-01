# Programmers - 줄 서는 방법
# Level 3
# 동적계획법

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def fact_notation(n, k):
    k = k - 1
    fact_li = []
    for i in range(1, n):
        fact_li.append(k // fact(n - i))
        k = k % fact(n - i)

    return fact_li


def solution(n, k):
    answer = []
    check = list(range(1, n + 1))

    for i in fact_notation(n, k):
        answer.append(check.pop(i))

    answer.append(check[0])

    return answer
