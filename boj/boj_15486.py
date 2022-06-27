# solved: [15486] 퇴사 2
# https://www.acmicpc.net/problem/15486
# dp
# 
# Silver 1
# dp[i] : i일 전까지(i-1일까지)의 최대 수익
# i번째 일을 안한다면 dp[i+1] = dp[i], i번째 일을 한다면 dp[i+T[i]] = dp[i] + P[i]
# 따라서 dp[i+1] = max(dp[i], dp[i+1]), dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])를 만족함

import sys
input = sys.stdin.readline

n = int(input())
T, P = [], []
for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (n+1)
for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    if i + T[i] <= n:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])
        
print(dp[-1])
