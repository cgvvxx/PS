# Programmers - 가장 긴 팰린드롬

def palindrome(s):
    idx, idx_len = 0, len(s)

    while True:
        if idx_len == 1:
            return 1

        check = s[idx:idx + idx_len]
        if check == check[::-1]:
            return len(check)
        elif idx + idx_len == len(s):
            idx_len -= 1
            idx = 0
        else:
            idx += 1