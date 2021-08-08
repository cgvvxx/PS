# Baekjoon 17298 - 오큰수
# Gold 4
# 스택/큐

n = int(input())
arr = list(map(int, input().split()))

stack = []
ans = [-1] * n

for idx, num in enumerate(arr):
    
    if not stack:
        stack.append(idx)
        continue
        
    while stack:
        if arr[stack[-1]] < num:
            ans[stack[-1]] = num
            stack.pop()
        else:
            break
    
    stack.append(idx)
    
print(*ans)