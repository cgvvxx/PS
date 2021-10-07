# Programmers - 방문 길이
# Level 2


def solution(dirs):
    
    def to_num(x, y):
    
        return 100*x+y
    
    dir_dict = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    pos = (0, 0)
    been = set()
    answer = 0
    
    for d in dirs:

        d_pos = dir_dict[d]
        next_pos = (pos[0] + d_pos[0], pos[1] + d_pos[1])

        if -5 <= next_pos[0] <= 5 and -5 <= next_pos[1] <= 5:
            n1 = to_num(*pos)
            n2 = to_num(*next_pos)
            check = (n1, n2)
            if check not in been:
                answer += 1
                been.add(check)
                been.add(check[::-1])
            pos = next_pos

    return answer


# dir에 해당하는 방향으로 간 좌표 next_pos와 pos로 가본 길인지 아닌지 체크해야함
# 주어진 좌표평면이 -5~5로 제한되어 있으므로 (x, y) <=> 100*x+y 는 일대일 대응임을 이용해서
# 가본 길을 체크하는 set에 check에 해당하는 tuple을 넣어 가본 길인지 아닌지 체크함
# 크기가 커지면 다른 방법으로 해야할 듯