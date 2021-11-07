# Programmers - 뉴스 클러스터링
# Level 2


from collections import Counter

def make_set(s):
    
    s_set = list()
    
    for i in range(len(s)-1):
        check = s[i:i+2]
        if check.isalpha():
            s_set.append(check.lower())
            
    return Counter(s_set)


def cal_jaccard(c1, c2):
    
    s1 = set(c1.keys())
    s2 = set(c2.keys())
    i = s1 & s2
    u = s1 | s2
    
    i_num, u_num = 0, 0
    for e1 in i:
        i_num += min(c1[e1], c2[e1])
        
    for e2 in u:
        u_num += max(c1[e2], c2[e2])
    
    if u_num == 0:
        return 65536
    else:
        return int(i_num/u_num*65536)
    
    
def solution(str1, str2):
    
    return cal_jaccard(make_set(str1), make_set(str2))


# 다중 집합(원소의 개수가 중복되는 집합)의 교집합, 합집합을 구현하는 부분이 특이한 문제
# 이는 Counter를 통해 각 집합의 원소의 개수를 구하고 교집합과 합집합에서의 원소의 개수를 다시 계산하여 구함