# Baekjoon 15990 - 1, 2, 3 더하기 5
# Silver 2
# DP


dp = [[0, 0, 0] for _ in range(10**5+1)]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

max_n = 0
nums = []
for _ in range(int(input())):
    n = int(input())
    
    nums.append(n)
    if n > max_n:
        max_n = n

for i in range(4, max_n+1):
    dp[i] = [(dp[i-1][1] + dp[i-1][2]) % 1000000009, (dp[i-2][0] + dp[i-2][2]) % 1000000009, (dp[i-3][0] + dp[i-3][1]) % 1000000009]
    
for n in nums:
    print(sum(dp[n]) % 1000000009)
    
    
# 점화식을 활용한 dp 문제
# n 이라는 수의 1, 2, 3 으로 끝나는 더하기 방법의 개수를 dp[n] 이라고 하면
# n+1 이라는 수의 더하기 방법의 1, 2, 3 으로 끝나는 더하기 방법의 개수는
# dp[n][1]+dp[n][2], dp[n-1][0]+dp[n-1][2], dp[n-2][0]+dp[n-2][1] 임을 이용하여 해결
# 1000000009 로 나눠주는 부분 빼먹지 말 것