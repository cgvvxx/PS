# solved: [10819] 차이를 최대로
# https://www.acmicpc.net/problem/10819
# bruteforcing, combinatoric
# 
# Silver 2
# n이 최대 8이므로, 8!=40000번의 경우의 수만 따지면 충분함
# permutaions를 이용하여 모든 경우에 대하여 계산하여 최댓값 return

from itertools import permutations

def calculate(arr):
    
    ans = 0
    for i in range(len(arr)-1):
        ans += abs(arr[i+1]-arr[i])
    return ans


n = int(input())
arr = list(map(int, input().split()))

ans = 0
for perm in permutations(arr, n):
    ans = max(ans, calculate(perm))
print(ans)
