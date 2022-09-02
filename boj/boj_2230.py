# solved: [2230] 수 고르기
# https://www.acmicpc.net/problem/2230
# two-pointer
# 
# Gold 5
# 주어진 숫자 리스트를 정렬한 후, 투 포인터를 통해 앞에서 부터
# 두 수의 차이가 m보다 크면 i += 1, 아니면 j += 1 하면서 전진해나가면서
# i번째 수와 j번째 수의 최솟값을 체크

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()

i, j = 0, 1
diff = 10**10

while True:
    
    if nums[j] - nums[i] <= m:
        j += 1
    else:
        i += 1
        
    if j >= n:
        break
        
    if m <= nums[j] - nums[i] < diff:
        diff = nums[j] - nums[i]
        
print(diff)
