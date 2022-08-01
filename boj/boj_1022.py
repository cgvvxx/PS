# solved: [1022] 소용돌이 예쁘게 출력하기
# https://www.acmicpc.net/problem/1022
# implementation
# 
# Gold 4
# 문제에서 요구하는대로 잘 구현할 것
# 단순히 전체 숫자를 list에 넣은 후에 해당 인덱스로 자리면 메모리 초과 발생
# 1. (r, c) 위치에 해당하는 숫자를 return하는 num_at 함수
# 2. num_at 함수를 이용하여 주어진 (r1, c1) ~ (r2, c2) 숫자를 담은 리스트를 생성 후
# 3. 해당 숫자들의 최댓값 자릿수를 기준으로, 그 자릿수보다 작다면 앞에 공백 패딩을 추가하여 출력

def num_at(r, c):
    
    n = max(abs(r), abs(c))
    
    if c == n:
        if r == n:
            return (2*n+1)**2
        else:
            return (2*n-1)**2 + n - r
    elif r == -n:
        return (2*n-1)**2 + 3*n - c
    elif c == -n:
        return 4*n**2 + 1 + r + n
    else:
        return (2*n+1)**2-n+c

def pretty_print():
    
    max_num = 0
    pretty_nums = []
    for r in range(r1, r2+1):
        line = []
        for c in range(c1, c2+1):
            chk = num_at(r, c)
            if chk > max_num:
                max_num = chk
            line.append(chk)
        pretty_nums.append(line)

    max_len = len(str(max_num))
    for ns in pretty_nums:
        print(*map(lambda x:' '*(max_len-len(str(x)))+str(x), ns))


r1, c1, r2, c2 = map(int, input().split())
pretty_print()
