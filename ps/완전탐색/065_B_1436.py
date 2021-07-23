# Baekjoon 1436 - 영화감독 숌
# Silver 5
# 완전탐색

N = int(input())
i = 666
count = 0
while True:
    if '666' in str(i):
        count += 1
    if count == N:
        print(i)
        break
    i += 1