# solved: [1747] 소수&팰린드롬
# https://www.acmicpc.net/problem/1747
# primality test
#  
# Silver 1
# t보다 큰 소수 리스트를 만들어 놓고 해당 소수가 팰린드롬인지 체크 후 print
# 1000000보다 큰 소수이면서 팰린드롬인 수는 1003001이므로 최댓값은 해당 수로 고정함

def prime_list(n, t):
    
    primes = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
                
    return [i for i in range(2, n+1) if primes[i] and i >= t]


for p in prime_list(1003002, int(input())):
    if str(p) == str(p)[::-1]:
        print(p)
        break
