# solved: [92334] 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334
# implementation
#
# Level 1
# rep_dict는 key는 유저 ID, value는 유저가 신고한 ID의 set
# count_dict는 key는 신고당한 유저 ID, value는 신고 횟수
# count_dict에서 value가 k이상인 key값을 reported에, rep_dict의 value와 reported의 교집합의 갯수가 answer

from collections import defaultdict


def solution(id_list, report, k):
    
    rep_dict = defaultdict(set)
    count_dict = defaultdict(int)

    for rep in report:
        a, b = rep.split()
        if b in rep_dict[a]:
            continue
        rep_dict[a].add(b)
        count_dict[b] += 1
    
    reported = set(x for x in count_dict if count_dict[x] >= k)
    
    answer = []
    for _id in id_list:
        answer.append(len(reported & rep_dict[_id]))
        
    return answer
