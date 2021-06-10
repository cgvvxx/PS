# Programmers - 숫자의 표현
# Level 2

def solution(n):
    num_list = list(range(1, n + 1))
    left, right = 0, 1
    answer = 0

    while left < n or right < n:
        sum_list = sum(num_list[left:right])
        if sum_list > n:
            left += 1
        elif sum_list < n:
            right += 1
        else:
            answer += 1
            left += 1

    return answer