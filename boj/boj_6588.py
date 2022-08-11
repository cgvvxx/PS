# solved: [6588] 골드바흐의 추측
# https://www.acmicpc.net/problem/6588
# primality-test, sieve-of-eratosthenes
# 
# Silver 1
# 가장 큰 숫자 기준으로 prime_list를 구한 후
# prime_list에서 작은 수 p를 꺼내면서 n-p 또한 소수인지 체크


def prime_list(n):
    
    primes = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]][1:]


nums = []
max_n = 0
while 1:
    num = int(input())
    max_n = max(num, max_n)
    if num == 0:
        break
    nums.append(num)
    
p_list = prime_list(max_n)
p_set = set(p_list)

for num in nums:
    for p in p_list:
        if (num-p) in p_set:
            print(f'{num} = {p} + {num-p}')
            break  
