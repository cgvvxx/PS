# solved: [11057] 오르막 수
# https://www.acmicpc.net/problem/11057
# dp
# 
# Silver 1
# dp : 10 X n 행렬
# dp[n][i] : n자리수 중 끝이 i로 끝나는 숫자의 개수
# dp[n+1][i] = dp[n][0] ~ dp[n][i]의 합의 점화식을 만족
# 예를 들어, dp[3][4]는 3자리 수 중 4로 끝나는 수의 개수이고, 이는 2자리 수중 0~4로 끝나는 수를 이용하여 하나씩 만들 수 있음

n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[1] = [1] * 10

for i in range(1, n):
    for j in range(10):
        for k in range(j+1):
            dp[i+1][j] += dp[i][k]
            dp[i+1][j] %= 10007
            
print(sum(dp[n]) % 10007)
