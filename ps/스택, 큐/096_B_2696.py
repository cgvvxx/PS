# Baekjoon 2696 - 중앙값 구하기
# Gold 2
# 스택/큐 - 힙


import heapq

def return_median(arr):

    min_heap = []
    max_heap = []
    median_nums = []

    for num in arr:

        if len(min_heap) == len(max_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, (num, num))

        if len(min_heap) > 0 and max_heap[0][1] > min_heap[0][1]:
            bigger = heapq.heappop(max_heap)[1]
            smaller = heapq.heappop(min_heap)[1]

            heapq.heappush(max_heap, (-smaller, smaller))
            heapq.heappush(min_heap, (bigger, bigger))
        
        if len(max_heap) > len(min_heap):
            median_nums.append(max_heap[0][1])
    
    return median_nums


N = int(input())
medians = []

for _ in range(N):
    arr =[]
    m = int(input())
    
    for _ in range(m // 10 + 1):
        arr.extend(map(int, input().split()))
        
    medians.append(return_median(arr))

for med in medians:
    
    print(len(med))
    
    for i in range(len(med) // 10 + 1):
        print(*med[i*10:i*10+10])