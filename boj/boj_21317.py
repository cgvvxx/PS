# solved: [21317] 징검다리 건너기
# https://www.acmicpc.net/problem/21317
# dp
# 
# Silver 2
# dp : 2 X n 행렬
# dp[0][n] : 매우 큰 점프 x, n번째 돌까지 소비한 에너지
# dp[1][n] : 매우 큰 점프 o, n번째 돌까지 소비한 에너지
# dp[0][i] = min(dp[0][i-2]+big[i-3], dp[0][i-1]+small[i-2])
# & dp[1][i] = min(dp[0][i-3]+k, dp[1][i-2]+big[i-3], dp[1][i-1]+small[i-2])
# 이 때, 주어진 점화식들은 dp[i][j]가 잘 정의될때여야 하고 n <= 3인 경우는 그냥 경우 다 나누어서 적용하여 지저분해짐..

n = int(input())
small = []
big = []
for _ in range(n-1):
    s, b = map(int, input().split())
    small.append(s)
    big.append(b)
k = int(input())

if n >= 4:
    dp = [[0] * (n+1) for _ in range(2)]

    dp[0][2] = small[0]
    dp[0][3] = min(dp[0][2] + small[1], big[0])
    dp[1][4] = k

    for i in range(4, n+1):
        dp[0][i] = min(dp[0][i-2]+big[i-3], dp[0][i-1]+small[i-2])

        if i == 4:
            continue

        if i >= 5:
            dp[1][i] = min(dp[0][i-3]+k ,dp[1][i-1]+small[i-2])
        if i >= 6:
            dp[1][i] = min(dp[1][i] ,dp[1][i-2]+big[i-3])

    print(min(dp[0][n], dp[1][n]))
elif n == 3:
    print(min(small[0] + small[1], big[0]))
elif n == 2:
    print(small[0])
elif n == 1:
    print(0)
