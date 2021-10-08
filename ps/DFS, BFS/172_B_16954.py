# Baekjoon 16954 - 움직이는 미로 탈출
# Gold 4
# BFS/DFS


def go(possible):
    
    dirs = {(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    new_possible = set()
    
    for x, y in possible:
        
        new_possible.add((x, y))
        
        for dx, dy in dirs:
            
            nx = x + dx
            ny = y + dy
            
            if (nx, ny) in possible or (nx, ny) in blocks:
                continue
            
            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                continue
                
            new_possible.add((nx, ny))
            
    return new_possible


def fall(blocks):
    
    new_blocks = set()
    for x, y in blocks:
        if x < 7:
            new_blocks.add((x+1, y))
    
    return new_blocks


def remove(possible, blocks):
    
    new_possible = set()
    for x, y in possible:
        
        if (x, y) in blocks:
            continue
        
        new_possible.add((x, y))
        
    return new_possible
    

maps = [list(input()) for _ in range(8)]

blocks = set()
for i in range(8):
    for j in range(8):
        if maps[i][j] == '#':
            blocks.add((i, j))

possible = {(7, 0)}
for _ in range(8):
    possible = go(possible)
    blocks = fall(blocks)
    possible = remove(possible, blocks)

    if not possible:
        print(0)
        break
else:
    print(1)
    
    
# BFS/DFS 문제인듯 싶은데 딱히 그래프로 풀진 않음
# graph 사이즈도 8*8로 매우 작고 단순히 통과여부만 판단하면 되므로 내가 갈 수 있는 모든 좌표의 수를 세서 해결
# go ; 내가 갈 수 있는 모든 좌표 계산
# fall ; 벽이 위치를 한칸 아래로 내림
# remove ; 내가 갈 수 있는 위치에 벽이 있으면 그 위치 제거
# 내가 갈 수 있는 위치가 없으면 0, 7초가 지나도 내가 갈 수 있는 위치가 존재하면 1 ( 모든 벽은 7초 뒤에 사라짐 )