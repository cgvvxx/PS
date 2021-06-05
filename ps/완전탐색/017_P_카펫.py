# Programmers - 카펫
# Level 2
# 완전탐색

def solution(brown, yellow):

    # 가로*세로 = brown + yellow / 가로+세로 = brown/2 + 2
    # 위 식을 만족하는 연립방정식의 해(가로, 세로)를 구함
    for i in range(3, int(brown*yellow/2)):
        j = (brown + yellow) / i
        if j == int(j) and i+j == brown/2 + 2:
            break

    answer = [j, i]

    return answer