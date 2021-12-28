# Baekjoon 3107 - IPv6
# Gold 5
# 구현


def add_zero(s):
    
    if 0 < len(s) < 4:
        return '0'*(4-len(s)) + s
    else:
        return s

    
ip = input()
ans = ''
tar_idx = ip.find('::')
if tar_idx == -1:
    for s in ip.split(':'):
        ans += add_zero(s) + ':'
elif ip == '::':
    ans = '0000:0000:0000:0000:0000:0000:0000:0000:'
else:
    splited = ip.split(':')
    tar_len = 9 - len(splited)
    space = False
    for s in splited:
        if s == '':
            if not space:
                space = True
                for _ in range(tar_len):
                    ans += '0000:'
            else:
                ans += '0000:'
        else:
            ans += add_zero(s) + ':'

print(ans[:-1])


# 그리 어렵지 않은 구현 문제
# 문제의 조건에 맞게 케이스를 그냥 적당히 나눠버림