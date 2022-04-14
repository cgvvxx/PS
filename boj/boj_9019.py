# solved: [9019] DSLR
# https://www.acmicpc.net/problem/9019
# bfs
#
# Gold 4
# d, s, l, r에 해당하는 연산을 정의한 후 순서대로 queue에 append하여 bfs 진행
# pypy로 약 12000 ms 소요

from collections import deque
from sys import stdin
input = stdin.readline


def bfs(a, t):
    
    queue = deque()
    visited = set()
    
    queue.append((a, ''))
    visited.add(a)
    
    while queue:
        
        x, c = queue.popleft()
        
        for com in ('D', 'S', 'L', 'R'):
            
            nx = command(com, x)
            
            if nx == t:
                return c + com
            
            if nx in visited:
                continue
                
            visited.add(nx)
            queue.append((nx, c + com))

def command(com, x):
    
    if com == 'D':
        
        x *= 2
        x %= 10000    
        
    elif com == 'S':
        
        if x == 0:
            x = 9999
        else:
            x -= 1
        
    elif com == 'L':

        y = '0'*(4-len(str(x))) + str(x)
        x = int(y[1:] + y[0])
        
    else:
        
        y = '0'*(4-len(str(x))) + str(x)
        x = int(y[-1] + y[:-1])
        
    return x


for _ in range(int(input().strip())):
    print(bfs(*map(int, input().split())))
