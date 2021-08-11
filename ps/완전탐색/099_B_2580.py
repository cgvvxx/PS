# Baekjoon 2580 - 스도쿠
# Gold 4
# 완전탐색 - 백트래킹


def get_promising_num(i, j):
    
    nums = list(range(10))
    is_num = [True] * 10
    is_num[0] = False
    
    for idx in range(9):
        is_num[sudoku[i][idx]] = False
        is_num[sudoku[idx][j]] = False
        
    idxs = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    x_idx, y_idx = i // 3, j // 3
    
    check = [sudoku[i][j] for i in idxs[x_idx] for j in idxs[y_idx]]
    for num in check:
        if num == 0:
            continue
        else:
            is_num[num] = False
            
    return [nums[idx] for idx in range(10) if is_num[idx]]

end = False
def dfs(k):
    
    global sudoku, end
    
    if end:
        return
        
    if k == len(zero_pos):
        for line in sudoku:
            print(*line)
        end = True
        return
    
    
    else:
        row_idx, col_idx = zero_pos[k]
        promising_num = get_promising_num(row_idx, col_idx)
        for num in promising_num:
            sudoku[row_idx][col_idx] = num
            dfs(k+1)
            sudoku[row_idx][col_idx] = 0

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split())))
            
zero_pos = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j]==0]
dfs(0)