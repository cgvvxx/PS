# Baekjoon 14405 - 피카츄
# Silver 5


s = input()

pikachus = ['pi', 'ka', 'chu']
check = ''
for i in range(len(s)):
    
    check += s[i]
    
    if check in pikachus:
        check = ''
        
if check:
    print('NO')
else:
    print('YES')
    

# 간단한 문제