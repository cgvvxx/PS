# solved: [118667] 두 큐 합 같게 만들기
# https://programmers.co.kr/learn/courses/30/lessons/118667
# data-structure
# 
# Level 2
# 자료구조 - 큐(덱)
# 두 큐의 합을 같게 하기 위하여 합이 작은 큐에서 pop하여 합이 큰 큐로 append하는 과정을 반복
# 해당 과정을 반복하면서 합이 같은 경우 cnt를 return
# 두 큐의 길이의 합의 2배보다 큰 경우(pop과 append를 한바퀴 이상 돈 경우) 합이 같아지는 경우가 없으므로 -1을 return

from collections import deque

def solution(queue1, queue2):
    
    q1, q2 = deque(queue1), deque(queue2) 
    s1, s2 = sum(queue1), sum(queue2)
    l = 2 * (len(queue1) + len(queue2))
    
    cnt = 0
    
    while True:
        
        if s1 == s2:
            return cnt
        elif s1 > s2:
            p = q1.popleft()
            q2.append(p)
            s1 -= p
            s2 += p
        else:
            p = q2.popleft()
            q1.append(p)
            s2 -= p
            s1 += p
            
        l -= 1
        cnt += 1
            
        if l == 0:
            return -1
 