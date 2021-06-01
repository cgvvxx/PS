# Programmers - 멀리뛰기
# Level 3
# 동적계획법

def solution(n):
    fibo_li = [1, 2]
    for i in range(2, 2000):
        fibo_li.append(fibo_li[i - 1] + fibo_li[i - 2])

    answer = fibo_li[n - 1] % 1234567

    return answer
