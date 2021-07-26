# Baekjoon 11656 - 접미사 배열
# Silver 4

s = input()

last_s = [s[i:] for i in range(len(s))]
last_s.sort()

for i in last_s:
    print(i)