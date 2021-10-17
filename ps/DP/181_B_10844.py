# Baekjoon 10844 - 쉬운 계단 수
# Silver 1
# DP


n = int(input())
div = 1000000000
dp = [[0] * (n+1) for _ in range(10)]

for i in range(1, 10):
    dp[i][1] = 1

for j in range(2, n+1):
    for i in range(10):
        if i == 0:
            dp[i][j] = dp[1][j-1] % div
        elif i == 9:
            dp[i][j] = dp[8][j-1] % div
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i+1][j-1]) % div
            
print(sum([dp[i][-1] for i in range(10)]) % div)
    
    
# dp[i][j] = j개의 숫자로 이루어진 수 중 마지막 자리의 수가 i인 계단수의 개수
# 점화식은 dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1] (0 < i < 9), i가 0 또는 8일 떄는 dp[1][j-1] 과 dp[8][j-1]
# 위의 점화식과 memoization을 이용 + 1000000000으로 나눈 나머지를 저장