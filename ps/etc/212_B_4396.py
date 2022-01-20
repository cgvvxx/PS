# Baekjoon 4396 - 지뢰 찾기
# Silver 5


def count_bomb(x, y):
    
    checks = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    
    cnt = 0
    for i, j in checks:
        
        if i < 0 or i >= n or j < 0 or j >= n:
            continue
        
        if closed_map[i][j] == '*':
            cnt += 1
    
    return cnt
    

def show_map():
    
    is_break = False
    my_map = [['.']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            
            if open_map[i][j] == 'x':
                my_map[i][j] = str(count_bomb(i, j))
                
                if closed_map[i][j] == '*':
                    is_break = True
                    
    if is_break:
        for i in range(n):
            for j in range(n):
                if closed_map[i][j] == '*':
                    my_map[i][j] = '*'
                    
                    
    for arr in my_map:
        print(''.join(arr))


n = int(input())
closed_map = [list(input()) for _ in range(n)]
open_map = [list(input()) for _ in range(n)]

show_map()
    

# 어렵지 않은 구현