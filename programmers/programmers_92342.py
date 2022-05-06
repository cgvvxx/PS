# solved: [92342] 양궁대회
# https://programmers.co.kr/learn/courses/30/lessons/92342
# bruteforcing
#
# Level 2
# 결국 라이언이 가장 큰 점수차로 이기기 위해 완전탐색을 통해 케이스를 열심히 나누었음..
# 여러 가지 반례들을 생각하는게 쉽지 않음

def solution(n, info):
    
    info = info[::-1]
    info_idx, not_info_idx = [], []
    
    for idx in range(11):
        if info[idx] > 0:
            info_idx.append(idx)
        else:
            not_info_idx.append(idx)

    info_tar = list(map(lambda x:info[x], info_idx))

    m = len(info_idx)
    answer = [-1]
    score_diff = -1
    for i in range(1 << m):
        total = n
        l_info = []
        a_score, l_score = 0, 0

        for j in range(m):
            if i & (1 << j):
                l_info.append(0)
                a_score += info_idx[j]
            else:
                l_info.append(info_tar[j]+1)
                total -= info_tar[j]+1
                l_score += info_idx[j]
                if total < 0:
                    break

        left_score = a_score - l_score

        if total == 0 and left_score < 0:
            if -left_score > score_diff:
                score_diff = -left_score
                this_ans = [0] * 11
                for k in range(m):
                    this_ans[info_idx[k]] = l_info[k]
                answer = this_ans
                
        elif total > 0:
            if left_score < sum(not_info_idx[-total:]):
                
                this_ans = [0] * 11
                for k in range(m):
                    this_ans[info_idx[k]] = l_info[k]
                for k in not_info_idx[::-1]:
                    this_ans[k] = 1
                    total -= 1
                    l_score += k
                    if total <= 0:
                        break

                for i in range(11):
                    if i in info_idx:
                        if info[i] > 1:
                            this_ans[i] += min(info[i] - 1, total)
                            total -= min(info[i]-1, total)
                            if total <= 0:
                                break                    
                    else:
                        this_ans[not_info_idx[0]] += total
                        break

                if l_score - a_score >= score_diff:
                    answer = this_ans
                    score_diff = l_score - a_score

    return answer[::-1]
