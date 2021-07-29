# Baekjoon 2841 - 외계인의 기타 연주
# Silver 1
# 스택/큐

import sys

N, P = map(int, sys.stdin.readline().strip().split())

fingers = []
for _ in range(N):
    fingers.append(list(map(int, sys.stdin.readline().strip().split())))
    
stacks = [[] for _ in range(7)]
count = 0
for finger in fingers:
    stack = stacks[finger[0]]
    
    if stack:
        while stack[-1] > finger[1]:
            stack.pop()
            count += 1
            
            if not stack:
                break
            
            if stack[-1] == finger[1]:
                break
                
    if stack and stack[-1] == finger[1]:
        continue
        
    stack.append(finger[1])
    count += 1
    
print(count)