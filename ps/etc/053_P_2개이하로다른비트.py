# Programmers - 2개 이하로 다른 비트
# Level 2

def find_ans(numbers):
    bin_num = bin(numbers)

    if set(bin_num[2:]) == {'1'}:
        len_bin = len(bin_num)
        return bin_num[:2] + '10' + '1' * (len(bin_num) - 3)
    else:
        if bin_num[-1] == '0':
            return bin_num[:-1] + '1'
        else:
            zero_idx = bin_num.rfind('0')
            return bin_num[:zero_idx] + '10' + '1' * (len(bin_num) - zero_idx - 2)


def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(int(find_ans(num), 2))

    return answer