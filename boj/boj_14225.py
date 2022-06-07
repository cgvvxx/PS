# solved: [14225] 부분수열의 합
# https://www.acmicpc.net/problem/14225
# bruteforcing, combinatoric
# 
# Silver 1
# itertools의 combinations를 이용하여 모든 부분수열의 경우의 sum을 구하고
# visited에 체크, visited 리스트에서 최초로 False가 나오는 index를 return

from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

visited = [False] * 2000001
visited[0] = True
for i in range(1, n+1):
    for comb in combinations(arr, i):
        visited[sum(comb)] = True
        
print(visited.index(False))
