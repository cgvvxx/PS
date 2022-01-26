# Baekjoon 17413 - 단어 뒤집기 2
# Silver 3


temp = ''
opened = False
for s in input():
    
    temp += s
    
    if s == ' ':
        if not opened:
            print(temp[:-1][::-1], end=' ')
            temp = ''
    elif s == '<':
        opened = True
        if temp:
            print(temp[:-1][::-1], end='')
            temp = '<'
    elif s == '>':
        opened = False
        print(temp, end='')
        temp = ''
        
if temp:
    print(temp[::-1])
    

# 경우를 ' ', '<', '>' 나눠서 구현
# 이 때 '<' 안에 ' ' 있는 case 고려
# 역순으로 프린트 할 때 [::-1]