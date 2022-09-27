# solved: [118670] 행렬과 연산
# https://programmers.co.kr/learn/courses/30/lessons/118670
# data-structure
# 
# Level 4
# 자료구조 - 덱 또는 연결리스트
# 행렬에서 각 연산을 직접 수행하게 되면 효율성 테스트 통과 X
# 주어진 행렬을 쪼개서 덱 또는 연결리스트를 이용하면 각 연산을 O(1)에 해결가능
# 참고 >> https://nahwasa.com/entry/%EC%9E%90%EB%B0%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%89%EB%A0%AC%EA%B3%BC-%EC%97%B0%EC%82%B0-Lv4-Java
# 열의 개수(c==2)인 경우는 나누어서 생각해야함

from collections import deque

def solution(rc, operations):
    
    if len(rc[0]) == 2:
        
        l = deque([row[0] for row in rc])
        r = deque([row[-1] for row in rc])
        
        for op in operations:
            if op == "ShiftRow":
                l.rotate(1)
                r.rotate(1)
            else:
                r.appendleft(l.popleft())
                l.append(r.pop())  
            
        return [[l[i], r[i]] for i in range(len(rc))]

    else:
    
        l = deque([row[0] for row in rc])
        r = deque([row[-1] for row in rc])
        c = deque(map(lambda x:deque(x[1:-1]), rc))

        for op in operations:
            if op == "ShiftRow":
                c.rotate(1)
                l.rotate(1)
                r.rotate(1)
            else:
                c[0].appendleft(l.popleft())
                r.appendleft(c[0].pop())
                c[-1].append(r.pop())
                l.append(c[-1].popleft())

        return [[l[i]] + list(c[i]) + [r[i]] for i in range(len(rc))]
 