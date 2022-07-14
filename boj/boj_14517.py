# solved: [14517] 팰린드롬 개수 구하기 (Large)
# https://www.acmicpc.net/problem/14517
# dp, inclusion-and-exclusion
# 
# Platinum 5
# dp[i][j] : s[i:j]에서의 '부분수열'(연속된 부분 문자열이 아님) 중 팰린드롬의 개수
# 0. i > j라면 해당 문자열은 존재하지 않으므로 dp[i][j] = 0
# s[i:j]에서의 팰린드롬의 개수는 s[i] != s[j] 라면
# 1. i를 포함하지 않는 경우 (s[i+1:j]) 와
# 2. j를 포함하지 않는 경우 (s[i:j-1]) 의 개수에
# 3-1. i와 j를 모두 포함하지 않는 경우 (s[i+1:j-1]) 의 개수를 빼주어야 한다. (1과 2에서 중복되므로)
# 단 s[i] = s[j] 라면
# 3-2. s[i+1:j-1]에서 s[i]와 s[j]를 양쪽에 추가하면 팰린드롬이 되므로 빼주지 않아도 되고 추가로 s[i], s[j] 자체도 팰린드롬이므로 1을 더해준다.
# 따라서 다음과 같은 점화식을 만족한다.
# dp[i][j] = 0    if i > j
# dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]    if s[i] != s[j]
# dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1    otherwise

import sys
sys.setrecursionlimit(100000)

def pelin(i, j):
    
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = (pelin(i+1, j) + pelin(i, j-1)) % 10007
    if s[i] == s[j]:
        dp[i][j] += 1
    else:
        dp[i][j] -= pelin(i+1, j-1)
        
    dp[i][j] %= 10007
    
    return dp[i][j]


s = input()
n = len(s)
dp = [[0] * (n+1) for _ in range(n+1)]

print(pelin(0, n-1)) 
