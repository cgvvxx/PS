# solved: [2156] 포도주 시식
# https://www.acmicpc.net/problem/2156
# dp
#
# Silver 1
# dp ; n * 3, dp[i][k]는 i번째 포도주를 마시는 경우에 대해 k번 연속 마시는 양
# dp[i][0] ; i-1번째 포도주를 마시는 경우의 최댓값
# dp[i][1] ; i-1번째에서 포도주를 안 마시는 경우
# dp[i][2] ; i-1번째에서 포도주를 1번 연속 마시는 경우
# dp[i]의 최댓값 return

import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]

if n == 1:
    print(wines[0])
else:
    dp[0] = [0, wines[0], wines[0]]
    dp[1] = [wines[0], wines[1], wines[0]+wines[1]]
    for i in range(2, n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + wines[i]
        dp[i][2] = dp[i-1][1] + wines[i]

    print(max(dp[-1]))
