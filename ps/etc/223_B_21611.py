# Baekjoon 21611 - 마법사 상어와 블리자드
# Gold 1


def cast_blizzard(di: int, si: int):
    
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dx, dy = dirs[di-1]
    
    cx = cy = n // 2
    
    for i in range(1, si+1):
        
        nx = cx + i * dx
        ny = cy + i * dy
        
        maps[nx][ny] = 0


def get_1d_maps(maps: list):
    
    x = y = n // 2
    
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_i = 0
    maps_1d = []
    flag = False
    
    while not flag:
        
        dx, dy = dirs[dir_i % 4]
        q = (dir_i // 2) + 1
        
        for _ in range(q):
            
            x += dx
            y += dy
            
            if (x, y) == (0, -1):
                flag = True
                break
            
            maps_1d.append(maps[x][y])
            
        dir_i += 1
        
    return maps_1d


def explode_ball_once(maps_1d: list):
    
    global score

    maps_1d_new = []
    
    maps_1d.append(-1)
    b = maps_1d[0]
    cnt = 0
    
    for ball in maps_1d:
        
        if ball == 0:
            continue
        
        if b != ball:
            
            if cnt >= 4:
                score += b * cnt
                cnt = 1
                b = ball

                continue
            else:
                maps_1d_new += [b]*cnt
                cnt = 1
                b = ball
        else:
            cnt += 1
        
    return maps_1d_new


def explode_ball(maps_1d: list):

    while True:
        
        maps_1d_new = explode_ball_once(maps_1d)

        if maps_1d_new == maps_1d[:-1]:
            break
        else:
            maps_1d = maps_1d_new
            
    return maps_1d_new


def change_maps(maps_1d: list):
    
    maps_1d_new = []
    
    if maps_1d:
        b = maps_1d[0]
        cnt = 0
        
        for ball in maps_1d:
            
            if ball == 0:
                continue
            
            if b != ball:
                
                if cnt >= 4:
                    cnt = 1
                    b = ball
                    continue
                else:
                    maps_1d_new.extend([cnt, b])
                    cnt = 1
                    b = ball
            else:
                cnt += 1
                
        maps_1d_new.extend([cnt, b])
        
        return maps_1d_new

    else:
        return maps_1d


def get_2d_maps(maps_1d: list):
    
    x = y = n // 2
    
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_i = 0
    maps_2d = [[0] * n for _ in range(n)]
    idx = 0
    flag = False
    
    while not flag and maps_1d:
        
        dx, dy = dirs[dir_i % 4]
        q = (dir_i // 2) + 1
        
        for _ in range(q):
            
            x += dx
            y += dy

            if y == -1:
                flag = True
                break
            
            maps_2d[x][y] = maps_1d[idx]
            idx += 1

            if idx >= len(maps_1d):
                flag = True
                break
            
        dir_i += 1
        
    return maps_2d


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
score = 0

for _ in range(m):
    
    di, si = map(int, input().split())
    cast_blizzard(di, si)
    
    maps = get_2d_maps(change_maps(explode_ball(get_1d_maps(maps))))

print(score)


# 문제 그대로 빡구현..
# 1. 주어진 2d map에서 주어진 방향에 있는 구슬에 0
# 2. 주어진 2d map > 1d list 로 변환(get_1d_maps)
# 3. 연속된 구슬 폭발 > 다시 정렬 > 다시 폭발 > .. (explode_ball)
# 4. 구슬의 개수대로 다시 list 변환 (change_maps)
# 5. 다시 1d list > 2d map 으로 변환(get_2d_maps)

# 주의할 부분은
# 1. 2d map <-> 1d list로 변환시 인덱스 주의
# ex. 1d list가 빈 리스트인 경우도 있고
# ex. 1d list > 2d map으로 변환시킬 때 2d map의 인덱스를 벗어나는 경우
# 2. 처음 얼음파편에 의해 제거된 구슬은 점수 카운트 X !!