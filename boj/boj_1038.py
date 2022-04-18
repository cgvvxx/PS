# solved: [1038] 감소하는 수
# https://www.acmicpc.net/problem/1038
# backtracking, combinatorics, dfs
# 
# Gold 5
# 0 ~ 9까지 combinations을 이용하여 감소하는 케이스를 모두 구하고 하나씩 체크하면서 단순히 count

from itertools import combinations

def get_nth(n):
    
    temp_cnt = 0
    flag = False
    temp = list()
    for i in range(1, 11):
        for comb in combinations(range(10), i):
            temp.append(int(''.join(map(str, sorted(list(comb), reverse=True)))))
            temp_cnt += 1
            if temp_cnt > n:
                flag = True
        
        if flag:
            break
    
    temp.sort()
    if n >= len(temp):
        print(-1)
    else:
        print(temp[n])
            
get_nth(int(input()))
