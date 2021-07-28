# Baekjoon 2164 - 카드2
# Silver 4
# 스택/큐

from collections import deque

n = int(input())
cards = deque(range(1, n+1))

i = 0
while len(cards) > 1:
    
    cards.popleft() if i % 2 == 0 else cards.rotate(-1)
    i += 1

print(cards[0])