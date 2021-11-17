# Baekjoon 1011 - Fly me to the Alpha Centauri
# Gold 5
# 이진탐색


from bisect import bisect_left

check = [0]
for i in range(2**20):
    check.append(check[-1]+i//2+1)
    if check[-1] >= 2**31:
        break
        
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bisect_left(check, b-a))
    
    
# 2n번 움직일 때 갈 수 있는 최대 거리는 1 + 2 + ... + n + n + (n-1) + ... + 2 + 1 = n(n+2)/4
# 2n+1번 움직일 때 갈 수 있는 최대 거리는 n(n+2)/4 + (n+1)
# k번 움직일 때 갈 수 있는 최대거리를 담은 리스트를 만든 후 이진탐색을 통해 그 인덱스를 반환