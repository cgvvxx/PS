# Programmers - 괄호 회전하기
# Level 2
# 스택/큐


from collections import deque

def solution(s):
    
    def is_ok(s):
    
        char_dict = {'{':'}', '(':')', '[':']'}
        stack = []

        for char in s:
            if char in char_dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                open_char = stack.pop()
                if char_dict[open_char] != char:
                    return False
        
        if stack:
            return False
        
        return True
    
    queue = deque(s)
    count = 0
    
    for _ in range(len(s)):
        
        queue.append(queue.popleft())
        check_s = ''.join(list(queue))
        
        if is_ok(check_s):
            count += 1
    
    return count