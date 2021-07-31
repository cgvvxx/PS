# Programmers - 불량 사용자
# Level 3
# 완전탐색 - 백트래킹

from collections import Counter

def solution(user_id, banned_id):

    def compare_id(user, ban):

        if len(user) != len(ban):
            return False

        for idx in range(len(user)):
            if ban[idx] == '*':
                continue
            else:
                if ban[idx] != user[idx]:
                    return False

        return True


    def match_id(ban):

        match_list = []
        for user in user_id:
            if compare_id(user, ban):
                match_list.append(user)

        return match_list


    def make_dict(banned_id):

        ban_match = list()
        
        for ban in banned_id:
            mat_list = match_id(ban)
            if mat_list:
                ban_match.append(mat_list)
                    
        return ban_match

    
    def backtrack(idx, ans_li):

        if len(ans_li) == len(match_li):
            print(ans_li)
            ans_set.append(set(ans_li))
            return

        for j in range(len(match_li[idx])):
            if match_li[idx][j] in ans_li:
                continue
            ans_li.append(match_li[idx][j])
            backtrack(idx+1, ans_li)
            ans_li.pop()

            
    ans_set = list()
    match_li = make_dict(banned_id)
    ans_li = []
    backtrack(0, [])
    
    prod = list()
    for i in ans_set:
        if i not in prod:
            prod.append(i)
            
    return len(prod)