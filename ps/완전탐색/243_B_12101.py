# Baekjoon 12101 - 1, 2, 3 더하기 2
# Silver 1
# 완전탐색 - 백트래킹


def dfs(l, s):
    
    if s >= n:
        if sum(l) == n:
            ans.append(l)
        return
    
    for i in nums:
        dfs(l+[i], s+i)


n, k = map(int, input().split())
nums = [1, 2, 3]

ans = []
dfs([], 0)
print(*ans[k-1], sep='+') if len(ans) >= k else print(-1)   


# 기본적인 백트래킹