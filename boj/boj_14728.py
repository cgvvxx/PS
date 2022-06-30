# solved: [14728] 벼락치기
# https://www.acmicpc.net/problem/14728
# dp
# 
# Gold 5
# 0-1 knapsack과 동일한 dp 점화식 활용

N, T = map(int, input().split())
KS = []
for _ in range(N):
    KS.append(tuple(map(int, input().split())))
    
dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, T+1):
        
        k, s = KS[i-1]
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)
            
print(dp[N][T])     
