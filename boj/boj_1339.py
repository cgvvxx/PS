# solved: [1339] 단어 수학
# https://www.acmicpc.net/problem/1339
# greedy
# 
# Gold 4
# 가장 긴 문자열을 기준으로 가장 앞에 나온 문자일수록 큰 수가 들어가야함
# 가장 먼저 나온 문자 순으로 우선순위를 만들고(priority) 그리디하게 우선순위가 높은 순서대로
# 해당 문자에 가장 큰 수(9)부터 순서대로 대응시킴

from collections import defaultdict

def match(alpha):
    
    n = ''
    for a in alpha:
        n += str(match_dict[a])
    
    return int(n)
   

alphas = [input() for _ in range(int(input()))]

priority = defaultdict(int)
alphas.sort(key=lambda x:len(x), reverse=True)

for alpha in alphas:
    for i, a in enumerate(alpha):
        priority[a] += 10 ** (len(alpha) - i)

match_dict = dict()
sorted_priority = sorted(list(priority.items()), key=lambda x:x[1], reverse=True)
num = 9
for (a, p) in sorted_priority:
    match_dict[a] = num
    num -= 1

print(sum(map(match, alphas)))  
