# Baekjoon 13334 - 철로
# Gold 2
# 스택/큐


import heapq

spots = []
for _  in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    spots.append((a, b))
d = int(input())

spots.sort(key=lambda x:x[1])
s_heap = []

count = 0
for s, e in spots:
    
    if e - s > d:
        continue
    
    heapq.heappush(s_heap, s)
    
    while s_heap[0] < e - d:
        heapq.heappop(s_heap)
    
    if count < len(s_heap):
        count = len(s_heap)

print(count)


# heap 이용해서 시간복잡도(nlogn)에 해결하면 되는 듯
# 풀고 나면 어려운건 아닌데 생각보다 시간이 오래걸림
# 1. 끝나는 기준으로 정렬 후
# 2. 시작 시간을 담는 heap을 만들어 주어진 경우가 하나의 철로에 포함되는지 안되는지 여부를 판단