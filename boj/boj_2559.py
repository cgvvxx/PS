# solved: [2559] 수열
# https://www.acmicpc.net/problem/2559
# prefix-sum
# 
# Silver 3
# 누적 합 기본 문제

n, k = map(int, input().split())
nums = list(map(int, input().split()))

s = sum(nums[:k])
ans = s
for i in range(k, n):
    s += nums[i] - nums[i-k]
    ans = max(s, ans)
    
print(ans)
