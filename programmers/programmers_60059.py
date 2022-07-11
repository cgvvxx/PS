# solved: [60059] 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# bruteforcing
#
# Level 3
# key가 회전하는 경우 4가지 * lock에 key를 대입하는 경우 (N+2M-1)^2가지, 최대 약 15000가지이므로 완전탐색으로 해결
# 1. rotate : key의 회전함수
# 2. put : lock의 x, y 위치에 key를 꽂아지는지 체크, 이 때 돌기와 돌기가 만나면 안되고, 키의 돌기와 자물쇠의 홈만 만나야 함
# 3. check : lock에 key를 대입할 수 있는 (N+2M-1)^2가지 체크
# 4. 4번의 회전 모두 check를 진행하면서 true가 나오는 경우 바로 return

def rotate(k):
    
    return list(zip(*k[::-1]))


def put(k, l, x, y, cnt):
    
    len_k = len(k)
    len_l = len(l)
    
    for i in range(len_k):
        for j in range(len_k):
            if 0 <= x + i < len_l and 0 <= y + j < len_l:
                if k[i][j] == 1 and l[x+i][y+j] == 1:
                    return False
                
                if k[i][j] == 1 and l[x+i][y+j] == 0:
                    cnt -= 1
                    
    if cnt:
        return False 
    else:
        return True


def check(k, l, cnt):
    
    len_l = len(l)
    len_k = len(k)
    
    for i in range(-len_k+1, len_l):
        for j in range(-len_k+1, len_l):
            if put(k, l, i, j, cnt):
                return True
    
    return False


def solution(key, lock):
    
    n = len(lock)
    cnt = n*n - sum(sum(lock, []))
    
    for _ in range(4):
        if check(key, lock, cnt):
            return True        
        else:
            key = rotate(key)
    
    return False
