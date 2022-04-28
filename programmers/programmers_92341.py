# solved: [92341] 주차 요금 계산
# https://programmers.co.kr/learn/courses/30/lessons/92341
# implementation
#
# Level 2
# 특별한 아이디어는 필요없는 구현 문제
# 문제 조건에 맞추어서 차근차근 함수 정의 > 문제 해결

from collections import defaultdict
import math

def cal_fee(fees, time):
    
    a, b, c, d = fees
    if time <= a:
        return b
    else:
        return b + math.ceil((time - a) / c) * d
    
    
def to_min(t):
    a, b = map(int, t.split(':'))
    return 60 * a + b

    
def cal_time(t1, t2):
    return to_min(t2) - to_min(t1)


def solution(fees, records):
    
    car_dict = defaultdict(list)
    fee_dict = defaultdict(int)
    for rec in records:
        time, car, status = rec.split()

        if status == 'IN':
            car_dict[car].append(to_min(time))
        else:
            in_time = car_dict[car].pop()
            take_time = to_min(time) - in_time
            fee_dict[car] += take_time

    for i in car_dict:
        if car_dict[i]:
            take_time = to_min('23:59') - car_dict[i].pop()
            fee_dict[i] += take_time

    for j in fee_dict:
        fee_dict[j] = cal_fee(fees, fee_dict[j])
    
    answer = list(fee_dict.items())
    answer.sort()
    
    return list(map(lambda x:x[1], answer))
