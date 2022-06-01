# solved: [1946] 신입 사원
# https://www.acmicpc.net/problem/1946
# greedy, sorting
# 
# Silver 1
# 먼저 서류 성적 순으로 sort한 이후, 면접 성적이 앞의 최고 면접 성적보다 큰 경우만 count

import sys
input = sys.stdin.readline

for _ in range(int(input())):

    n = int(input())
    scores = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        scores.append((a, b))
        
    scores.sort()

    cut = scores[0][1]
    ans = 1
    for a, b in scores[1:]:
        if cut > b:
            ans += 1
            cut = b

    print(ans)    
