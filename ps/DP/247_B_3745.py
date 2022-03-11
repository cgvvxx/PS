# Baekjoon 3745 - 오름세
# Gold 2
# DP


from bisect import bisect_left


while True:
    try:
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
        print(len(D))
    except:
        break


# 기본적인 LIS - DP & 이진탐색으로 시간복잡도 O(nlogn)까지
# 이 때 입력을 무한히 받으므로 while True & try - excpet