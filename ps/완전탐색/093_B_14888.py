# Baekjoon 14888 - 연산자 끼워넣기
# Silver 1
# 완전탐색 - 백트래킹

#1. permuation을 이용한 완전탐색

from itertools import permutations

def calculate(arr, perm):
    
    ans = arr[0]
    operation_dict = {'0':'+', '1':'-', '2':'*', '3':'//'}
    
    for n, o in zip(arr[1:], perm):
        if ans < 0 and o =='3':
            ans = -eval(str(-ans)+operation_dict[o]+str(n))
        else:
            ans = eval(str(ans)+operation_dict[o]+str(n))
    
    return ans

n = int(input())
arr = list(map(int, input().split()))
operations = list(map(int, input().split()))

base_perm = ''
for idx, num in enumerate(operations):
    base_perm += str(idx) * num

min_ans, max_ans = 10**9, -10**9
for perm in set(permutations(base_perm, len(base_perm))):
    
    ans = calculate(arr, perm)
    if ans < min_ans:
        min_ans = ans
    
    if ans > max_ans:
        max_ans = ans

print(max_ans)
print(min_ans)


#2. 재귀함수 + 백트래킹 

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -1e9
min_result = 1e9

def dfs(x, now):
    global add, sub, mul, div, max_result, min_result
    if n == x:
        max_result = max(max_result, now)
        min_result = min(min_result, now)
    else:
        if add > 0:
            add -= 1
            dfs(x+1, now + data[x])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(x+1, now - data[x])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(x+1, now * data[x])
            mul += 1
        if div > 0:
            div -= 1
            dfs(x+1, int(now / data[x]))
            div += 1

dfs(1, data[0])
print(max_result)
print(min_result)