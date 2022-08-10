# solved: [11726] 2xn 타일링
# https://www.acmicpc.net/problem/11726
# dp
# 
# Silver 3
# dp[n]는 2*n 크기의 직사각형을 채우는 방법의 수
# dp[n+2] = dp[n+1] + dp[n]를 만족 
# n+2 크기의 직사각형을 만들려면 n 크기의 직사각형에 =를 추가하거나 n+1 크기의 직사각형에 |를 추가하는 2가지 경우만 존재

n = int(input())
if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2])%10007
    print(dp[n])
