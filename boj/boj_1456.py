# solved: [1456] 거의 소수
# https://www.acmicpc.net/problem/1456
# primality-test
# 
# Silver 1
# b의 제곱근보다 작거나 같은 수까지의 소수 리스트를 구한 후
# 그 소수의 거듭제곱이 a보다 크거나 b보다 작거나 같을 때 ans += 1

def is_prime(n):
    
    n = int(n)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if n % i == 0:
            return False
    
    return True

def prime_list(n):
    
    primes = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]]


a, b = map(int, input().split())
ans = 0

for p in prime_list(int(b**(1/2))+1):

    m = p**2
    while m <= b:
        if m >= a:
            ans += 1
        m *= p
            
print(ans)
