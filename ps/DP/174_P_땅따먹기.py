# Programmers - 땅따먹기
# Level 2
# DP


def except_i(idx, row):
    
    max_num = 0
    for jdx in range(len(row)):
        if jdx == idx:
            continue
        if max_num < row[jdx]:
            max_num = row[jdx]
    return max_num
    

def solution(land):
    
    answer = [0]*len(land[0])

    for l in land:
        temp = [0] * len(l)
        for idx in range(len(l)):
            temp[idx] = except_i(idx, answer) + l[idx]
        answer = temp
            
    return max(answer)


# 행을 진행하면서 현재 행에서의 값 + 이전 행에서의 현재 인덱스를 제외한 최댓값으로 update 하면서
# 마지막 행의 최댓값을 구함
# dp의 memoization?!