# solved: [1932] 정수 삼각형
# https://www.acmicpc.net/problem/1932
# dp
# 
# Silver 1
# dp[i][j]는 (i, j) 번째 수로 오는 경로의 합의 최댓값
# dp[i][0] = dp[i-1][0] + graphs[i][0], dp[i][i] = dp[i-1][i-1] + graphs[i][i] (j == 0 or j == i)
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graphs[i][j] (j != 0 and j != i)를 만족

def solution(triangle):
    count = triangle[:]
    for i in range(len(triangle)):
        for j in range(i+1):
            if i == 0:
                continue
            if j == 0:  
                count[i][j] += count[i-1][j]
            elif j == i:  
                count[i][j] += count[i-1][j-1]
            else:
                count[i][j] += max(count[i-1][j-1], count[i-1][j])
        
    return max(count[-1])

arrays = []
for _ in range(int(input())):
    arrays.append([*map(int, input().split())])
print(solution(arrays))
