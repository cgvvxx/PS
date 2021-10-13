# Baekjoon 2447 - 별 찍기 10
# Silver 1


def draw_star(n, x, y):
    
    if n == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                stars[x+i][y+j] = '*'
        return
    
    m = n//3
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            draw_star(m, x+m*i, y+m*j)

n = int(input())
stars = [[' '] * n for _ in range(n)]
draw_star(n, 0, 0)
for s in stars:
    print(''.join(s))
    
    
# 재귀함수로 별 찍기
# 단순히 print로 만으로는 행과 열로 재귀함수를 적용하기 어려우므로
# stars라는 2차원 배열 생성후 인덱스를 기준으로 재귀함수 적용