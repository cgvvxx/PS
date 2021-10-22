# Baekjoon 14400 - 편의점 2
# Silver 2


def dist_sum(pts):
    
    ans = 0
    for i in range(len(pts)//2):
        ans += pts[-i-1] - pts[i]
        
    return ans

xs = list()
ys = list()
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()

print(dist_sum(xs) + dist_sum(ys))


# 수학 문제(?)
# 절대값의 합의 최솟값은 정렬된 리스트에 대해 가장 가운데 값일때 발생
# 그 절대값의 합은 큰 값과 작은 값의 거리의 합과 같음을 이용하여 
# 정렬 후 dist_sum을 통해 리스트의 좌표값에 대한 거리의 합을 구함