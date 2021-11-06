# Programmers - 스킬트리
# Level 2


def solution(skill, skill_trees):
    
    skill_set = set(skill)
    ans = 0
    
    for skills in skill_trees:
        idx = -1
        for s in skills:

            if s in skill_set:
                this_idx = skill.find(s)
                if this_idx == idx + 1:
                    idx = this_idx
                else:
                    break
        else:
            ans += 1
            
    return ans


# 주어진 skill 순서에 대해서 순서가 맞는지 확인하는 문제
# 특별한 알고리즘을 사용하지 않고 단순히 skill에 들어간 문자에 대해서만 순서를 체크해줌