# solved: [13908] 비밀번호
# https://www.acmicpc.net/problem/13908
# backtracking, dfs
# 
# Silver 2
# 완전탐색 시간 초과 > 백트래킹 + pypy로 시간 초과 통과
# 현재 탐색하는 숫자 p에서 더 붙여야 하는 숫자의 개수(n - len(p))가 needed의 숫자보다 작은 경우 return
# m = 0 인 경우, input을 받지 않는 조건 확인할 것

def dfs(p):
    
    global cnt
    
    if n-len(p) < sum(needed):
        return
    
    if len(p) == n:
        if sum(needed) == 0:
            cnt += 1
        return
    
    for i in range(10):
        if needed[i]:
            needed[i] -= 1
            dfs(p+str(i))
            needed[i] += 1
        else:
            dfs(p+str(i))
            
n, m = map(int, input().split())
needed = [0] * 10
if m != 0:
    for i in map(int, input().split()):
        needed[i] += 1
cnt = 0
dfs('')
print(cnt)
