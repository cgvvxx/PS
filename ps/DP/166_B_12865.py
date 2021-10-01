# Baekjoon 12865 - 평범한 배낭
# Gold 5
# DP


items = []
n, k = map(int, input().split())
for _ in range(n):
    items.append(tuple(map(int, input().split())))

DP = [[0] * (k+1) for _ in range(n)]
for i in range(n):
    for j in range(k+1):
        w, v = items[i]
        
        if i == 0:
            if j >= w:
                DP[i][j] = v
            continue
    
        if j < w:
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-w]+v)
                
print(max([DP[i][-1] for i in range(n)]))


# 전형적인 knapsack 알고리즘이라고 함
# DP 배열을 2차원으로 만들고 dp[i][j] = max(dp[i-1][j], dp[i][j-w[i]]+v[i])의 점화식 사용
# DP 문제 어려움 ... > DP 관련 문제들은 유형별로 문제를 풀어보고 관련 유형을 익히는게 우선일 듯