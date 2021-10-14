# Baekjoon 1080 - 행렬
# Silver 2
# 그리디


def add(c):
    
    for x in range(i, i+3):
        for y in range(j, j+3):
            c[x][y] += 1

            
def is_valid(f, c):
    
    for i in range(n):
        for j in range(m):
            if f[i][j] % 2 != c[i][j] % 2:
                return False
    return True


n, m = map(int, input().split())
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(n)]

fliped = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            fliped[i][j] = 1

cnt = 0
check = [[0] * m for _ in range(n)]
for i in range(n-2):
    for j in range(m-2):
        if fliped[i][j] % 2 != check[i][j] % 2:
            cnt += 1
            add(check)

if is_valid(fliped, check):
    print(cnt)
else:
    print(-1)
    
    
# (0, 0)부터 A와 B가 다르면 홀수번, 같으면 짝수번 바뀔 수 있도록 3*3 행렬을 +1 씩 더해나감
# 3*3 만큼 행렬을 바꿀수 있는 만큼 바꾸었을 때의 check 행렬과 fliped 행렬의 모든 원소들이 2로 나눈 나머지가 같으면 True, 아니면 False
