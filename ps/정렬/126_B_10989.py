# Baekjoon 10989 - 수 정렬하기3
# Silver 5
# 정렬


count = [0] * 10001

n = int(input())
for _ in range(n):
    count[int(input())] += 1
    
for idx, num in enumerate(count):
    if num == 0:
        continue
    else:
        for _ in range(num):
            print(idx)

# 카운팅 정렬