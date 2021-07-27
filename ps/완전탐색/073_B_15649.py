# Baekjoon 15649~15652 - N과 M (1) ~ (4)
# Silver 3
# 완전탐색 - 백트래킹

# 15649
n, m = map(int, input().split())

l = []
def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, n+1):
        if i in l:
            continue
        l.append(i)
        dfs()
        l.pop()

dfs()


# 15650
n, m = map(int, input().split())

l = []
def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    start = l[-1] if l else 1
    
    for i in range(start, n+1):
        if i in l:
            continue
        l.append(i)
        dfs()
        l.pop()

dfs()


# 15651
n, m = map(int, input().split())

l = []
def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    for i in range(1, n+1):
        l.append(i)
        dfs()
        l.pop()

dfs()


# 15652
n, m = map(int, input().split())

l = []
def dfs():
    if len(l) == m:
        print(' '.join(map(str, l)))
        return
    
    start = l[-1] if l else 1
    
    for i in range(start, n+1):
        l.append(i)
        dfs()
        l.pop()

dfs()