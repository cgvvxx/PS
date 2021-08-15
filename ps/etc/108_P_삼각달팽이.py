# Programmers - 삼각달팽이
# Level 2

def solution(n):
    
    arr = [[0] * i for i in range(1, n+1)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    count = 1
    d = 0
    x, y = -1, 0
    
    while count <= n * (n+1) // 2 :
        
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx < 0 or nx >= n or ny < 0 or ny > nx:
            d = (d + 1) % 3
            continue
            
        if arr[nx][ny] != 0:
            d = (d + 1) % 3
            continue
            
        x, y = nx, ny
        arr[nx][ny] = count
        count += 1
    
    return sum(arr, [])