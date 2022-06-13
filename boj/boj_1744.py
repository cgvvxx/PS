# solved: [1744] 수 묶기
# https://www.acmicpc.net/problem/1744
# greedy, sorting
# 
# Gold 4
# 단순히 그리디하게 양수끼리 제일 큰 수 짝들끼리의 곱의 합, 음수들끼리 제일 큰 수 짝들끼리의 곱의 합을 구하면 됨
# 단, 몇 가지 반례 생각해야함
# 1. 1이 여러 개 있는 경우 => 1은 무조건 더해야 합이 최대가 됨
# 2. 0이 있는 경우 => 음수들의 짝들끼리의 곱을 통해 하나의 음수가 나오는 경우 0과 곱해야 최소가 됨

plus = []
minus = []
is_zero = False

n = int(input())
for _ in range(n):
    a = int(input())
    if a > 0:
        plus.append(a)
    elif a < 0:
        minus.append(-a)
    else:
        is_zero = True
        
plus.sort()
minus.sort()
ans = 0

while len(plus) >= 2:
    
    a = plus.pop()
    b = plus.pop()
    
    if a == 1 or b == 1:
        ans += a + b
        break
    
    ans += a*b

if plus:
    ans += sum(plus)

while len(minus) >= 2:
    
    a = minus.pop()
    b = minus.pop()

    ans += a*b
    
if minus and not is_zero:
    ans -= minus[0]
    
print(ans)    
