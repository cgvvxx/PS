# Baekjoon 14719 - 빗물
# Gold 5


h, w = map(int, input().split())
arr = list(map(int, input().split()))

hs = [-1]
max_h = -1
answer = 0

for i in arr:
    if max_h < i:
        answer += sum(map(lambda x:max_h-x, hs))
        hs = [i]
        max_h = i        
    else:
        hs.append(i)
        if i > max_h:
            max_h = i
            
rh = -1
for j in hs[::-1]:
    if j > rh:
        rh = j
    else:
        answer += rh - j
        
print(answer)


# 어렵지 않은 구현인듯
# 최대 높이와 그 때 까지의 높이들을 저장하는 리스트를 이용해서 다음 최대 높이가 나타날 때
# 최대 높이와 그 높이들의 차이만큼 빗물의 양을 추가
# 마지막에 담겨진 높이는 따로 처리 ; 뒤에서 부터 더 큰 높이가 나오면 그 차이만큼 +