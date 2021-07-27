# Programmers - N-Queen
# Level 3
# 완전탐색 - 백트래킹


def solution(n):
    
    board = []
    ct = []

    def is_diagonal(board, k):

        l = board + [k]
        if len(l) <= 1:
            return True
        idx_k = len(l)-1

        for i in range(len(l)-1):
            if abs(i - idx_k) == abs(l[i] - k):
                 return False

        return True

    def dfs_chess():

        if len(board) == n:
            ct.append(1)
            return

        for i in range(n):
            if i in board:
                continue

            if not is_diagonal(board, i):
                continue

            board.append(i)
            dfs_chess()
            board.pop()

    dfs_chess()
    
    return sum(ct)