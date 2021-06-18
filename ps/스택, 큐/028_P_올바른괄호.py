# Programmers - 올바른 괄호
# Level 2
# 스택/큐

def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False