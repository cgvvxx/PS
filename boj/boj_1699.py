# solved: [1699] 제곱수의 합
# https://www.acmicpc.net/problem/1699
# dp
# 
# Silver 2
# dp[n] : n을 제곱수의 합으로 표현할 때 최소 개수
# j + i ** 2 < n일 때, dp[j + i**2] = min(dp[j]+1, dp[j+i**2]) (for j=1,2,3,...)

n = int(input())
dp = [100001] * (n+1)
i = 1

dp[0] = 0
dp[1] = 1

while i**2 <= n: 
    for j in range(n):
        if j + i**2 > n:
            break
        else:
            dp[j+i**2] = min(dp[j]+1, dp[j+i**2])    
    i += 1

print(dp[n])
