# Baekjoon 12933 - 오리
# Silver 5


q_list = [0] * 5
exit = False
n = -1

for char in input():
    
    if char == 'q':
        q_list[0] += 1
        if q_list[0] > n:
            n = q_list[0]
    elif char == 'u':
        q_list[1] += 1
        if q_list[0] < q_list[1]:
            exit = True
            break
    elif char == 'a':
        q_list[2] += 1
        if min(q_list[:2]) < q_list[2]:
            exit = True
            break
    elif char == 'c':
        q_list[3] += 1
        if min(q_list[:3]) < q_list[3]:
            exit = True
            break
    elif char == 'k':
        q_list[4] += 1
        if min(q_list[:4]) < q_list[4]:
            exit = True
            break
        for i in range(5):
            q_list[i] -= 1

if exit:
    print(-1)
else:
    if len(set(q_list)) == 1:
        print(n)
    else:
        print(-1)


# 단순한 구현문제라 그냥 케이스를 나눠서 풀었음
# 조금 더 간단히 할 수 있을거 같은데...