# Programmers - 튜플
# Level 2

def str2list(s): # 집합 모양의 string을 원소는 set, 전체는 list 형태로 바꿈
    
    ret_list = []
    num = ''
    
    for char in s[1:-1]:
        if char == '{':
            stack = set()
            ing = True
        elif char == '}':
            stack.add(int(num))
            num = ''
            ret_list.append(stack)
            ing = False
        elif char == ',':
            if ing:
                stack.add(int(num))
                num = ''
        else:
            num += char
    
    return ret_list

def solution(s):
    
    s_list = str2list(s)
    s_list.sort(key=len) # 주어진 리스트를 길이 순으로 정렬
    
    answer = [set(s_list[0]).pop()] # 첫번째 원소를 append하고 시작
    tup_prior = s_list[0]

    for tup in s_list[1:]: 
        element = tup - tup_prior # 두 set의 차집합에서 원소를 구함
        tup_prior = tup
        answer.append(element.pop())
        
    return answer