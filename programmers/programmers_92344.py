# solved: [92344] 파괴되지 않은 건물
# https://programmers.co.kr/learn/courses/30/lessons/92344
# prefix-sum
#
# Level 3
# 2차원 누적합
# (r1, c1) ~ (r2, c2) 까지의 모든 값을 +d 하는건 
# 누적합 하기 전 (r1, c1) = +d , (r1, c2+1) = -d, (r2, c1) = -d, (r2, c2) = +d 를 더한 후 누적합 하는 것과 동치
# 구간 합을 하는 것을 누적 합 하기 전 행렬로 바꾸어서 모두 더한 후 마지막에 누적 합 함으로써 효율성 통과 가능
# psum = (n+1) * (m+1) 꼴의 직사각형임을 주의

def solution(board, skill):
    
    n = len(board)
    m = len(board[0])
    psum = [[0] * (m+1) for _ in range(n+1)]
    
    for typ, r1, c1, r2, c2, degree in skill:
        
        degree *= (-1)**typ

        psum[r1][c1] += degree
        psum[r2+1][c1] += -degree    
        psum[r1][c2+1] += -degree
        psum[r2+1][c2+1] += degree
        
    for i in range(n):
        for j in range(m):
            psum[i][j+1] += psum[i][j]
    
    for j in range(m):
        for i in range(n):
            psum[i+1][j] += psum[i][j]
            
    ans = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += psum[i][j]
            
            if board[i][j] > 0:
                ans += 1
                
    return ans
 