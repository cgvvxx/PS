# Baekjoon 12904 - A와 B
# Gold 5


def backward(w):
    
    if w[-1] == 'A':
        return w[:-1]
    else:
        return w[:-1][::-1]    

    
s = input()
t = input()

while True:
    
    t = backward(t)
    
    if t == s:
        print(1)
        break
    
    if len(t) < len(s):
        print(0)
        break
    


# 역으로 t > s로 갈때 가는 경우는 1가지 밖에 없음
# A로 끝나는 경우 그 전 단어까지 / B로 끝나는 경우 그 전 단어까지의 역순
# 따라서 t에서 시작해서 s의 길이가 같을 때까지 돌린 후 그 단어가 s랑 같은지 확인