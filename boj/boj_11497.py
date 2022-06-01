# solved: [11497] 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497
# greedy, sorting
# 
# Silver 1
# 통나무를 길이 순으로 정렬 후 두 계단 차이의 통나무 높이 차의 최댓값이 최소 난이도
# 예를 들어 7개의 통나무가 있으면 1 > 3 > 5 > 7 > 6 > 4 > 2 와 같은 방식으로 난이도 배열시 최소 난이도를 가짐

for _ in range(int(input())):

    n = int(input())
    logs = list(map(int, input().split()))
    logs.sort()

    ans = -1

    for i in range(n):
        if i+2 < n:
            ans = max(ans, abs(logs[k]-logs[i]))

    print(ans)     
