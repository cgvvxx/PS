# Programmers - 짝지어 제거하기
# Level 2
# 스택/큐

def solution(s):
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
            continue
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

    return 0 if stack else 1