# solved: [42897] 도둑질
# https://programmers.co.kr/learn/courses/30/lessons/42897
# dp
#
# Level 4
# steal(money) : 주어진 money 배열이 선형적이라고 할 때, dp를 이용해 훔칠 수 있는 돈의 최댓값 return
# dp[n] : [n번째 마을을 안 훔쳤을 때 n번째 까지의 훔친 돈의 최댓값, n번째 마을을 훔쳤을 때, n번째 까지의 훔친 돈의 최댓값]
# 따라서 다음과 같은 점화식을 만족
# dp[n][0] = max(dp[n-1][0], dp[n-1][1]) ; n-1번째 마을은 훔쳤을 때와 훔치지 않았을 때 중의 돈의 최댓값
# dp[n][1] = dp[n-1][0] + money[n] ; n-1번째 마을은 훔치지 않고, n번째 마을은 훔치는 경우
# 주어진 문제의 경우 원형으로 이어져 있으므로,
# 1. 첫번째 마을은 훔치고, 마지막 마을은 훔치지 않는 경우
# 2. 첫번째 마을은 훔치지 않고, 마지막 마을은 훔치는 경우 둘 중 최댓값
# 1의 경우 두번째 마을은 훔치지 않아야 하므로, 3 ~ n-1 번째 마을들에서 훔치는 돈의 최댓값 + 1번째 마을의 돈
# 2의 경우, 2 ~ n-1 번째 마을들에서 훔치는 돈의 최댓값 + n번째 마을의 돈

def steal(money):
    
    n = len(money)
    dp = [[0, 0] for _ in range(n)]
    
    dp[0] = [0, money[0]]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1])
        dp[i][1] = dp[i-1][0] + money[i]

    return dp[-1]
            
def solution(money):
    
    n = len(money)

    return max(max(steal(money[2:n-1])) + money[0], steal(money[1:n-1])[0] + money[-1])
