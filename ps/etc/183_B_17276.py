# Baekjoon 17276 - 배열 돌리기
# Silver 1


def rot_45(mat, n):
    
    d1 = [mat[i][i] for i in range(n)]
    d2 = [mat[i][-i-1] for i in range(n)]
    h = [mat[n//2][i] for i in range(n)]
    v = [mat[i][n//2] for i in range(n)]
    
    rotated_mat = [[0] * n for _ in range(n)]
    
    for i in range(n):
        
        rotated_mat[i][i] = h[i]
        rotated_mat[i][-i-1] =  v[i]
        rotated_mat[n//2][-i-1] = d2[i]
        rotated_mat[i][n//2] = d1[i]
    
    for x in range(n):
        for y in range(n):
            if rotated_mat[x][y] == 0:
                rotated_mat[x][y] = mat[x][y]
                
    return rotated_mat


def rot_45_rev(mat, n):
    
    d1 = [mat[i][i] for i in range(n)]
    d2 = [mat[i][-i-1] for i in range(n)]
    h = [mat[n//2][i] for i in range(n)]
    v = [mat[i][n//2] for i in range(n)]
    
    rotated_mat = [[0] * n for _ in range(n)]
    
    for i in range(n):
        
        rotated_mat[i][i] = v[i]
        rotated_mat[-i-1][i] =  h[i]
        rotated_mat[n//2][-i-1] = d1[i]
        rotated_mat[i][n//2] = d2[i]
    
    for x in range(n):
        for y in range(n):
            if rotated_mat[x][y] == 0:
                rotated_mat[x][y] = mat[x][y]
                
    return rotated_mat


def rot(mat, n, d):
    
    d %= 360  # 한 바퀴인 360도 기준으로 나머지에 대한 회전만 생각
    cnt = d // 45
    if cnt > 0:
        for _ in range(cnt):
            mat = rot_45(mat, n)
    else:
        for _ in range(-cnt):
            mat = rot_45_rev(mat, n)
    
    for row in mat:
        print(*row)


for _ in range(int(input())):
    n, d = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    rot(mat, n, d)


# 행렬을 45도 기준으로 회전시키는 배열 돌리기 구현 문제
# 대각선 원소와 가운데 수직, 수평 원소들을 저장해놓고 맞는 방향으로 할당해줌
# 시계방향으로 회전하는 경우와 시계반대방향으로 회전하는 경우는 따로 정의