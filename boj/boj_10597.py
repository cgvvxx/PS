# solved: [10597] 순열장난
# https://www.acmicpc.net/problem/10597
# backtracking, dfs
# 
# Silver 1
# 앞에서 부터 한글자, 또는 두글자를 체크해나가면서 현재 set(cur)에 있는지 체크하면서 백트래킹

def dfs(cur, line):
    
    global flag
    
    if not line:
        if set(cur) == set(range(1, len(cur)+1)):
            print(*cur)
            flag = True
            return
        else:
            return
    
    check = ''
    for i in range(2):
        
        if len(line) == 1 and i == 1:
            continue
        
        check += line[i]
        i_check = int(check)
        
        if i_check <= 0 or i_check >= 51:
            continue
            
        if i_check in cur:
            continue
        
        dfs(cur + [i_check], line[i+1:])
        
        if flag:
            return 


flag = False
dfs([], input())
