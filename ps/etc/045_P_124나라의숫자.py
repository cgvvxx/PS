# Programmers - 124 나라의 숫자
# Level 2

def digit_num(n):
    base = 3
    count = 1
    while n > base:
        n -= base
        base *= 3
        count += 1

    return count, n


def divide_num(n):
    base = 1
    while n > base:
        base *= 3
    base //= 3

    divided_num = []
    while True:
        if n <= 3:
            divided_num.append(n)
            break

        if n > base:
            n -= base
            divided_num.append(base)
        else:
            base //= 3
    return divided_num


def match_124(num):
    if num == 3:
        return '4'
    else:
        return str(num)


def match_012(num):
    if num == 2:
        return '4'
    else:
        return str(num + 1)


def solution(n):
    digit_dict = dict()
    base = 1

    for exp in range(1, digit_num(n)[0]):
        base *= 3
        digit_dict[base] = 0

    for i in divide_num(digit_num(n)[1])[::-1][1:]:
        digit_dict[i] += 1

    return ''.join(list(map(match_012, list(digit_dict.values()))))[::-1] + match_124(
        divide_num(digit_num(n)[1])[::-1][0])