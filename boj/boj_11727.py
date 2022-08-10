# solved: [11727] 2xn 타일링 2
# https://www.acmicpc.net/problem/11727
# dp
# 
# Silver 3
# boj 11726과 비슷
# dp[n]는 2*n 크기의 직사각형을 채우는 방법의 수
# dp[n+2] = dp[n+1] + 2*dp[n]를 만족 
# n+2 크기의 직사각형을 만들려면 n크기의 직사각형에 = 또는 ㅁ을 추가하는 2가지 경우 또는 n+1 크기의 직사각형에 |를 추가하는 1가지 경우가 존재

n = int(input())
if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2*dp[i-2])%10007
        
    print(dp[n])
