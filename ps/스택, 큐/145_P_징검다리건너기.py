# Programmers - 징검다리 건너기
# Level 3
# 스택/큐 - 힙


import heapq

def solution(stones, k):
    
    heap = []
    answer = 10**9

    for i in range(len(stones)):
        
        heapq.heappush(heap, (-stones[i], i))

        if len(heap) < k:
            continue
        else:
            while True:
                if heap[0][1] <= i-k:
                    heapq.heappop(heap)
                else:
                    break


        if answer > -heap[0][0]:
            answer = -heap[0][0]

    return answer


# k개의 연속된 돌들 중에 최댓값이 가장 작을 때 그 값이 answer가 됨
# 최대 힙을 이용해서 heap에 돌과 그 index를 넣고 힙의 길이가 k보다 작으면 append
# 힙의 길이가 k보다 커졌을 때 최대크기의 돌의 index가 현재 위치(i) 보다 k 만큼 작은 수 보다 작은 경우 pop
# 이 때의 최댓값이 k개의 연속된 돌들 중의 최댓값
# 이를 전체 돌들에 대해서 반복하면서 최댓값의 최솟값을 찾음