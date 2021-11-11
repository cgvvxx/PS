# Baekjoon 1759 - 암호 만들기
# Gold 5
# 완전탐색 - 백트래킹


def is_valid(l):
    
    v = 0
    c = 0
    for s in l:
        if s in ['a', 'e', 'i', 'o', 'u']:
            v += 1
        else:
            c += 1
    
    if c >= 2 and v >= 1:
        return True
    else:
        return False
    
def dfs(l):
    
    if len(l) == n:
        if is_valid(l):
            print(''.join(l))
            return
        
    for i in chars:
        
        if not l or l[-1] < i:
            l.append(i)
            dfs(l)
            l.pop()
            
            
n, m = map(int, input().split())
chars = list(input().split())
chars.sort()
dfs([])


# 백트래킹 or itertools의 combination 활용
# sort 후 백트래킹
# 모음이 최소 한 개, 자음이 최소 두 개 포함되어야 하는 조건 체크