# Baekjoon 16508 - 전공책
# Silver 3
# 완전탐색


from itertools import combinations
from collections import Counter

t = input()
n = int(input())

costs = []
books = []
for _ in range(n):
    c, w = input().split()
    costs.append(int(c))
    books.append(w)
    
ans = 10**8
for i in range(1, n+1):
    for comb in combinations(range(n), i):
        check_name = ''
        check_cost = 0
        for idx in comb:
            check_cost += costs[idx]
            check_name += books[idx]
            
        c = Counter(check_name)
        d = Counter(t)
        c.subtract(d)
        check = all(map(lambda x: True if x>=0 else False, c.values()))

        if check and check_cost < ans:
            ans = check_cost
            
if ans == 10**8:
    print(-1)
else:
    print(ans)


# 책을 선택하는 모든 경우의 수 (최대 2**16가지 경우의 수)를 살펴본 후 가장 적은 가격 print

# 처음에 단순히 set으로 합집합 + 부분집합으로 풀려고 했다가 틀림
# 이 때 책에 포함되는 글자의 개수도 카운트 해야함

# ex. 반례
# AAA
# 1
# 5 A
# >> -1
# 주어진 책 하나로는 A 하나 밖에 가질 수 없음