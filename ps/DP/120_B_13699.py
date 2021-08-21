# Baekjoon 13699 - 점화식
# Silver 4
# DP


n = int(input())
dp = [0] * (n+1)

dp[0] = 1
for i in range(1, n+1):
    rec_n = 0
    for j in range(i):
        rec_n += dp[j] * dp[i-j-1]
    dp[i] = rec_n

print(dp[n])

# 기본적인 DP 문제
# dp 리스트를 할당하고 bottom-up 방식으로 품