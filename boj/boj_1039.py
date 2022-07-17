# solved: [1039] 교환
# https://www.acmicpc.net/problem/1039
# dfs, graph-traversal
# 
# Gold 3
# dfs를 통해 k번 자리를 바꾸고, ans에 가장 큰 값을 저장
# 재귀함수를 통해 자리를 바꾼 횟수(d)를 count
# 교환을 할 수 없는 경우 1. 한 자리 숫자인 경우, 2. 두 자리 숫자인데 0을 포함하는 경우 체크

n, k = input().split()
k = int(k)
visited = set()
ans = '0'

def is_valid(nums):
    
    if len(nums) == 1:
        return False
    
    if len(nums) == 2 and '0' in nums:
        return False
    
    return True    
    

def dfs(nums, d):
    
    global ans
    
    if d == 0:
        if ans < ''.join(nums):
            ans = ''.join(nums)
        return
    
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            nums[i], nums[j] = nums[j], nums[i]
            
            check = str(d) + ''.join(nums)
            if check not in visited:
                visited.add(check)
                dfs(nums, d-1)
            
            nums[i], nums[j] = nums[j], nums[i]

if is_valid(list(n)):
    dfs(list(n), k)
    print(ans)
else:
    print(-1)
