# Baekjoon 21610 - 마법사 상어와 비바라기
# Gold 5
# 구현


def move_cloud(clouds, di, si):
    
    dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    dx, dy = dirs[di-1]
    
    return list(map(lambda x: ((x[0]+dx*si)%n, (x[1]+dy*si)%n), clouds))

def rain(clouds):
    
    dirs = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

    for i, j in clouds:
        maps[i][j] += 1

    for i, j in clouds:
        for di, dj in dirs:
            
            ni = i + di
            nj = j + dj
            
            if ni < 0 or nj < 0 or ni >= n or nj >= n:
                continue
            
            if maps[ni][nj] > 0:
                maps[i][j] += 1

def make_cloud(clouds):
    
    clouds = set(clouds)
    new_clouds = []
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] >= 2 and (i, j) not in clouds:
                maps[i][j] -= 2
                new_clouds.append((i, j))

    return new_clouds

def cycle(clouds, di, si):
    
    clouds = move_cloud(clouds, di, si)
    rain(clouds)
    clouds = make_cloud(clouds)
    
    return clouds


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    di, si = map(int, input().split())
    clouds = cycle(clouds, di, si)
    
print(sum(sum(maps, [])))


# 문제 요구 충실하게 구현
# move_cloud > rain > make_cloud의 과정을 한 사이클로 반복