# Baekjoon 21608 - 상어 초등학교
# Silver 1


from collections import defaultdict
import sys
input = sys.stdin.readline

def get_closest_crd(x: int, y:int):
    
    crds = []
    
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if i < 0 or i >= n or j < 0 or j >= n:
            continue
        
        crds.append((i, j))
        
    return crds


def get_likest_seat(studs: list):
    
    likest_seat_dict = defaultdict(int)
    
    for s in studs:
        
        if s not in seated_crd_from_num:
            continue
        
        i, j = seated_crd_from_num[s]
        checks = get_closest_crd(i, j)
        
        for l, m in checks:
                
            if (l, m) in seated_num_from_crd:
                continue
                
            likest_seat_dict[(l, m)] += 1
    
    if likest_seat_dict:
        max_num = max(likest_seat_dict.values())
        n_likest_seat_dict = set()    
        
        for i, j in likest_seat_dict:

            if (i, j) in seated_num_from_crd:
                continue
                
            if likest_seat_dict[(i, j)] == max_num:
                n_likest_seat_dict.add((i, j))

        return n_likest_seat_dict
    
    else:
        return set()


def get_empty_seat(seat_set: set):
    
    cnt = -1
    x, y = n, n
    
    if not seat_set:
        
        for i in range(n):
            for j in range(n):
                
                if (i, j) in seated_num_from_crd:
                    continue
                    
                seat_set.add((i, j))
    
    for i, j in seat_set:
        check = [(i, j) for i, j in get_closest_crd(i, j) if (i, j) not in seated_num_from_crd]

        if len(check) > cnt:
            cnt = len(check)
            x, y = i, j
        elif len(check) == cnt:
            x, y = sorted([(x, y), (i, j)])[0]
    
    return x, y


def get_my_seat(studs: list):
    
    likests = get_likest_seat(studs)
    x, y = get_empty_seat(likests)
    
    return x, y


def get_score(seat: list):
    
    score = 0
    for i in range(n):
        for j in range(n):
            
            num = seat[i][j]
            checks = get_closest_crd(i, j)
            cnt = 0
            
            for l, m in checks:
                if seat[l][m] in stud_dict[num]:
                    cnt += 1
            
            if cnt != 0:
                score += 10 ** (cnt-1)
    
    return score
    

n = int(input())

seat = [[0] * n for _ in range(n)]
seated_crd_from_num = dict()
seated_num_from_crd = dict()
stud_dict = dict()

for _ in range(n**2):
    i, *studs = map(int, input().split())
    nx, ny = get_my_seat(studs)
    
    stud_dict[i] = studs
    seat[nx][ny] = i
    seated_crd_from_num[i] = (nx, ny)
    seated_num_from_crd[(nx, ny)] = i

print(get_score(seat))


# 구현 요구 사항 자체는 어렵지 않았는데 너무 오래 걸림
# 1. 좋아하는 친구를 기준가 가장 많은 자리 찾기 
# 2. 여러 개 존재하는 경우 주위의 빈자리가 가장 많은 자리 찾기
# 3. 여러 개 존재하는 경우 행 번호 > 열 번호가 작은 순으로
# 최대한 함수를 재활용할 수 있게끔 짜려고 했는데 중간에 추가 조건을 계속 덧붙이느라 오래 걸림
# 문제를 접근할 때부터 필요한 함수를 세팅하고 접근해야 할듯