# Baekjoon 5430 - AC
# Gold 5
# 스택/큐

import sys
from collections import deque


def print_list(li):
    
    print('[', end='')
    for idx, i in enumerate(li):
        if idx == len(li)-1:
            print(i, end='')
        else:
            print(i, end=',')
    print(']')


n = int(input())
answer = []

for _ in range(n):
    commands = sys.stdin.readline().strip()
    len_array = int(sys.stdin.readline().strip())
    series = sys.stdin.readline().strip().strip('[').strip(']').split(',')
    reverse = 0

    if len_array:
        array = deque(list(map(int, series)))
    else:
        array = deque()
        
    try:
        for com in commands:
            if com == 'R':
                reverse += 1
            else:
                if reverse % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
        if reverse % 2 == 1:
            array.reverse()
        answer.append(list(array))
    except:
        answer.append('error')
        
for i in answer:
    if i != 'error':
        print_list(i)
    else:
        print(i)