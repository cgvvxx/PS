# solved: [1890] 점프
# https://www.acmicpc.net/problem/1890
# dp
# 
# Silver 1
# dp : n X n 행렬
# 각각의 좌표를 돌면서 현재 좌표에서 오른쪽, 아래 방향 좌표의 현재 dp값을 더해나가면서 dp[-1][-1]을 print

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        
        if (i, j) == (n-1, n-1):
            print(dp[i][j])
        
        x = i + graphs[i][j]
        y = j + graphs[i][j]
        
        if x < n:
            dp[x][j] += dp[i][j]
        if y < n:
            dp[i][y] += dp[i][j]
