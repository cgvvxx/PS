# solved: [2293] 동전 1
# https://www.acmicpc.net/problem/2293
# dp
# 
# Gold 5
# dp[i] : i원을 만드는 동전의 경우의 수
# 모든 동전 c에 대해, dp[i] = dp[i] + dp[i-c] (i>=c)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]    

dp = [0] * (k+1)
dp[0] = 1

for c in coins:
    for i in range(1, k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]
            
print(dp[k])
