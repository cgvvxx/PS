# Baekjoon 21314 - 민겸수
# Silver 1
# Greedy


s = input()

max_ans = ''
min_ans = ''
temp = ''
for char in s:
    if char == 'M':
        temp += char        
    else:
        if temp:
            max_ans += str(5 * 10 ** len(temp))
            min_ans += str(10 ** (len(temp)-1)) + '5'
            temp = ''
        else:
            max_ans += '5'
            min_ans += '5'
if temp:
    max_ans += '1' * len(temp)
    min_ans += str(10 ** (len(temp)-1))

print(max_ans)
print(min_ans)


# K가 나왔을 때 큰수는 K를 포함하여, 작은수는 K를 포함하지 않고 변환하는 경우
# 다만 마지막에 M이 남았을 때 큰 수는 각각의 M을 1로
# 작은 수는 전체를 10의 거듭제곱으로 바꿔주어야 함! >> 이 부분의 반례를 생각해내는게 오래 걸림
# ex. MKMMMM
# 501111
# 151000