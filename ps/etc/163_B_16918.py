# Baekjoon 16918 - 봄버맨
# Silver 1


def count_bomb(graph):
    
    pos = set()
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'O':
                pos.add((i, j))
                
    return pos


def explode_bomb(graph, pos):
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    explode_pos = set()
    
    for x, y in pos:
        explode_pos.add((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            explode_pos.add((nx, ny))
            
    return explode_pos


def make_graph(e_pos):
    
    graph = [list('O')*c for _ in range(r)]
    for x, y in e_pos:
        graph[x][y] = '.'
    return graph


def print_graph(graph):
    
    for row in graph:
        print(''.join(row))


r, c, n = map(int, input().split())
graph = [list(input()) for _ in range(r)]

if n % 2 == 0:
    for _ in range(r):
        print('O'*c)
else:
    for _ in range(n//2):
        pos = count_bomb(graph)
        e_pos = explode_bomb(graph, pos)
        graph = make_graph(e_pos)
    print_graph(graph)


# 문제의 조건에 맞게 구현하는 문제
# 특별한 아이디어 X, 그냥 단순 구현만 함