# solved: [2331] 반복수열
# https://www.acmicpc.net/problem/2331
# implementation
# 
# Silver 4
# D : 각 자리의 숫자를 p번 곱한 수들의 합
# D 함수로 다음 수열을 만들어 나가면서 해당 숫자가 이전 수열에 있을 경우(set으로 체크) 해당 값의 index를 return

def D(n, p):
    
    ans = 0
    for i in str(n):
        i = int(i)
        ans += i ** p
        
    return ans


n, p = map(int, input().split())
num_list = [n]
num_set = set(num_list)

while True:
    
    cur = num_list[-1]
    nxt = D(cur, p)
    
    if nxt in num_set:
        print(num_list.index(nxt))
        break
    
    num_list.append(nxt)
    num_set.add(nxt)       
