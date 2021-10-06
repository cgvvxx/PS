# Programmers - 다음 큰 숫자
# Level 2


def solution(n):
    
    bin_n = bin(n)[2:]
    bin_len = len(bin_n)

    flag = False
    idx = 0
    ones = 0
    for j in range(bin_len-1, -1, -1):

        if not flag and bin_n[j] == '1':
            flag = True
            ones += 1
            continue

        if flag:
            if bin_n[j] == '1':
                ones += 1
            else:
                idx = j
                break

    if idx == 0:
        ans = '1' + '0' * (bin_len + 1 - idx - ones) + '1' * (ones - 1)
    else:
        ans = bin_n[:idx] + '1' + '0' * (bin_len - idx - ones) + '1' * (ones - 1)
    
    return int(ans, 2)


# 문제의 조건에 맞게 구현(?)
# 오른쪽부터 1의 개수를 카운팅 한후 왼쪽으로 밀고 0과 1로 채우는 방법으로 해결