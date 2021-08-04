# Baekjoon 2023 - 신기한 소수
# Gold 5
# 완전탐색 - 백트래킹


def is_prime(n):
    
    n = int(n)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if n % i == 0:
            return False
    
    return True


def dfs(p):
    
    if len(p) == n:
        print(p)
        return
    
    else:
        for i in range(1, 10):
            p_now = p + str(i)
            if is_prime(p_now):
                dfs(p_now)

n = int(input())
primes = ['2', '3', '5', '7']
for prime in primes:
    dfs(prime)