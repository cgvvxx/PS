# Baekjoon 16719 - ZOAC
# Gold 5
# 스택/큐 - 덱, 힙


import heapq

word = input()
heap = list(zip(word, range(len(word))))
temp = []

heapq.heapify(heap)
ans = list()

left = [-1]
right = len(word)

while heap:
    
    w, n = heapq.heappop(heap)

    if left[-1] < n:
        left.append(n)
        ans.append((n, w))
        ans.sort()
        print(''.join(map(lambda x:x[1], ans)))
    else:
        temp.append((w, n))

    if left[-1] == right - 1:
        right = left.pop()
        while temp:
            heapq.heappush(heap, temp.pop())


# 힙을 이용하여 해결
# 주어진 문자를 (알파벳, 인덱스) 순으로 정렬 후
# pop하면서 앞에 나온 인덱스보다 큰 인덱스로만 정렬