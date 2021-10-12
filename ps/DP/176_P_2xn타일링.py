# Programmers - 2 x n 타일링
# Level 3
# DP


def solution(n):
    if n == 1:
        return 1
    else:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2])%1000000007
        return dp[n]
    
    
# 점화식을 활용한 DP 문제
# a1 = 1, a2 = 2, a_n = a_(n-1) + a_(n-2)와 memoization을 이용하여 해결
