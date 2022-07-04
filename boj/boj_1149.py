# solved: [1149] RGB 거리
# https://www.acmicpc.net/problem/1149
# dp
# 
# Silver 1
# dp[i][j] : i번째 집을 빨강(j=0), 초록(j=1), 파랑(j=2)로 칠했을 때의 최소 비용
# 이전의 집(i-1번째)과 다른 색으로 칠했을 때의 최댓값을 구하면되므로 다음과 같은 점화식을 만족
# dp[i][j] = sum(dp[i-1][k]) + cost[i][j] (k != j)

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0, 0, 0] for _ in range(n)]
dp[0] = cost[0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[n-1]))    
