# solved: [6443] 애너그램
# https://www.acmicpc.net/problem/6443
# backtracking, combinatorics, dfs
# 
# Gold 5
# 중복을 허용하여 전체 경우의 수 나열하기 > 단순히 itertools 모듈을 쓰면 간단히 해결할 수 있는 문제
# 백트래킹 연습으로 해당 모듈 안쓰고 해결 
# checked라는 set에 모든 중간과정(temp)를 저장하여 checked에 있는지 없는지 체크하면서 백트래킹

def dfs(l, visited, n):
    
    if len(l) == n:
        print(l)
        return
    
    for j in range(n):
        if visited & (1 << j):
            continue

        temp = l + words[j]
        if temp not in checked:
            checked.add(temp)
            dfs(temp, visited | (1 << j), n)

    
for _ in range(int(input())):
    words = sorted(list(input().strip()))
    checked = set()
    dfs('', 0, len(words))
