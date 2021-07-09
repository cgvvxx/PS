# Programmers - 이중우선순위큐
# Level 3
# 스택/큐 - 힙

import heapq

def solution(operations):
    heap = []
    for ops in operations:

        op, num = ops.split(" ")
        if op == 'I':
            heapq.heappush(heap, int(num))  # heap 구조로 push
        else:
            if len(heap) == 0:
                continue

            if int(num) == 1:  # max 값 delete할 때 list의 index 이용 & 다시 heapify
                max_idx = heap.index(max(heap))
                heap.pop(max_idx)
                heapq.heapify(heap)
            else:  # min 값 delete의 경우 단순히 pop
                heapq.heappop(heap)

    if len(heap) == 0:
        return [0, 0]
    else:
        return [heapq.nlargest(1, heap)[0], heap[0]]