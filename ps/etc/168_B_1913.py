# Baekjoon 1913 - 달팽이
# Silver 5


n = int(input())
target = int(input())

num = n**2
arr = [[0] * n for _ in range(n)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

i, j = 0, 0
dir_num = 0
for _ in range(n**2):
    
    if num == target:
        ans = (i+1, j+1)
    
    arr[i][j] = num
    num -= 1
    
    d = dirs[dir_num % 4]
    ni = i + d[0]
    nj = j + d[1]
    
    if ni < 0 or nj < 0 or ni >= n or nj >= n or arr[ni][nj] != 0:
        dir_num += 1
        d = dirs[dir_num % 4]
        
        ni = i + d[0]
        nj = j + d[1]
        
    i = ni
    j = nj
    
for line in arr:
    print(*line)
print(*ans)


# 간단한 버전의 달팽이 구현