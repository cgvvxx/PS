# solved: [4796] 캠핑
# https://www.acmicpc.net/problem/캠핑
# greedy
# 
# Silver 5
# 단순히 0일이 휴가의 시작인 경우 전체 휴가 일정이 최대가 됨

idx = 0
while True:
    l, p, v = map(int, input().split())
    
    if l == p == v == 0:
        break
        
    q = (v // p) * l
    r = v % p
    
    if r >= l:
        q += l
    else:
        q += r
        
    idx += 1
    print(f"Case {idx}: {q}")        
