# Programmers - N개의 최소공배수
# Level 2


from math import gcd

def solution(arr):
    
    def lcm(n, m):
        return n*m//gcd(n, m)
    
    answer = 1
    for i in arr:
        answer = lcm(answer, i)
        
    return answer


# math 모듈에서 gcd를 꺼내서 lcm 구하는 함수 정의
# 모든 arr의 숫자에 대해서 lcm update 반복