# solved: [2812] 크게 만들기
# https://www.acmicpc.net/problem/2812
# greedy, stack
# 
# Gold 3
# 앞에서 부터 stack에 넣어가면서 더 큰 숫자가 나오면 k개만큼 버림
# 즉, 앞의 숫자가 뒤의 숫자보다 작은 경우가 나올 때마다 k번 버려야 함
# 이 때 다 버리지 못한 경우 stack에 있는 숫자중 최초 n-k개 만큼의 숫자만 활용하여 프린트

n, k = map(int, input().split())
num = list(input())
r = n-k

stack = []
for i, s in enumerate(num):
    
    while stack and k:
        chk = stack[-1]
        if chk < s:
            stack.pop()
            k -= 1
        else:
            stack.append(s)
            break
    else:
        stack.append(s)
        
    if not k:
        break
        
if k:
    print(''.join(stack[:r]))
else:
    ans = stack + num[i+1:]
    print(''.join(ans))
