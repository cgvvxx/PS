# Programmers - 등굣길
# Level 3
# DP

def solution(m, n, puddles):
    # 초기 배열 m(가로)X n(세로)의 값을 -1로 초기화, [0, 0] = 1로 초기화
    arrays = [[-1] * m for _ in range(n)]
    arrays[0][0] = 1

    # puddle에 있는 곳은 0으로 초기화
    for [i, j] in puddles:
        arrays[j - 1][i - 1] = 0

    for i in range(n):
        for j in range(m):
            # puddle에 있는 위치의 경우 0
            # 아니면 [i-1, j] + [i, j-1]의 값으로 할당
            if i == 0 and j == 0:
                continue
            elif i == 0:
                if arrays[i][j - 1] * arrays[i][j] != 0:
                    arrays[i][j] = 1
                else:
                    arrays[i][j] = 0
            elif j == 0:
                if arrays[i - 1][j] * arrays[i][j] != 0:
                    arrays[i][j] = 1
                else:
                    arrays[i][j] = 0
            else:
                if arrays[i][j] == 0:
                    continue
                elif arrays[i - 1][j] == 0 and arrays[i][j - 1] == 0:
                    arrays[i][j] = 0
                else:
                    arrays[i][j] = (arrays[i - 1][j] + arrays[i][j - 1]) % 1000000007

    return arrays[-1][-1]