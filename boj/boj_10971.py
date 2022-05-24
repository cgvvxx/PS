# solved: [10971] 외판원 순회 2
# https://www.acmicpc.net/problem/10971
# bruteforcing, combinatorics
#
# Silver 2
# 외판원 순회 문제 - n이 10이므로 DP말고 완전탐색으로 풀어봄
# 도시 사이의 경로가 존재하지 않는 경우(graph[i][j]=0)가 존재하므로, is_possible라는 변수를 활용 graph[i][j]=0인 경우 해당 경로 탐색을 종료
# 경로를 탐색하면서 현재 경로의 비용(check)이 이전 최소 비용(ans)보다 큰 경우 경로 탐색을 종료

from itertools import permutations

n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

ans = 10**10
for perm in permutations(range(n)):
    
    is_possible = True
    check = 0
    
    for i in range(n):
        cost = graphs[perm[i-1]][perm[i]]
        if cost and check < ans:
            check += cost
        else:
            is_possible = False
            break
            
    if is_possible:
        ans = min(ans, check)
        
print(ans)
