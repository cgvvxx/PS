# Programmers - 영어 끝말잇기
# Level 2

import math

def solution(n, words):
    used_words = []
    before = ' '
    check = False
    for idx in range(len(words)):
        if words[idx] in used_words:
            check = True
            break
        elif idx != 0 and before[-1] != words[idx][0]:
            check = True
            break
        else:
            before = words[idx]
            used_words.append(words[idx])

    if check:
        idx += 1
        if idx % n == 0:
            idx_n = n
        else:
            idx_n = idx % n
        return [idx_n, math.ceil(idx / n)]
    else:
        return [0, 0]