# Baekjoon 2800 - 괄호 제거
# Gold 5
# 스택/큐

from itertools import product

exp = list(input())
n = exp.count('(')

result = []
for prod in product(*[(0, 1) for _ in range(n)]):
        
    ans = ''
    open_count = 0
    is_open = []
    
    if all(prod):
        continue
    
    for char in exp:
        if char == '(':
            if prod[open_count] == 0:
                is_open.append(False)
            else:
                ans += char
                is_open.append(True)
            open_count += 1
        elif char == ')':
            if is_open and is_open.pop():
                ans += char
            else:
                pass
        else:
            ans += char
    
    result.append(ans)

result = list(set(result))
result.sort()
for res in result:
    print(res)