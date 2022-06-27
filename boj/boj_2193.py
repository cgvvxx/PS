# solved: [2193] 이친수
# https://www.acmicpc.net/problem/2196
# dp
# 
# Silver 3
# dp : 2 X n 행렬
# dp[0][n] : n자리수 중 끝이 0으로 끝나는 숫자의 갯수
# dp[1][n] : n자리수 중 끝이 0으로 끝나는 숫자의 갯수
# dp[0][n+1] = dp[0][n] + dp[1][n], dp[1][n+1] = dp[0][n] 점화식을 만족

n = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(2)]

dp[1][1] = 1
for i in range(1, n):
    dp[0][i+1] = dp[0][i] + dp[1][i]
    dp[1][i+1] = dp[0][i]
    
print(dp)
print(dp[0][n]+dp[1][n])
