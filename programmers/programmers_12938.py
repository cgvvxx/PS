# solved: [12938] 최고의 집합
# https://programmers.co.kr/learn/courses/30/lessons/12938
# programmers_92343.py
#
# Level 3
# 산술기하 부등식에서 합이 일정할 때 곱의 최댓값은 각 수가 모두 같을 때 발생
# 각 수가 모두 같을 수 없으면, 그 차이가 가장 적을때 최대가 됨을 이용

def solution(n, s):
       
    q = s // n
    r = s % n
    
    if q == 0:
        return [-1]
    else:
        return [q] * (n-r) + [q+1] * r
