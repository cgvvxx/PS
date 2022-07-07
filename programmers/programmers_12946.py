# solved: [12946] 하노이의 탑
# https://programmers.co.kr/learn/courses/30/lessons/12946
# recursion
#
# Level 2
# 재귀적으로 hanoi 함수 구성
# n개의 원판을 1 > 3으로 옮기려면 
# 1. n-1개의 원판을 1 > 2로 옮기고
# 2. 1개의 원판을 1 > 3으로 옮기고
# 3. n-1개의 원판을 2 > 1로 옮기면 됨

def solution(n):

    def hanoi(n, a, b):

        if n == 1:
            ans.append([a, b])
        else:
            c = (set([1, 2, 3]) - set([a, b])).pop()
            hanoi(n-1, a, c)
            hanoi(1, a, b)
            hanoi(n-1, c, b)       

    ans = []
    hanoi(n, 1, 3)
    
    return ans
