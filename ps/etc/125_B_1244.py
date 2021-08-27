# Baekjoon 1244 - 스위치 켜고 끄기
# Silver 4

import sys
input = sys.stdin.readline


def m_switch(num):
    
    idx = num
    while idx <= n:
        lights[idx] = 1 - lights[idx]
        idx += num
        
        
def f_switch(num):
    
    lights[num] = 1 - lights[num]
    idx_left = num - 1
    idx_right = num + 1
    while idx_left > 0 and idx_right <= n:
        if lights[idx_left] == lights[idx_right]:
            lights[idx_left] = 1 - lights[idx_left]
            lights[idx_right] = 1 - lights[idx_right]
            idx_left -= 1
            idx_right += 1
        else:
            break
            
            
n = int(input())
lights = [-1] + list(map(int, input().split()))
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 1:
        m_switch(b)
    else:
        f_switch(b)

start = 1
end = 21
while True:
    print(*lights[start:end])
    start += 20
    end += 20

    if start > len(lights) - 1:
        break
