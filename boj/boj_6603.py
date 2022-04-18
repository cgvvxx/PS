# solved: [6603] 로또
# https://www.acmicpc.net/problem/6603
# backtracking, combinatorics
# 
# Silver 2
# 단순히 combinations 내장함수를 활용하여 해결

from itertools import combinations

def get_lotto(n, lotto):
    
    for perm in combinations(range(n), 6):
        print(*map(lambda x:lotto[x], perm))
    print('')

while True:
    
    n, *lotto = map(int, input().split())
    lotto.sort()
    get_lotto(n, lotto)
    
    if not n:
        break
