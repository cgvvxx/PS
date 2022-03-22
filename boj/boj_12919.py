# solved: [12919] A와 B 2
# https://www.acmicpc.net/problem/12919
# bfs, bruteforcing
# 
# Gold 5
# 처음에는 s 부터 t까지 모든 경우의 수를 체크하면서 단어를 늘려나감 > 메모리 초과 (최대 2**50가지 경우의 수)
# 역으로 t부터 s까지 단어를 하나씩 줄여나가는 모든 경우의 수를 체크
# 'A'로 끝나는 경우 앞 단어까지 / 'B'로 시작하는 경우 뒷 단어의 역순

from collections import deque


def backward(w):
    
    check = []
    
    if w[-1] == 'A':
        check.append(w[:-1])
        
    if w[0] == 'B':
        check.append(w[1:][::-1])
    
    return check

def bfs(s, t):
    
    queue = deque()
    queue.append(t)
    
    while queue:
        
        c = queue.popleft()
        
        if c == s:
            return 1
        
        if len(c) < len(s):
            return 0
        
        for w in backward(c):
            queue.append(w)
    
    return 0
            

s = input()
t = input()
print(bfs(s, t))
