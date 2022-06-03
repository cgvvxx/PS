# solved: [1715] 카드 정렬하기
# https://www.acmicpc.net/problem/1715
# greedy, priority-queue, sorting
# 
# Gold 4
# 카드의 수가 적은 수대로 합치고 다시 넣고를 반복
# 카드의 수대로 정렬이 이루어져야 하므로 우선순위 큐 - 힙을 이용하여 정렬

import heapq

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))
    
if len(cards) == 1:
    print(0)
else:
    ans = 0
    while cards:

        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        ans += a+b

        if cards:
            heapq.heappush(cards, a+b)

    print(ans)      
