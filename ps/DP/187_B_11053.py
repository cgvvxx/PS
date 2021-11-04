# Baekjoon 11053 - 가장 긴 증가하는 부분 수열
# Silver 2
# DP

# 1. 시간 복잡도 ~ O(n^2)
n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))


# 2. 시간 복잡도 ~ O(nlogn)
from bisect import bisect_left

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp_val = [0]
for i in range(1, n+1):
    
    idx = bisect_left(dp_val, arr[i])
    if idx == len(dp_val):
        dp_val.append(arr[i])
    else:
        dp_val[idx] = arr[i]
    dp[i] = idx
    
print(len(dp_val)-1)


# O(n^2)
# 현재 인덱스 i를 기준으로 0 ~ i-1 까지의 가장 긴 증가하는 부분수열의 길이를 저장하는 dp를 생성
# 각 i마다 0 ~ i-1의 dp를 살펴보면서 dp를 업데이트 하기 때문에 시간복잡도 n^2
# O(nlogn)
# 이전의 인덱스를 살펴볼 때 0 ~ i-1 모든 dp를 살펴보지 말고
# 각 증가하는 부분수열의 길이에 해당하는 최대 원소를 저장하는 dp_val 이라는 리스트를 생성
# dp_val은 정렬되어 있으므로 이진탐색을 통해 현재 arr[i] 보다 크지 않은 dp_val이 저장되어 있는 인덱스 idx를 찾고
# 이를 통해 dp를 업데이트