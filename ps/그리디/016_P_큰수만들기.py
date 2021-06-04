# Programmers - 큰 수 만들기
# Level 2
# 그리디

def solution(num, k):
    num_li = list()
    for idx, i in enumerate(num):
        i = int(i)
        if k == 0:
            break

        if len(num_li) == 0:
            num_li.append(i)
            continue
        else:
            while True:
                if k == 0:
                    break
                if len(num_li) == 0:
                    break
                if num_li[-1] >= i:
                    break
                num_li.pop()
                k -= 1
            if k == 0:
                break
            num_li.append(i)

    if k > 0:
        ans = ''.join(map(str, num_li))[:-k]
    else:
        ans = ''.join(map(str, num_li)) + num[idx:]

    return ans