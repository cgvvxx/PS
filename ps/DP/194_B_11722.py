# Baekjoon 11722 - 가장 긴 감소하는 부분 수열
# Silver 2
# DP


from bisect import bisect_left

n = int(input())
arr = [0] + list(map(int, input().split()))[::-1]

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


# baekjoon 11053 참고
# 주어진 수열을 거꾸로 (arr[::-1]) 로 append 하면 결국 가장 긴 증가하는 부분 수열을 찾는 문제와 같아짐