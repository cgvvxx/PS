# solved: [87390] n^2 배열 자르기
# https://programmers.co.kr/learn/courses/30/lessons/87390
# implementation
#
# Level 2
# 실제 2차원 배열을 만들어 1차원 배열로 자르면 시간 초과
# 1. left와 right를 포함하는 행들로 my_list를 만들고 
# 2. left, right에 해당하는 인덱스로 my_list slicing


def solution(n, left, right):
    
    left_s = left // n
    right_e = right // n
    
    my_list = []
    for i in range(left_s + 1, right_e + 2):
        my_list += [i]*(i-1) + list(range(i, n+1))
    
    ls = left - left_s * n
    re = right + 1 - n * (right_e + 1)
    
    if re == 0:
        return my_list[ls:]
    else:
        return my_list[ls:re]
