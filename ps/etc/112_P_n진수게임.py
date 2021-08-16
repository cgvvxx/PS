# Programmers - n진수 게임
# Level 2


def base_n(num, n):
    
    bases = '0123456789ABCDEF'
    n_num = ''
    
    while num >= 1:
        
        num, r = divmod(num, n)
        n_num += bases[r]
        
    return n_num[::-1]

def solution(n, t, m, p):
    
    long_string = '0' + ''.join(map(base_n, range(m*t), [n]*(m*t)))
    answer = long_string[p-1::m][:t]
    
    return answer