# Baekjoon 1182 - 부분수열의 합
# Silver 2
# 완전탐색 - 백트래킹

N, S = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
def backtrack(idx, total):
    global ans
    
    if idx >= N:
        if total == S:
            ans += 1
        return
        
    backtrack(idx + 1, total + arr[idx])
    backtrack(idx + 1, total)

backtrack(0, 0)
if S == 0:
    print(ans-1)
else:
    print(ans)