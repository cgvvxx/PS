# Programmers - 거리두기 확인하기
# Level 2
# BFS/DFS

# Solution 1
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, pl, pl_check):
    queue = deque()
    queue.append((x, y))

    while queue:

        v, w = queue.popleft()

        for i in range(4):
            nx = v + dx[i]
            ny = w + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            if pl_check[nx][ny] == 0:
                continue

            if (nx, ny) == (x, y):
                continue

            if pl_check[nx][ny] == 1:
                pl_check[nx][ny] = pl_check[v][w] + 1
                queue.append((nx, ny))

                if pl_check[nx][ny] <= 3 and pl[nx][ny] == 'P':
                    return 0

    return 1


def bfs_pl(pl):
    for i in range(5):
        for j in range(5):
            if pl[i][j] == 'P':
                pl_check = make_pl_check(pl)
                if bfs(i, j, pl, pl_check) == 0:
                    return 0

    return 1


def make_pl_check(pl):
    pl_check = [[1] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if pl[i][j] == "X":
                pl_check[i][j] = 0

    return pl_check


def solution(places):
    answer = []
    for pl in places:
        answer.append(bfs_pl(pl))

    return answer


# Solution 2
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs_place(place, i, j):
    new_place = [[-1] * 5 for _ in range(5)]

    que = deque()
    que.append((i, j))

    is_dist = True
    breaker = False
    while que:
        x, y = que.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            if abs(nx - i) + abs(ny - j) > 2:
                continue

            if place[nx][ny] == "X":
                continue
            elif new_place[nx][ny] == -1:
                new_place[nx][ny] = new_place[x][y] + 1
                que.append((nx, ny))

                if (nx != i or ny != j) and place[nx][ny] == 'P' and new_place[nx][ny] >= 0:
                    is_dist = False
                    breaker = True
                    break

        if breaker:
            break

    return is_dist


def is_dist_p(place, p):
    other_p = []
    other_o = []

    for i in range(5):
        i = i - 2
        for j in range(5):
            j = j - 2

            ni = p[0] + i
            nj = p[1] + j

            if ni <= -1 or ni >= 5 or nj <= -1 or nj >= 5:
                continue

            if (i, j) != (0, 0) and abs(i) + abs(j) <= 2:
                if place[ni][nj] == 'P':
                    other_p.append((ni, nj))
                if place[ni][nj] == 'O':
                    other_o.append((ni, nj))

    return other_p, other_o


def pl_dist(pl):
    dist = True
    breaker = False
    for i in range(5):
        for j in range(5):
            if pl[i][j] == "P":
                dist = bfs_place(pl, i, j)
                if dist == False:
                    breaker = True
                    break
        if breaker:
            break

    return dist


def solution(places):
    answer = []
    for pl in places:
        answer.append(int(pl_dist(pl)))

    return answer