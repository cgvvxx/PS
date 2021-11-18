# Baekjoon 9184 - 신나는 함수 실행
# Silver 2
# DP


def w(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]
    
    if a < b < c:
        if dp[a][b][c] == 0:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]
        else:
            return dp[a][b][c]
    else:
        if dp[a][b][c] == 0:
            dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return dp[a][b][c]
        else:
            return dp[a][b][c]
        

ROW = 21
dp = [[[0] * ROW for _ in range(ROW)] for _ in range(ROW)]

while True:
    a, b, c = map(int, input().split())
    
    if a == b == c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a, b, c)}')
        

# 재귀함수를 DP로 구현