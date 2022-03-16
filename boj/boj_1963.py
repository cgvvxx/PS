# solved: [1963] 소수 경로
# https://www.acmicpc.net/problem/1963
# graph-traversal, bfs
#
# Gold 4
# 10000 까지의 소수 리스트를 먼저 구한 후
# 1. 주어진 수에서 한 자리를 바꾸어가면서(bfs) 소수 체크 
# 2. 소수인 경우 각 루트까지의 길이를 ps_dict에 기록
# 3. 원하는 숫자가 등장하면 그 때까지의 루트의 길이를, 나오지 않는 경우 'Impossible'을 return


from collections import deque


def prime_list(n):
    
    primes = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if primes[i]:
            for j in range(i+i, n+1, i):
                primes[j] = False
    
    return [i for i in range(2, n+1) if primes[i]]

def change_char(num, idx, char):
    
    check = list(str(num))
    check[idx] = str(char)
    
    return int(''.join(check))

def get_change_nums(a, b):
    
    if a == b:
        return 0
    
    ps_dict = dict(zip(ps, [0]*len(ps)))
    queue = deque()
    queue.append(a)
    ps_dict[a] = 1
    
    while queue:
        
        x = queue.popleft()
        
        for i in range(4):
            for j in range(10):

                nx = change_char(x, i, j)
                
                if nx == b:
                    return ps_dict[x]

                if nx < 1000:
                    continue

                if nx in ps_dict and ps_dict[nx] == 0:
                    ps_dict[nx] = ps_dict[x] + 1
                    queue.append(nx)
    
    return 'Impossible'


ps = prime_list(10000)

for _ in range(int(input())):
    print(get_change_nums(*map(int, input().split())))
