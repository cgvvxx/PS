# Baekjoon 11054 - 가장 긴 바이토닉 부분 수열
# Gold 3
# DP


from bisect import bisect_left


def get_DK(arr):

    D = [arr[0]]
    K = [1]
    K_max = 1
    for i in arr[1:]:

        if D[-1] < i:
            K_max += 1
            D.append(i)
            K.append(K_max)
        else:
            j = bisect_left(D, i)
            D[j] = i
            K.append(j+1)
            
    return D, K


n = int(input())
arr = list(map(int, input().split()))

d1, k1 = get_DK(arr, n)
d2, k2 = get_DK(arr[::-1], n)
k2 = k2[::-1]

b_max = 0
for idx in range(n):
    b_max = max(b_max, max(k1[:idx+1]) + max(k2[idx:])-1)
print(b_max)


# 12015 - 가장 긴 증가하는 부분수열 2 참고
# 가장 긴 바이토닉 부분 수열 = 앞에서부터 가장 긴 증가하는 부분 수열 + 뒤에서부터 가장 긴 증가하는 부분 수열
# 주어진 수들의 원래 순서대로 K, 역순의 K를 구한 뒤
# (이 때, K는 주어진 수들의 크기 순으로 나열했을 때의 인덱스 값의 리스트)
# K 값들의 합이 최대가 되는 지점에서의 최댓값을 계산