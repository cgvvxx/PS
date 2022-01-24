# Baekjoon 17626 - Four Squares
# Silver 4
# DP


def is_square(n): 
    
    return int(n ** 0.5) ** 2 == n


def get_dp(n):

    if dp[n] != 5:
        return
        
    if is_square(n):
        dp[n] = 1
        return
    else:
        
        cnt = 5
        for root in range(int(n**0.5), 0, -1):
            
            root **= 2
            
            if dp[n-root] == 5:
                get_dp(n-root)
                
            cnt = min(cnt, 1+dp[n-root])
            
            if cnt == 2:
                dp[n] = cnt
                return
                
        dp[n] = cnt

        
n = int(input())
dp = [5] * (n+1)
dp[0] = 0

get_dp(n)
print(dp[n])


# n의 제곱근보다 작은 i에 대하여 dp[n] = min(dp[i**2]+dp[n-i**2])