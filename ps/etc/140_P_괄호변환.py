# Programmers - 괄호 변환
# Level 2


def is_balanced(p):
    
    if not p:
        return True
        
    stack = []
    for char in p:
        if not stack:
            if char == ')':
                return False
            else:
                stack.append(char)
                continue
        
        if char == '(':
            stack.append(char)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True
    

def p_split(p):
    
    u_bal = [0, 0]
    for idx in range(len(p)):
        
        if p[idx] == "(":
            u_bal[0] += 1
        else:
            u_bal[1] += 1
            
        if u_bal[0] == u_bal[1]:
            break
    
    return p[:idx+1], p[idx+1:]


def p_reverse(p):
    
    ans = ''
    for char in p:
        if char == '(':
            ans += ')'
        else:
            ans += '('
    return ans


def solution(p):
    
    if is_balanced(p):
        return p
    
    while p:

        u, v = p_split(p)
        if is_balanced(u):
            return u + solution(v)
        else:
            v = '(' + solution(v) + ')' + p_reverse(u[1:-1])
            return v
            
    return ans


# 문제에서 요구하는 조건 맞춰서 차례대로 구현
# 재귀적으로 !