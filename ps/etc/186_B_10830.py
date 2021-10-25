# Baekjoon 10830 - 행렬 제곱
# Gold 4
# Divide & Conquer


def inner_prod(a, b):
    
    return sum(map(lambda x:x[0]*x[1]%1000, zip(a, b)))


def mat_prod(A, B):
    
    mat = [[0]*len(A) for _ in range(len(B[0]))]
    
    B_star = list(zip(*B))
    for idx in range(len(A)):
        for jdx in range(len(B_star)):
            mat[idx][jdx] = inner_prod(A[idx], B_star[jdx])
    
    return mat


def mat_power(A, n):
    
    if n == 1:
        return A
    else:
        x = mat_power(A, n//2)
        y = mat_prod(x, x)
        if n % 2 == 0:
            return y
        else:
            return mat_prod(y, A)
        
        
n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

for r in mat_power(A, b):
    for i in r:
        print(i%1000, end=' ')
    print()
    
    
# 분할 정복 대표 문제
# 거듭 제곱을 O(n) => O(log n) 만큼 줄일 수 있음!
# 행렬의 곱셉만 따로 정의해서 해결