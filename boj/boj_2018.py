# solved: [2018] 수들의 합 5
# https://www.acmicpc.net/problem/2018
# two-pointer
#
# Silver 5
# i~j 까지의 합을 s라고 할 때, 
# s <= n이면 j += 1, s > n 이면 i += 1로 전진하면서 s==n인 경우의 수를 카운트

n = int(input())
i, j = 0, 0
cnt = 0
s = 0

while j <= 100000000:
    
    if j > n:
        break
    
    if s <= n:
        j += 1
        s += j
    else:
        i += 1
        s -= i
        
    if s == n:
        cnt += 1

print(cnt)
