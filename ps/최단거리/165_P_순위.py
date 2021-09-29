# Programmers - 순위
# Level 3
# 최단 거리 - 플로이드 워셜


from collections import defaultdict

def solution(n, results):

    win = defaultdict(set)
    lose = defaultdict(set)
    
    for x, y in results:
        win[x].add(y)
        lose[y].add(x)
        
    for i in range(1, n+1):
        for w in win[i]:
            lose[w].update(lose[i])
        for l in lose[i]:
            win[l].update(win[i])
            
    answer = 0
    for i in range(1, n+1):
        if len(win[i]|lose[i]) == n-1:
            answer += 1    
    return answer


# 주어진 방향 그래프에서 나보다 위에 있는 노드의 개수 + 아래에 있는 노드의 개수 == n-1 일때 승패를 알 수 있음
# dictionary 그래프를 표현하고 나보다 이긴 사람과 진 사람의 dictionary 정의
# 이 dictionary를 업데이트 하면서 나보다 이긴 사람의 수와 진 사람의 수의 합을 체크
# 일반적으로는 플로이드-워셜써서 모든 노드에 대한 승패 기록을 체크 하는듯