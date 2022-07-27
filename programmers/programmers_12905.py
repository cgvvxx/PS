# solved: [12905] 가장 큰 정사각형 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12905
# dp
#
# Level 2
# board의 해당 칸(i, j)의 (i-1, j-1), (i-1, j), (i, j-1)에 현재까지의 최대 정사각형의 한 변의 길이를 기록

def solution(board):
    
    n = len(board)
    m = len(board[0])
    ans = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                ans = max(1, ans)
                
            if i >= 1 and j >= 1 and board[i][j]:
                board[i][j] = min([board[i-1][j-1], board[i-1][j], board[i][j-1]]) + 1
                ans = max(ans, board[i][j])
                
    return ans ** 2
