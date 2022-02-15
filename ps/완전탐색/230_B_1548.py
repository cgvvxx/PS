# Baekjoon 1548 - 부분 삼각 수열
# Silver 1
# 완전탐색


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


# 숫자들을 크기 순대로 정렬 후
# 가장 작은 두 수의 합보다 작은 숫자 까지 숫자들을 check 리스트에 append
# check 리스트의 길이의 최댓값을 return