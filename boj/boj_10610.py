# solved: [10610] 30
# https://www.acmicpc.net/problem/10610
# greedy, sorting
# 
# Silver 5
# 주어진 수에서 0이 존재하지 않거나 각 자리의 숫자 합이 0이 아닌 경우 -1 출력
# 아닌 경우 0 하나를 제외하여 역순 정렬 후 출력

n = list(input())

if '0' not in n:
    print(-1)
else:
    n.remove('0')
    check = sum(map(int, n))
    if check % 3:
        print(-1)
    else:
        n.sort(reverse=True)
        print(''.join(n) + '0')     
