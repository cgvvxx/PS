# solved: [2212] 센서
# https://www.acmicpc.net/problem/2212
# greedy, sorting
# 
# Gold 5
# N <= K인 경우 당연히 0
# sensors의 위치를 정렬 후, 각 센서의 위치 차이를 s_diff에 append
# s_diff를 정렬 후, 작은 값부터 N-K개의 위치 차이를 return
# 즉, greedy하게 해당 센서들의 위치를 정렬하였을 때, 위치 차이가 작은 값부터 N-K개의 합이 문제에서 요구하는 거리의 합의 최소값

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

if N <= K:
    print(0)
else:
    sensors.sort()
    s_diff = [sensors[i+1]-sensors[i] for i in range(N-1)]
    s_diff.sort()

    print(sum(s_diff[:N-K]))    
