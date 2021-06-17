# Programmers - 문자열 압축
# Level 2

def comp_to_n(s, n):
    n_list = []
    for i in range(len(s)):
        if i * n <= len(s):
            n_list.append(s[i * n:i * n + n])
        else:
            break

    n_list.append(' ')
    ans = ''
    count = 1
    check = n_list[0]
    for idx in range(len(n_list)):
        if idx == 0:
            continue

        if n_list[idx] == check:
            count += 1
        else:
            if count >= 2:
                ans += str(count)
            ans += check
            count = 1
            check = n_list[idx]

    return ans


def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        comp_len = len(comp_to_n(s, i))
        if answer >= comp_len:
            answer = comp_len

    return answer