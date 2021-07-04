# Programmers - 위장
# Level 2
# 해시

def solution(clothes):
    cloth_dict = dict()

    for cloth in clothes:
        try:
            cloth_dict[cloth[-1]].append(cloth[0])
        except:
            cloth_dict[cloth[-1]] = [cloth[0]]

    answer = 1
    for i in cloth_dict:
        answer *= len(cloth_dict[i]) + 1

    return answer - 1