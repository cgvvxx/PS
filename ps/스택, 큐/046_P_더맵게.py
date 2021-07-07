# Programmers - 더 맵게
# Level 2
# 스택/큐 - 힙

import heapq


def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:  # 음식이 2개 이상인 경우에만

        if scoville[0] >= K:
            return count

        else:  # heap을 이용하여 가장 작은값, 두번째로 작은값을 구해 연산
            min1_sco = heapq.heappop(scoville)
            min2_sco = heapq.heappop(scoville)
            heapq.heappush(scoville, min1_sco + 2 * min2_sco)
            ㅌ
            count += 1

    if scoville[0] >= K:
        return count
    else:  # 문제의 조건을 만족하지 않는 경우
        return -1