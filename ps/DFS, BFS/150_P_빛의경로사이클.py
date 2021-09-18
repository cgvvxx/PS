# Programmers - 빛의 경로 사이클
# Level 3
# DFS/BFS


def solution(grid):
    
    def dfs(r, c, i):
    
        visited[r][c][i] = True
        cycle = 0
        while True:

            visited[r][c][i] = True
            cycle += 1
            if i == 0:
                c += 1
            elif i == 1:
                r -= 1
            elif i == 2:
                c -= 1
            else:
                r += 1

            r %= row
            c %= col

            if grid[r][c] == 'L':
                i += 1
            elif grid[r][c] == 'R':
                i -= 1
            else:
                pass

            i %= 4

            if visited[r][c][i]:
                return cycle
            
            
    col = len(grid[0])
    row = len(grid)

    graphs = [[list(range(1, 5)) for _ in range(col)] for _ in range(row)]
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]

    answer = []
    for r in range(row):
        for c in range(col):
            for i in range(4):
                if not visited[r][c][i]:
                    answer.append(dfs(r, c, i))
    answer.sort()
    
    return answer