# solved: [72412] 순위 검색
# https://programmers.co.kr/learn/courses/30/lessons/72412
# bruteforcing, binary-search
#
# Level 2
# 지원자의 종류는 총 3*2*2*2 = 24 가지 그룹에 대해서 dictionary에 해당 지원자의 점수를 기록한 뒤
# 해당 지원자가 속하는 그룹('-'이면 모두 매칭)의 점수들에 대해 이분 탐색을 통해 해당 점수보다 큰 지원자의 수를 count

from collections import defaultdict
from bisect import bisect_left

def is_equal(a, b):
    
    for i in range(len(a)):
        if a[i] != b[i] and a[i] != '-':
            return False
        
    return True

def solution(info, query):
    
    position = defaultdict(list)
    
    for i in info:
        l, p, c, f, s = i.split()
        position[l[0]+p[0]+c[0]+f[0]].append(int(s))
        
    for p in position:
        position[p].sort()
    
    ans = []
    for q in query:
        
        cnt = 0
        l, p, c, fs = q.split(" and ")
        f, s = fs.split()
        chk = l[0]+p[0]+c[0]+f[0]
        
        for p in position:
            if is_equal(chk, p):
                cnt += len(position[p]) - bisect_left(position[p], int(s))
        
        ans.append(cnt)
    
    return ans
