# Baekjoon 16926 - 배열 돌리기 1
# Silver 2


def find_tar(k: int, r: int):
    
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_num = 0
    
    x, y = k, k
    tot_num = 2*(m+n-4*k)-4
    r %= tot_num
    
    for _ in range(r):
        
        dx, dy = dirs[dir_num % 4]
        x, y = x + dx, y + dy
        
        if x < k or x > n-k-1 or y < k or y > m-k-1:
            
            x, y = x - dx, y - dy
            dir_num += 1
            
            dx, dy = dirs[dir_num % 4]
            x, y = x + dx, y + dy
            
    temps = []
    for _ in range(tot_num):
        
        dx, dy = dirs[dir_num % 4]
        x, y = x + dx, y + dy
        
        if x < k or x > n-k-1 or y < k or y > m-k-1:
            
            x, y = x - dx, y - dy
            dir_num += 1
            
            dx, dy = dirs[dir_num % 4]
            x, y = x + dx, y + dy
        
        temps.append(arrs[x][y])
            
    return temps[::-1]


def rotate_shell(k: int):
    
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_num = 0
    
    x, y = k, k
    i = 0
    temps = find_tar(k, r)
    
    
    for num in temps:
        
        arrs[x][y] = num
        
        dx, dy = dirs[dir_num % 4]
        x, y = x + dx, y + dy
            
        if x < k or x > n-k-1 or y < k or y > m-k-1:
            
            x, y = x - dx, y - dy
            dir_num += 1
            
            dx, dy = dirs[dir_num % 4]
            x, y = x + dx, y + dy
            
            
def rotate_arrs():
    
    k = min(n, m) // 2
    for i in range(k):
        rotate_shell(i)

        
n, m, r = map(int, input().split())
arrs = [list(map(int, input().split())) for _ in range(n)]
rotate_arrs()
for arr in arrs:
    print(*arr)
    

# 구현
# 껍데기(바깥쪽에서 k번째 둘레)를 돌리는 함수를 구현 후 r번 반복하려고 했응나 => r이 크면 불필요한 연산이 너무 많아짐
# 껍데기에서 시계 방향으로 r번째 값을 구한 후 반시계 방향으로 temps 리스트를 먼저 구해 놓은 후
# 껍데기의 (k, k)에서 시작하여 반시계 방향으로 temps 값을 할당