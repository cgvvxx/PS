# Programmers - 이진 변환 반복하기
# Level 2

from collections import Counter

def solution(s):

    count = 0
    zero_num = 0

    while True:

        if s == '1':
            break

        count += 1
        if '0' in s:
            zero_num += Counter(s)['0']
            s = ''.join(s.split('0'))
            print(s, count, zero_num)


        s = bin(len(s))[2:]

    return [count, zero_num]