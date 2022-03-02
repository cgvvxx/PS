# Baekjoon 9466 - 텀 프로젝트
# Gold 3
# BFS/DFS


import sys
input = sys.stdin.readline


def get_students(n):
    
    def dfs(n, route):
        
        visited[n] = True
        
        while True:
            
            c = arr[n]
            if visited[c]: break
            n = c
            route.append(n)
            visited[n] = True
        
        return len(route[route.index(c):]) if route and c in route else 0
        
    visited = [False] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            ans += dfs(i, [i])
    print(n - ans)


for _ in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    get_students(n)


# 재귀로 하니 계속 메모리 초과가 나서 stack으로 바꿈
# >> 각 노드의 값이 하나 밖에 없어서 굳이 재귀를 쓸 필요가 전혀 없기도 할 듯
# route에 현재 거쳐간 노드들을 저장해 놓고 while문 반복이 끝났을 때
# 순환하는 구조가 존재하는 경우 ans에 그 값을 저장
# 시간 제한도 까다로우므로 방분하는 노드들은 꼭 visited에 방문 체크 해야함