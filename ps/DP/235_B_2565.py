# Baekjoon 2565 - 전깃줄
# Gold 5
# DP


from bisect import bisect_left

n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]
nums.sort(key=lambda x:x[0])
arr = list(map(lambda x:x[1], nums))

D = []
for i in arr:
    
    if not D:
        D.append(i)
        continue
        
    if D[-1] < i:
        D.append(i)
    else:
        D[bisect_left(D, i)] = i

print(n-len(D))


# (전깃줄 번호1, 번호2)를 번호1의 순서로 정렬 후 번호2의 리스트를 구한 후 LIS