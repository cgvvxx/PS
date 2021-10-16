# Programmers - 프렌즈4블록
# Level 2


def solution(m, n, board):
    
    def is_box(r, c):
        
        check = [board[r][c], board[r][c+1], board[r+1][c], board[r+1][c+1]]
        return [(r, c), (r+1, c), (r, c+1), (r+1, c+1)] if len(set(check)) == 1 and set(check) != {'-'} else []
    
    def get_boxpos():
        
        boxpos = set()
        for r in range(m-1):
            for c in range(n-1):
                box = is_box(r, c)
                if box:
                    boxpos.update(box)
                    
        return boxpos
    
    def empty_board(boxpos):
        
        for i, j in boxpos:
            board[i][j] = '-'
            
    def fill_board():
        
        for c in range(n):
            
            flag = False
            is_empty = []
            fillers = []
            
            for r in range(m-1, -1, -1):
                if not flag and board[r][c] == '-':
                    is_empty.append((r, c))
                    
                if is_empty and board[r][c] != '-':
                    fillers.append((r, c))
                    flag = True                  

            if is_empty:
                f_idx = 0
                er, ec = is_empty[0]
                for cr in range(er, -1, -1):

                    if f_idx >= len(fillers):
                        board[cr][ec] = '-'
                    else:
                        pos_r, pos_c = fillers[f_idx]
                        board[cr][ec] = board[pos_r][pos_c]
                        f_idx += 1
                        
    def count_x():
        
        cnt = 0
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == '-':
                    cnt += 1
        
        return cnt
                
            
    board = [list(line) for line in board]
    
    while True:
        
        boxpos = get_boxpos()
        
        if not boxpos:
            break
            
        empty_board(boxpos)
        fill_board()
        
    answer = count_x()
    return answer


# 어렵지는 않지만 귀찮은 구현 문제
# 문제에 조건에 맞게끔 구현을 잘 하면 되는건데 .... 그래서 다소 지저분하지만 단계별로 나누어서 함수 작성 후 해결함
# 구현 자체에서 어려운 부분은 없는듯