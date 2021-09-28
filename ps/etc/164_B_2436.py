# Baekjoon 2436 - 공약수
# Gold 5


import math

g, l = map(int, input().split())

if g == l:
    print(f'{g} {l}')
else:
    k = l//g
    sqrt = int(math.sqrt(k))
    
    while True:
        if k % sqrt == 0 and math.gcd(sqrt, k//sqrt) == 1:
            print(f'{g*sqrt} {g*(k//sqrt)}')
            break
        sqrt -= 1
        
        
# 수학 문제에 가까운듯
# A=Ga, B=Gb, L=Gab (G:gcd, L:lcm, a,b서로소)이고 a+b가 최소인 a,b를 찾는 문제
# 곱이 일정할 때 합의 최솟값은 두 수의 차이가 작을 때 나오므로
# ab의 제곱근부터 시작해서 1씩 감소시켜가면서 a, b가 서로소인 경우를 찾으면 됨