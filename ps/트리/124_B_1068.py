# Baekjoon 1068 - 트리
# Gold 5
# 그래프 - 트리


def dfs(node):
    
    not_tree[node] = True
    stack = [node]
    visited[node] = True
    
    while stack:
        
        v = stack.pop()
        
        for i in trees[v]:
            if not visited[i]:
                visited[i] = True
                not_tree[i] = True
                stack.append(i)


n = int(input())
parents = list(map(int, input().split()))
trees = [[] for _ in range(n)]

for idx, p in enumerate(parents):
    if p == -1:
        continue
    trees[p].append(idx)
    
visited = [False] * n
not_tree = [False] * n

dfs(int(input()))

count = 0
for idx in range(n):
    if not not_tree[idx]:
        for j in trees[idx][::-1]:
            if not_tree[j]:
                trees[idx].pop()
                
        if not trees[idx]:
            count += 1
        
print(count)


# 잘라낸 node부터 dfs를 시작하여 not_tree에 True로 체크
# not_tree가 아닌 node이면서 node의 자식 노드가 없으면 count += 1
# 틀렸던 반례 1)
# 0번째 노드가 루트 노드라고 생각하고 처음에 코드를 짜서 틀림, 아래 입력 참고
# 5
# 1 2 3 4 -1
# 4
# 틀렸던 반례 2)
# 자식 노드가 없는 걸 counting 할 때 trees의 원소가 []만 카운팅함, 노드가 잘릴 때도 자식 노드가 없어질 수 있음
# 4
# -1 0 1 2
# 2