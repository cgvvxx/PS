# Baekjoon 10994 - 별 찍기 (19)
# Silver 4


def draw_star(n):
    
    if n == 1:
        return ['*']
    
    m = 4*n-3
    stars = [[' ']*m for _ in range(m)]
    
    for i in range(m):
        stars[i][0] = '*'
        stars[0][i] = '*'
        stars[i][-1] = '*'
        stars[-1][i] = '*'
        
    stars_b = draw_star(n-1)
        
    for i in range(2, m-2):
        for j in range(2, m-2):
            stars[i][j] = stars_b[i-2][j-2]
            
    return stars


for s in draw_star(int(input())):
    print(''.join(s))


# 재귀적으로 별 찍기
# n=1 인 경우 * 하나
# n인 경우 (2,2)의 리스트 원소부터 n-1의 별찍기 원소로 할당