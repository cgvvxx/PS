# Baekjoon 14620 - 꽃길
# Silver 2
# 완전탐색


from itertools import combinations


def get_crd_cost():
    
    crd_costs = dict()
    for i in range(1, n-1):
        for j in range(1, n-1):
            crd_costs[(i, j)] = cal_cost(i, j)
            
    return crd_costs


def get_taxi_dst(c1, c2):
    
    return abs(c1[0]-c2[0]) + abs(c1[1]-c2[1])


def cal_cost(x, y):
    
    return maps[x][y] + maps[x-1][y] + maps[x+1][y] + maps[x][y-1] + maps[x][y+1]


def is_possible(check):
    
    for i in range(len(check)):
        for j in range(i+1, len(check)):
            if get_taxi_dst(check[i], check[j]) < 3:
                return False
    else:
        return True


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

crd_costs = get_crd_cost()
crd_costs = sorted(crd_costs.items(), key=lambda x:x[1])

ans = 10**4
for comb in combinations(crd_costs, 3):
    cs, costs = zip(*comb)
    costs = sum(costs)
    if is_possible(cs) and ans > costs:
        ans = costs
print(ans)


# 각 좌표별로 꽃을 심었을 때의 가격을 dictionary에 저장
# 각 좌표들의 3개의 조합의 모든 경우의 수(최악의 경우 64C3)에 대해 
# 각 좌표들의 택시 거리가 3이상일 때의 가격의 합의 최솟값을 return