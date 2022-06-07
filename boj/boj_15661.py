# solved: [15661] 링크와 스타트
# https://www.acmicpc.net/problem/15661
# bitmask, bruteforcing
# 
# Silver 1
# n은 최대 20이므로 조를 두개로 나누는 경우는 부분집합의 개수 2**20, 약 100만개의 경우의 수
# 완전탐색을 통해 각각의 경우에 대해여 능력의 합의 차를 구하여 ans를 return
# ans == 0인 경우 무조건 최솟값이므로 바로 break
# combinations을 이용해서 하려고 했으나 계속 시간초과 >> 비트마스크로 수정하여 시간단축

def cal(b):
    
    chk = 0
    for i in range(n):
        if (b & (1 << i)):
            for j in range(n):
                if (b & (1 << j)):
                    chk += ability[i][j]
                    
    return chk


n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * (1<<n + 1)
ans = 100000

for i in range(1, 1<<n):
    
    j = (1<<n)-i-1
    
    if not visited[i]:
    
        start = cal(i)
        link = cal(j)

        visited[i] = True
        visited[j] = True

        ans = min(ans, abs(start-link))
        
        if not ans:
            break
        
print(ans)
