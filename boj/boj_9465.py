# solved: [9465] 스티커
# https://www.acmicpc.net/problem/9465
# dp
# 
# Silver 1
# dp[status][c] : 0 ~ c열까지 중 떼어낸 스티커의 점수의 합의 최댓값
# status = 0 ; c열에서 위의 스티커를 떼어낸 경우
# status = 1 ; c열에서 아래의 스티커를 떼어낸 경우
# status = 2 ; c열에서 스티커를 떼어내지 않은 경우
# dp[0][c+1] = max(dp[1][c], dp[2][c]) + stickers[0][c+1]
# dp[1][c+1] = max(dp[0][c], dp[2][c]) + stickers[1][c+1]
# dp[2][c+1] = max(dp[0][c], dp[1][c], dp[2][c])
#1. Bottom-up

for _ in range(int(input())):
    
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    dp = [[0 for _ in range(n)] for _ in range(3)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    for i in range(n-1):
        
        dp[0][i+1] = max(dp[1][i], dp[2][i]) + stickers[0][i+1]
        dp[1][i+1] = max(dp[0][i], dp[2][i]) + stickers[1][i+1]
        dp[2][i+1] = max(dp[0][i], dp[1][i], dp[2][i])
        
    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))


# 2. Top-down
import sys
sys.setrecursionlimit(100000)

def set_dp(status, c):
    
    if c == 0:
        if status == 2:
            return 0
        else:
            return arrs[status][c]
        
    if dp[status][c] != -1:
        return dp[status][c]
    
    if status == 2:
        dp[status][c] = max(set_dp(0, c-1), set_dp(1, c-1), set_dp(2, c-1))
    else:
        dp[status][c] = max(set_dp(1-status, c-1), set_dp(2, c-1)) + arrs[status][c]
        
    return dp[status][c]


for _ in range(int(input())):
    n = int(input())
    arrs = [list(map(int, input().split())) for _ in range(2)]
    dp = [[-1 for _ in range(n+1)] for _ in range(3)]
    print(max(set_dp(0, n-1), set_dp(1, n-1), set_dp(2, n-1)))