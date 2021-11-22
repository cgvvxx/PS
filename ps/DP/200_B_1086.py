# Baekjoon 1086 - 박성원
# Platinum 5
# DP


from math import gcd

n = int(input())
nums = [int(input()) for _ in range(n)]
k = int(input())

rs = [num % k for num in nums]
tens = [10**len(str(num)) % k for num in nums]

dp = [[0] * k for _ in range(1<<n)]
dp[0][0] = 1

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            continue
            
        for r in range(k):
            dp[i|1<<j][(r*tens[j]+rs[j]) % k] += dp[i][r]
            
p = dp[(1<<n)-1][0]
q = sum(dp[(1<<n)-1])
g = gcd(p, q)
print(f'{p//g}/{q//g}')


# 비트마스크를 이용한 DP 문제
# 완전탐색의 경우 O(N!)으로 무조건 시간초과
# dp 테이블을 2**N X K로 만들어 놓은 후 dp[i(bit)][j] : i 집합으로 생성하는 수를 k로 나눈 나머지가 j인 수의 개수
# dp[i|1<<j][(r*tens[j]+rs[j]) % k] += dp[i][r]에서
#
# 1. dp[i | 1 << j] : i 번째 집합에 j번째 수를 넣는 경우 
# 예를 들어 11의 경우 10 | 1, 01 | 10으로 두 가지 경우가 나올 수 있음
# 각 수의 조합을 k로 나눈 나머지를 생각하므로 j번째 수는 마지막에 이어 붙인다라고 생각해도 무방함
#
# 2. r * tens[j] + rs[j] : tens[j]는 j번째 수의 자릿 수를 k로 나눈 나머지, rs[j]는 j번째 수를 k로 나눈 나머지
#
# 3. += dp[i][r] : 각 케이스에 대해서 dp[i][r]을 계속 더해줌
#
# 4. 최종적으로 p는 dp[(1<<n)-1][0] (모든 수를 사용해서 만든 수 중 k로 나눈 나머지가 0인 수의 개수), q는 sum(dp[(1<<n)-1])