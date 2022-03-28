# solved: [16953] A -> B
# https://www.acmicpc.net/problem/16953
# bfs
# 
# Silver 1
# a -> b로 가는 경우 bfs & 완전탐색으로 2**9의 경우이지만
# b -> a로 가는 경우 그 보다 적은 경우의 수 탐색이 가능
# b가 2의 배수이면 b의 절반을, b가 1로 끝나면 1을 제외한 수를 queue에 넣고
# 이러한 과정을 while문으로 반복

from collections import deque


a, b = map(int, input().split())
queue = deque()
queue.append((b, 0))

while queue:
    
    x, cnt = queue.popleft()
    
    if x == a:
        print(cnt+1)
        break
    
    if x % 2 == 0:
        queue.append((x // 2, cnt+1))
        
    if x >= 10 and str(x)[-1] == '1':
        queue.append((int(str(x)[:-1]), cnt+1))
        
else:
    print(-1)
