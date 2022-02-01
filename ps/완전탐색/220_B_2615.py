# Baekjoon 2615 - 오목
# Silver 2
# 완전탐색


def get_crd(board: list):
    
    blacks = set()
    whites = set()
    for i in range(19):
        for j in range(19):
            if board[i][j] == 1:
                blacks.add((i, j))
            elif board[i][j] == 2:
                whites.add((i, j))
                
    return blacks, whites


def is_omok(stones: set):
    
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    for x, y in stones:
        
        for dx, dy in dirs:

            ans = [(x, y)]

            for i in range(1, 5):
                
                nx = x + i*dx
                ny = y + i*dy
                
                if nx < 0 or nx >= 19 or ny < 0 or ny >= 19:
                    break
                    
                if (nx, ny) in stones:
                    ans.append((nx, ny))
                    continue
                else:
                    break
                    
            else:
                
                nx = x + 5*dx
                ny = y + 5*dy

                nnx = x - dx
                nny = y - dy
                
                if (nx, ny) not in stones and (nnx, nny) not in stones:
                    ans.sort(key=lambda x:(x[1], x[0])) 
                    return True, *ans[0]
                
    return False, None, None
    

board = [list(map(int, input().split())) for _ in range(19)]
blacks, whites = get_crd(board)

b, bx, by = is_omok(blacks)
w, wx, wy = is_omok(whites)

if b:
    print(1)
    print(bx+1, by+1)
elif w:
    print(2)
    print(wx+1, wy+1)
else:
    print(0)



# 단순히 완전탐색으로 구현함 (시간을 줄이려고 조금 더 효율적인 방법을 고민해봤는데 완전탐색으로도 해결되도록 한듯 => 시간을 줄이려면?)
# 1. 모든 돌들의 좌표를 구하고 각각의 돌들에 대해
# 2. 상하좌우와 대각선 방향으로 5개의 돌이 있는지
# 3. 추가적으로 주어진 방향의 *(-1), *5 방향 좌표에 주어진 돌이 없는지 체크