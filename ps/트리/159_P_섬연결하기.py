# Programmers - 섬 연결하기
# Level 3
# Tree - MST


def solution(n, costs):
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
            
            
    costs.sort(key=lambda x:x[2])
    answer = 0
    parent = list(range(n))
    
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost
    
    return answer


# 기본적인 MST 유형의 문제랑 똑같음
# 기존에 활용했던 kruskal 코드 재활용