# solved: [9084] 동전
# https://www.acmicpc.net/problem/9084
# dp
# 
# Gold 5
# boj 2293 동전 1과 동일한 로직
# dp[i] : i원을 만드는 동전의 경우의 수
# 모든 동전 c에 대해, dp[i] = dp[i] + dp[i-c] (i>=c)

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)
    dp[0] = 1

    for c in coins:
        for i in range(1, M+1):
            if i - c >= 0:
                dp[i] += dp[i-c]

    print(dp[M])
