# Programmers - 표 편집
# Level 3


def solution(n, k, cmd):
    
    linked_list = {i:[i-1, i+1] for i in range(n)}
    deleted = []
    for each_cmd in cmd:

        if each_cmd == 'C':

            prv, nxt = linked_list[k]
            deleted.append((k, prv, nxt))

            if prv == -1:
                linked_list[nxt][0] = prv
                k = nxt
            elif nxt == n:
                linked_list[prv][1] = nxt
                k = prv
            else:
                linked_list[prv][1] = nxt
                linked_list[nxt][0] = prv
                k = nxt

        elif each_cmd == 'Z':

            at, at_prv, at_nxt = deleted.pop()

            if at_prv == -1:
                linked_list[at_nxt][0] = at
            elif at_nxt == n:
                linked_list[at_prv][1] = at
            else:
                linked_list[at_prv][1] = at
                linked_list[at_nxt][0] = at

        else:
            a, b = each_cmd.split()
            sign = 1 if a == 'D' else 0
            for _ in range(int(b)):
                k = linked_list[k][sign]

    answer = ['O'] * n
    while deleted:
        at, _, _ = deleted.pop()
        answer[at] = 'X'

    return ''.join(answer)


# 2021 카카오 채용연계형 인턴십 문제
# 실제 시험에서는 효율성테스트를 결국 통과를 못했었다
# Doubly Linked List 이용해서 효율성테스트 통과!!
# 이때 단순히 이 문제의 경우 각 노드의 데이터정보가 필요없으므로 dictionary를 이용해서 이전 노드와 다음 노드의 정보만 저장