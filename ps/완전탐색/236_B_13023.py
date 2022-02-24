# Baekjoon 13023 - ABCDE
# Gold 5
# 완전탐색 - 백트래킹


from collections import defaultdict


def dfs(n, l, d):
    
    global flag
    
    if flag:
        return
    
    if d == 5:
        if len(set(l)) == 5:
            flag = True
        return
    
    for i in relations[n]:
        if i in l:
            continue
        dfs(i, l+[i], d+1)


n, m = map(int, input().split())
relations = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)
    
flag = False
for i in range(n):
    dfs(i, [i], 1)

if flag:
    print(1)
else:
    print(0)


# 백트래킹
# n, l, d = 현재 체크하는 숫자, 지금까지 체크한 숫자 리스트, 깊이
# 깊이 d가 5인 경우까지만 체크하고 이 때 l의 서로 다른 원소의 개수가 5면 문제의 조건 만족
# 아닌 경우 돌아가서 다시 백트래킹