# solved: [92343] 양과 늑대
# https://programmers.co.kr/learn/courses/30/lessons/92343
# bruteforcing, dfs, graph-traversal, tree
#
# Level 3
# 트리에서 양이 늑대보다 항상 크게 탐색하면서, 최대 양의 개수를 구하는 문제
# 이전 노드의 순서에 상관없이, 다음 노드는 이전 노드들의 자식 노드들이 됨을 주의
# n=17 이므로 dfs를 통해 방문할 수 있는 모든 경우(양의 개수 >= 늑대의 개수)일 때를 완전 탐색

def solution(info, edges):
    
    global ans
    
    def dfs(cur, wolf, sheep, visited):
    
        global ans

        if info[cur] == 1:
            wolf += 1
        else:
            sheep += 1

        if wolf >= sheep:
            return

        ans = max(ans, sheep)
        
        nxts = set()
        for i in visited:
            nxts.update(set(graphs[i]))
        nxts -= visited        

        for nxt in nxts:
            dfs(nxt, wolf, sheep, visited | {nxt})
            
        return
    
        
    ans = 0
    n = len(info)
    graphs = [[] for _ in range(n+1)]
    for p, c in edges:
        graphs[p].append(c)
    
    dfs(0, 0, 0, {0})
     
    return ans
