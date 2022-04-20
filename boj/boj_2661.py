# solved: [2661] 좋은수열
# https://www.acmicpc.net/problem/2661
# backtracking, dfs
# 
# Gold 4
# promising한 조건은 해당 단어를 거꾸로 뒤집어 앞글자 부터 1, 2, 3, ... 이 겹치는지 확인
# is_promising 함수를 활용하여 가지치기를 통해 백트래킹

def is_promising(cur):
    
    cur = cur[::-1]
    i = 1
    
    while 2*i <= len(cur):
        
        if cur[:i] == cur[i:2*i]:
            return False        
        
        i += 1
        
    return True

def dfs(cur):
    
    global flag
    
    if len(cur) == tar:
        print(cur)
        flag = True
        return
    
    for n in range(1, 4):
        
        if is_promising(cur + str(n)):
            dfs(cur + str(n))
        
        if flag:
            return


tar = int(input())
flag = False
dfs('')
