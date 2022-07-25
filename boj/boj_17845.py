# solved: [17845] 수강 과목
# https://www.acmicpc.net/problem/17845
# dp
# 
# Gold 5
# 0-1 knapsack과 동일한 dp 점화식 활용

T, N = map(int, input().split())
KS = []
for _ in range(N):
    KS.append(tuple(map(int, input().split())))
    
dp = [[0] * (T+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, T+1):
        
        s, k = KS[i-1]
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)
            
print(dp[N][T]) 
