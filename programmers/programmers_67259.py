# solved: [67259] 경주로 건설
# https://programmers.co.kr/learn/courses/30/lessons/67259
# bfs, bruteforcing, dp
#
# Level 3
# bfs를 통한 최소 비용을 갖는 경로 구하기
# 최소 비용을 업데이트하면서 (최소 비용은 방향으로 결정) board에 기록해서 나아가면 됨
# 단, 그 칸에 도달하는 비용이 최소가 아니어도 마지막 도착지점에 도달하는 비용이 최소가 되는 반례가 존재
# ex. board = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
# https://hillier.tistory.com/84 참고
# * 반례의 경우는 비용의 차가 400 미만일 때 발생하므로 이 예외케이스를 추가 >> 파악하는게 굉장히 어려웠음....

from collections import deque

def solution(board):
    
    def is_valid(x, y):
        
        if x == y == 0:
            return False
    
        if x < 0 or y < 0 or x >= n or y >= n:
            return False

        if board[x][y] == 1:
            return False

        return True

    def bfs():

        queue = deque()
        queue.append((0, 0, -1, 0))
        ans = NMAX

        while queue:
            
            x, y, d, cost = queue.popleft()
            
            if (x, y) == (n-1, n-1) and ans > cost:
                ans = cost
                continue

            for i in range(4):

                nx = x + dx[i]
                ny = y + dy[i]
                nd = dirs[i]
                
                if d == nd or d == -1:
                    n_cost = cost + 100
                else:
                    n_cost = cost + 600

                if is_valid(nx, ny) and dp[nx][ny] >= n_cost - 400:
                    dp[nx][ny] = n_cost
                    queue.append((nx, ny, nd, n_cost))

        return ans
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dirs = [0, 1, 2, 3]
    n = len(board)
    NMAX = 10**9
    
    dp = [[NMAX for _ in range(n)] for _ in range(n)]
   
    return bfs()
