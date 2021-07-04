# Programmers - N으로 표현
# Level 3
# DP

def expr(a, b):  # a와 b의 사칙연산으로 만들 수 있는 값들의 리스트 return
    expr = [a + b, a * b, a - b, b - a, a // b, b // a]
    expr = [i for i in expr if i >= 0 and i <= 32000]
    return list(set(expr))


def solution(N, number):
    answer = [[] for i in range(10)]  # i번째 원소는 연산을 i번 수행해서 만들어질 수 있는 값의 리스트
    check = []
    for i in range(1, 6):  # N=2 인 경우, 2, 22, 222 등은 2를 1번, 2번, 3번 사용하여 만들수 있음
        if int(str(N) * i) <= 32000:
            if number == int(str(N) * i):
                return i
            answer[i].append(int(str(N) * i))
            check.append(int(str(N) * i))

    if number == 0:
        return 2
    answer[2].append(0)  # 0의 경우, N-N으로 항상 2번의 연산을 통해 만들 수 있음
    check.append(0)

    # i번째 연산을 통해 만들어질 수 있는 수는
    # j번 연산을 통해 만들어진 수 + i-j번째 연산을 통해 만들어진 수(0 <= j < i)
    for i in range(2, 9):
        for j in range(1, i // 2 + 1):
            for a in answer[j]:
                for b in answer[i - j]:
                    if a * b != 0:
                        for ele in expr(a, b):
                            if ele == number:  # number가 나오는 경우 바로 return
                                return i
                            if ele not in answer[i] and ele not in check:
                                answer[i].append(ele)
                                check.append(ele)
    return -1