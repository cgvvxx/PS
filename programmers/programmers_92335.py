# solved: [92335] k진수에서 소수 개수 구하기
# https://programmers.co.kr/learn/courses/30/lessons/92335
# mathematics, primality-test
#
# Level 2
# is_prime : 해당 숫자 n이 소수인지 체크, root(n) 까지만
# to_base_k : 해당 숫자 n을 k진수로 바꿈
# k진수로 바뀐 수를 '0'으로 split하여 각 숫자가 소수인지 아닌지 판별

def is_prime(n):
    
    n = int(n)
    m = int(n ** 0.5)
    
    if n == 1:
        return False
    
    for i in range(2, m+1):
        if n % i == 0:
            return False
    
    return True

def to_base_k(n, k):
    
    ret_n = ''
    
    while True:
        
        n, r = divmod(n, k)
        ret_n = str(r) + ret_n
        
        if n < k:
            ret_n = str(n) + ret_n
            break
    
    return ret_n

def solution(n, k):
    
    kn = to_base_k(n, k)
    
    answer = 0
    for m in kn.split('0'):
        if m and is_prime(int(m)):
            answer += 1

    return answer
