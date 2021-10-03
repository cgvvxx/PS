# Baekjoon 20057 - 마법사 상어와 토네이도
# Gold 3


def cal_pos(pos1, pos2, cal_type): # 1 : plus, 2 : minus
    
    new_pos = []
    if cal_type == 1:
        for i in range(2):
            new_pos.append(pos1[i] + pos2[i])
    else:
        for i in range(2):
            new_pos.append(pos1[i] - pos2[i])
    
    return new_pos    


def get_pos(pos, my):
    
    my_dir = directions[my % 4]
    right_dir = directions[(my-1) % 4]
    left_dir = directions[(my+1) % 4]
    
    a = cal_pos(pos, my_dir, 1)
    x = cal_pos(pos, my_dir, 2)
    
    salt = graph[pos[0]][pos[1]]
    
    salts = []
    
    salts.append((*cal_pos(a, my_dir, 1), int(0.05*salt)))
    
    salts.append((*cal_pos(a, right_dir, 1), int(0.1*salt)))
    salts.append((*cal_pos(a, left_dir, 1), int(0.1*salt)))
    
    salts.append((*cal_pos(pos, right_dir, 1), int(0.07*salt)))
    salts.append((*cal_pos(pos, left_dir, 1), int(0.07*salt)))
    
    salts.append((*cal_pos(x, right_dir, 1), int(0.01*salt)))
    salts.append((*cal_pos(x, left_dir, 1), int(0.01*salt)))
    
    salts.append((*cal_pos(cal_pos(pos, right_dir, 1), right_dir, 1), int(0.02*salt)))
    salts.append((*cal_pos(cal_pos(pos, left_dir, 1), left_dir, 1), int(0.02*salt)))
    
    salt_sum_temp = sum(map(lambda x:x[2], salts))
    salts.append((*a, salt - salt_sum_temp))
    
    valid_salts = []
    for i, j, s in salts:
        if i < 0 or j < 0 or i >= n or j >= n:
            continue
        valid_salts.append((i, j, s))
        
    salt_sum = sum(map(lambda x:x[2], valid_salts))
    
    return valid_salts, salt - salt_sum


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
my = -1
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
pos = [n//2, n//2]
is_break = False

while not is_break:
    my += 1
    my_dir = directions[my%4]
    
    steps = (my // 2) + 1
    for _ in range(steps):
        
        pos = cal_pos(pos, my_dir, 1)
        
        if pos == [0, 0]:
            is_break = True
            
        salts, left_salt = get_pos(pos, my)
        answer += left_salt
        for i, j, s in salts:
            graph[i][j] += s
        graph[pos[0]][pos[1]] = 0
        
        if is_break:
            break
            
print(answer)


# 문제 조건에 맞게 구현하는 문제
# 1. 현재 위치와 방향을 체크하면서 돌리는 부분, 2. 소금을 분배하는 부분
# 1, 2만 잘 생각해서 구현하면 되었던 문제였던듯
# 다만 a 부분에 남아있는 소금이 가야 되는데 단순히 0.55 만큼의 소금이 간다고 착각해서 이 부분 해결하는데 시간이 다소 소요됨