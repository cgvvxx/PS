# Programmers - 단어변환
# Level 3
# DFS/BFS

from collections import deque


def compare_word(w1, w2):
    # 두 단어 w1, w2가 한 글자만 다를 때 True, 아니면 False를 반환

    count = 0

    if w1 == w2:
        return False

    for idx in range(len(w1)):
        if w1[idx] != w2[idx]:
            count += 1
        if count > 1:
            return False

    return True


def graph_dict(words):
    # words 리스트에 있는 단어들의 index를 node로 compare_word가 True인 graph 리턴
    # graph는 dictionary 클래스

    linked_dict = {}
    for i in range(len(words)):
        linked_dict[i] = []

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if compare_word(words[i], words[j]):
                linked_dict[i].append(j)
                linked_dict[j].append(i)

    return linked_dict


def bfs(graph, begin_idx, target_idx):
    # begin_idx(begin word의 인덱스)부터 시작하여 graph에서 BFS로 target까지의 거리 계산
    # target 까지의 경로가 존재하지 않으면 0을 return

    visited = [False] * len(graph)
    queue = deque()
    distance = 1

    if target_idx in graph[begin_idx]:
        return 1

    queue.extend(graph[begin_idx])

    while queue:

        check_list = []
        for _ in range(len(queue)):
            n = queue.popleft()
            check_list.append(n)
            for i in graph[n]:

                if i == target_idx:
                    return distance + 1

                if not visited[i]:
                    queue.append(i)

        for check in check_list:
            visited[check] = True

        distance += 1

    return 0


def solution(begin, target, words):
    # words에 target이 존재하지 않는 경우 에러를 발생시켜 0을 return

    try:
        begin_idx = len(words)
        target_idx = words.index(target)
        words.append(begin)
        linked_dict = graph_dict(words)
        answer = bfs(linked_dict, begin_idx, target_idx)

    except:
        answer = 0

    return answer
