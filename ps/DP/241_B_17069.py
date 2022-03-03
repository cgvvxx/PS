# Baekjoon 17069 - 파이프 옮기기 2
# Gold 5
# DP


def is_valid(x, y, c):
        
    if c == 0 and 0 <= y-1 and not graphs[x][y-1]:
        return True
    elif c == 1 and 0 <= y-1 and 0 <= x-1 and not graphs[x-1][y] and not graphs[x][y-1] and not graphs[x-1][y-1]:
        return True
    elif c == 2 and 0 <= x-1 and not graphs[x-1][y]:
        return True
        
    return False


n = int(input())
graphs = [list(map(int, input().split())) for _ in range(n)]

pipes = [[[0] * n for _ in range(n)] for _ in range(3)]
pipes[0][0][1] = 1

for i in range(n):
    for j in range(1, n):
        
        if graphs[i][j]:
            continue
            
        if is_valid(i, j, 0):
            pipes[0][i][j] += pipes[0][i][j-1] + pipes[1][i][j-1]
        
        if is_valid(i, j, 1):
            pipes[1][i][j] += pipes[0][i-1][j-1] + pipes[1][i-1][j-1] + pipes[2][i-1][j-1]
            
        if is_valid(i, j, 2):
            pipes[2][i][j] +=pipes[1][i-1][j] + pipes[2][i-1][j]

print(sum([pipes[k][-1][-1] for k in range(3)]))


# pipes[k][i][j]의 경우 i, j에서 k 상태의 파이프가 갈 수 있는 갯수
# k = 0 가로, k = 1 대각선, k = 2 세로
# 이 때 각각의 경우에 대해서 점화식을 이용하여 pipes를 채워줌
# ex. k=0 인 경우 (i, j-1)에서 가로인 경우(k=0) or 대각선인 경우(k=1)인 경우만 올 수 있으므로
# pipes[0][i][j] = pipes[0][i][j-1] + pipes[1][i][j-1]