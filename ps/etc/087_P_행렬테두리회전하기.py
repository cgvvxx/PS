# Programmers - 행렬 테두리 회전하기
# Level 2

def make_matrix(rows, columns):
    
    matrix = []

    num = 1
    for _ in range(rows):
        row_list = []
        for _ in range(columns):
            row_list.append(num)
            num += 1
        matrix.append(row_list)
        
    return matrix


def rotate_matrix(matrix, query, rows, columns):
    
    temp_num = -1
    min_num = rows * columns + 1
    
    upper_left_row, upper_left_col, bottom_right_row, bottom_right_col = query

    upper_left_row -= 1
    upper_left_col -= 1
    bottom_right_row -= 1
    bottom_right_col -= 1
    
    for idx_1 in range(upper_left_col, bottom_right_col+1):
        this_num = matrix[upper_left_row][idx_1]
        if min_num > this_num:
            min_num = this_num
        if temp_num != -1:
            matrix[upper_left_row][idx_1] = temp_num
        temp_num = this_num

    for idx_2 in range(upper_left_row+1, bottom_right_row+1):
        this_num = matrix[idx_2][bottom_right_col]
        if min_num > this_num:
            min_num = this_num
        if temp_num != -1:
            matrix[idx_2][bottom_right_col] = temp_num
        temp_num = this_num

    for idx_3 in range(bottom_right_col-1, upper_left_col-1, -1):
        this_num = matrix[bottom_right_row][idx_3]
        if min_num > this_num:
            min_num = this_num
        if temp_num != -1:
            matrix[bottom_right_row][idx_3] = temp_num
        temp_num = this_num

    for idx_4 in range(bottom_right_row-1, upper_left_row-1, -1):
        this_num = matrix[idx_4][upper_left_col]
        if min_num > this_num:
            min_num = this_num
        if temp_num != -1:
            matrix[idx_4][upper_left_col] = temp_num
        temp_num = this_num
    
    return matrix, min_num


def solution(rows, columns, queries):
    
    answer = []
    matrix = make_matrix(rows, columns)
    
    for query in queries:
        matrix, min_num = rotate_matrix(matrix, query, rows, columns)
        answer.append(min_num)
        
    return answer