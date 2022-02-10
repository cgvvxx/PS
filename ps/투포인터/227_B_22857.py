# Baekjoon 22862 - 가장 긴 짝수 연속한 부분 수열 (large)
# Silver 1
# 투 포인터


n = int(input())
nums = list(map(int, input().split()))
nums.sort()

if len(nums) <= 2:
    print(len(nums))
else:
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            check = [nums[i], nums[j]]
            for k in range(j+1, n):
                if nums[k] >= nums[i] + nums[j]:
                    ans = max(ans, len(check))
                    print(i, j, k, check)
                    break
                else:
                    check.append(nums[k])
            else:
                ans = max(ans, len(check))

    print(ans)


# 투 포인터로 홀수 개수를 체크하면서 전진
# 홀수 개수가 k와 같아 지면서 i, j의 거리가 제일 멀어지는 경우가
# 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이