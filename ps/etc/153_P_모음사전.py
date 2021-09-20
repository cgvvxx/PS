# Programmers - 모음사전
# Level 2


from itertools import product


def join_except_space(li):
    
    ans = ''
    for i in li:
        if i != ' ':
            ans += i
            
    return ans


def solution(word):
    
    word_list = sorted(list(set(map(lambda x:join_except_space(x), product('AEIOU ', repeat=5)))))
    
    return word_list.index(word)


# 전체 케이스가 약 4000개 내외로 크지 않기 때문에 product 이용해서 모든 케이스 리스트 생성
# 이 후 주어진 word의 index 리턴