# Programmers - 여행경로
# Level 3
# 완전탐색 - 백트래킹


def solution(tickets):

    tickets.sort()
    
    city_set = set()
    for start, end in tickets:
        city_set.add(start)
        city_set.add(end)
    n = len(city_set)
    
    root = ["ICN"]
    visited = [False] * len(tickets)
    
    def dfs():
    
        if all(visited):
            return root

        for idx, ticket in enumerate(tickets):
            if root[-1] != ticket[0]:
                continue

            if visited[idx]:
                continue

            visited[idx] = True
            root.append(ticket[1])
            answer = dfs()
            if answer:
                return answer
            visited[idx] = False
            root.pop()
    
    answer = dfs()
    return answer
    