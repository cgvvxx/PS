# Baekjoon 2668 - 숫자고르기
# Gold 5
# BFS/DFS


def dfs(n, visited):
    
    global ans
    
    visited.append(n)
    
    if arr[n] in set(visited):
        if visited[0] == arr[n]:
            ans |= set(visited)
        return
    
    dfs(arr[n], visited)


n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

ans = set()
for i in range(1, n+1):
    if i not in ans:
        dfs(i, [])

print(len(ans))
for i in sorted(list(ans)):
    print(i)


# 현재 n과 지금까지 체크한 숫자의 리스트인 visited를 인수로 dfs 반복
# visited에 arr[n]이 있는 경우 return
# 이 때 visted[0] == arr[n] 인 경우, 즉 순환하는 구조가 존재하는 경우 ans에 visited를 추가
# ans의 원소를 크기 순으로 print