# solved: [2294] 동전 2
# https://www.acmicpc.net/problem/2294
# dp
# 
# Silver 1
# dp[i] : i 만큼의 가치를 만드는 동전의 최소 개수
# 모든 코인 가치 c에 대해서 dp[i] = min(dp[i], dp[i-c]+1) 

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10**5] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for c in coins:
        if i - c < 0:
            continue
        else:
            dp[i] = min(dp[i], dp[i-c]+1)    

if dp[-1] >= 10**5:
    print(-1)
else:
    print(dp[-1])
