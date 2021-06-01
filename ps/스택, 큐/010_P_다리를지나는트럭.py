# Level2
# 스택/큐

from collections import deque


def solution(bridge_length, weight, truck_weights):
    queue = deque()
    idx = 0
    time = 0
    bridge_weight = 0

    # Queue에 truck_weights을 앞에서부터 하나씩 append
    ## 시간복잡도 ~ O(n)

    while True:
        # Queue에 아무것도 없다면 무조건 append
        if len(queue) == 0:
            queue.append(truck_weights[idx])
            bridge_weight += truck_weights[idx]

            idx += 1
            time += 1
            continue

        # idx가 truck_weights의 길이만큼 간다면(마지막 truck 까지 append 되어 있다면)
        # while문 종료
        if idx == len(truck_weights):
            time += bridge_length
            break

        # Queue가 bridge_length 개수 만큼 가득 차 있다면 가장 먼저 들어간 truck을 pop
        if len(queue) == bridge_length:
            truck_weight = queue.popleft()
            bridge_weight -= truck_weight

        # 새로 들어갈 truck이 다리의 weight을 버틸 수 있다면 그대로 다음 truck을 append
        # 못 버틴다면 0을 append하고 다시 while문 반복
        if bridge_weight + truck_weights[idx] > weight:
            queue.append(0)
        else:
            queue.append(truck_weights[idx])
            bridge_weight += truck_weights[idx]
            idx += 1

        time += 1

    return time
