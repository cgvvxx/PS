# Baekjoon 9421 - 소수상근수
# Silver 1
# DP

def sum_square(num):
    
    sums = 0
    for char in str(num):
        sums += int(char)**2
        
    return sums

def is_sanggeun(num):
    
    repeated = set()
    
    while True:
        squared_sum = sum_square(num)
        
        if squared_sum == 1: return True
        if squared_sum in repeated: return False
            
        repeated.add(squared_sum)
        num = squared_sum
        
def prime_list(num):

    is_primes = [True] * (num+1)
    root_num = int(num**0.5)
    
    for i in range(2, root_num+1):
        if is_primes[i]:
            for j in range(2*i, num+1, i):
                is_primes[j] = False
    
    return [k for k in range(2, num+1) if is_primes[k]]

n = int(input())
primes = prime_list(n)
for i in primes:
    if is_sanggeun(i):
        print(i)