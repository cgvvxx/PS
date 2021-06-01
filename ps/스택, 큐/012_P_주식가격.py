# Programmers - 주식가격
# Level 2
# 스택/큐

def solution(prices):
    answer = []
    l = len(prices)

    # 단순 이중 for문 반복 > 시간복잡도 ~ O(n^2)
    for i in range(l):
        for j in range(i + 1, l):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            else:
                if j == l - 1:
                    answer.append(l - i - 1)
    answer.append(0)

    return answer


def solution(prices):
    answer = [0] * len(prices)
    stack = []

    # stack에 index를 append하여 각 index에 대해 가격이 떨어지는 경우
    # stack에서 pop하여 answer list에 해당하는 index의 값으로 입력
    # 마지막 까지 stack에 남아있는 값에 대해서는 끝까지 가격이 떨어지지 않는 경우이므로
    # 전체 길이에서 그 index만큼 뺀 값을 입력
    # 시간복잡도 ~ O(n)
    for idx, p in enumerate(prices):
        while stack and p < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = idx - j
        stack.append(idx)

    for k in stack:
        answer[k] = len(prices) - k - 1

    return answer