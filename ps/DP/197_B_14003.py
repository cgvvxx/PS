# Baekjoon 14003 - 가장 긴 증가하는 부분 수열 5
# Platinum 5
# DP


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
    
check = max(dp)
ans = []
for j in range(len(dp)-1, 0, -1):
    if dp[j] == check:
        check -= 1
        ans.append(arr[j])
        
print(len(ans))
print(*ans[::-1])


# 단순히 LIS의 길이가 아닌 실제 LIS의 배열을 출력하는 문제
# 앞에서 구한 dp를 이용해 dp의 마지막 배열부터 거꾸로 탐색하여
# dp의 최댓값에서 시작하여 1씩 줄여가면서 주어진 값의 인덱스에 해당하는 배열의 값을 ans에 append
# 다시 ans의 역순으로 프린트하면 실제 LIS의 배열이 출력