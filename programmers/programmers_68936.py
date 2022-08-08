# solved: [68936] 쿼드압축 후 개수 세기
# https://programmers.co.kr/learn/courses/30/lessons/68936
# divide-and-conquer
#
# Level 2
# 재귀적으로 주어진 그래프의 1/4 부분에 대하여 하나의 숫자인지 or 1개로 이루어져 있는지 체크하여
# 0과 1의 개수를 카운팅

def dq(arr):
    
    global zero, one
    
    if len(arr) == 1 or len(set(sum(arr, []))) == 1:
        if arr[0][0]:
            one += 1
        else:
            zero += 1
        return
    
    m = len(arr) // 2
    for i in range(2):
        for j in range(2):
            new_arr = [[arr[m*i+k][m*j+l] for l in range(m)] for k in range(m)]
            dq(new_arr)
            

def solution(arr):
    
    global zero, one
    zero, one = 0, 0
    
    dq(arr)
    
    return [zero, one]
