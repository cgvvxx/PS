# Baekjoon 1213 - 팰린드롬 만들기
# Silver 4


from collections import Counter

c = Counter(input())

cnt = 0
impossible = False
for val in c.values():
    if val % 2 == 1:
        cnt += 1
    
    if cnt >= 2:
        impossible = True
        break
        
ans = ''
if impossible:
    print("I'm Sorry Hansoo")
else:
    keys = list(c.keys())
    keys.sort()
    for key in keys:
        while c[key] and c[key] > 1:
            ans += key
            c[key] -= 2

    if any(c.values()):
        for key in keys:
            if c[key]:
                ans += key
        ans += ans[:-1][::-1]
    else:
        ans += ans[::-1]
    
    print(ans)


# 주어진 문자열로 팰린드롬 만들기
# Counter 이용해서 각 문자마다의 개수를 카운팅 한 후 홀수 개수가 2개 이상이면 X
# 짝수 개수인 경우 keys를 sort해서 앞의 문자열부터 하나씩 추가