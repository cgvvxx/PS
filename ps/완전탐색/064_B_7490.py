# Baekjoon 7490 - 0 만들기
# Gold 5
# 완전탐색

from itertools import product

def eval_cals(n, prod):
    
    cal_dict = {0:'+', 1:'-', 2:''}
    print_cal_dict = {0:'+', 1:'-', 2:' '}
    
    cals = list(map(lambda x:cal_dict[x], prod))
    print_cals = list(map(lambda x:print_cal_dict[x], prod))
    
    ans = []
    print_ans = []
    for i in range(len(cals)):
        ans.append(f'{i+1}')
        ans.append(cals[i])
        print_ans.append(f'{i+1}')
        print_ans.append(print_cals[i])
    ans.append(f'{n}')
    print_ans.append(f'{n}')
    string = ''.join(ans)
    print_string = ''.join(print_ans)
    
    return string, print_string

def print_n(n):
    eval_lists = []
    for prod in product([0, 1, 2], repeat=n-1):
        s, print_s = eval_cals(n, prod)
        if eval(s) == 0:
            eval_lists.append(print_s)
            
    eval_lists.sort()
    for evals in eval_lists:
        print(evals)

n = int(input())
ns = []
for _ in range(n):
    ns.append(int(input()))

for i in ns:
    print_n(i)
    print('')