# Baekjoon 15686 - 치킨 배달
# Gold 5
# 완전탐색 


from itertools import combinations


def chicken_dist(a, b):
    
    return sum((abs(a[0]-b[0]), abs(a[1]-b[1])))


def cal_city_chicken_dist(dist_list):
    
    return sum(map(min, dist_list))


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

position_dict = {1:[], 2:[]}

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            position_dict[1].append((i, j))
        elif matrix[i][j] == 2:
            position_dict[2].append((i, j))
        else:
            pass

r = len(position_dict[2])
dist = []
for pos1 in position_dict[1]:
    pos_dist = []
    for pos2 in position_dict[2]:
        pos_dist.append(chicken_dist(pos1, pos2))
    dist.append(pos_dist)

answer = 10**10
for i in combinations(range(r), M):
    this_dist = [[dist[k][idx] for idx in i] for k in range(len(dist))]
    chick_dist = cal_city_chicken_dist(this_dist)
    if answer > chick_dist:
        answer = chick_dist

print(answer)