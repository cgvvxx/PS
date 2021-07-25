# Programmers - 보석 쇼핑
# Level 3
# etc - 투포인터

def solution(gems):
    set_gems = set(gems)
    len_gems = len(gems)
    len_set_gems = len(set_gems)
    i, j = 0, len_set_gems  # 투포인터 i, j
    ans = (-1, -1)

    check_gems = dict(zip(list(set_gems), [0] * len_set_gems))  # dict 형태로 i번째와 j번째 사이에 있는 list를 check
    for gem in gems[i:j]:
        check_gems[gem] += 1

    while True:
        if all(check_gems.values()):  # 모든 gem이 적어도 한 개 이상 있는 경우
            if ans[0] == -1:
                ans = (i, j)
            else:
                if ans[1] - ans[0] > j - i:  # 원래 값보다 작으면 ans에 assign
                    ans = (i, j)
            check_gems[gems[i]] -= 1
            i += 1
        else:
            if j == len_gems:
                return [ans[0] + 1, ans[1]]
            check_gems[gems[j]] += 1
            j += 1