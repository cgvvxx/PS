# Baekjoon 1365 - 꼬인 전깃줄
# Gold 2
# DP


from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

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


# 기본적인 LIS
# DP & 이진탐색으로 시간복잡도 O(nlogn)까지